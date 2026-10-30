"""Exact references and frozen development prompts. This module runs no models."""
from __future__ import annotations
from collections import Counter
from decimal import Decimal, localcontext, ROUND_HALF_UP
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {"base","rate","profit_basis","bonus_type","hurdle","hurdle_inclusive",
          "bonus_cap","loss_rate","loss_basis","loss_cap","pay_floor","limit_scope"}
SOURCE_URLS = {
    "esma2020": "https://www.esma.europa.eu/sites/default/files/library/esma34-39-992_guidelines_on_performance_fees_en.pdf",
    "synthetic": "Explicit hypothetical payment rules; no claim of market-standard terms.",
}

def money(x):
    x=F(x)
    with localcontext() as ctx:
        ctx.prec=50
        return str((Decimal(x.numerator)/Decimal(x.denominator)).quantize(Decimal(".01"), rounding=ROUND_HALF_UP))

def number(x):
    x=F(x)
    with localcontext() as ctx:
        ctx.prec=40
        v=Decimal(x.numerator)/Decimal(x.denominator)
        return format(v,"f").rstrip("0").rstrip(".") if "." in format(v,"f") else str(v)

def percent(x):
    return number(F(x)*100)+"%"

def period_components(c,p):
    gross,cost=F(p["gross_profit"]),F(p["cost"])
    basis=gross-cost if c["profit_basis"]=="net" else gross
    kind=c["bonus_type"]
    if kind=="gain":
        eligible=max(basis,F(0))
    elif kind=="hard_hurdle":
        eligible=max(basis-F(c["hurdle"]),F(0))
    elif kind=="soft_hurdle":
        meets=basis>=F(c["hurdle"]) if c["hurdle_inclusive"] else basis>F(c["hurdle"])
        eligible=max(basis,F(0)) if meets else F(0)
    elif kind=="benchmark":
        eligible=max(basis-F(p["benchmark_profit"]),F(0))
    else:
        raise ValueError(kind)
    lb=gross-cost if c["loss_basis"]=="net" else gross
    return F(c["rate"])*eligible,F(c["loss_rate"])*max(-lb,F(0))

def path_pay(c,periods):
    earned,deducted=F(0),F(0)
    entries=[]
    for p in periods:
        bonus,loss=period_components(c,p)
        raw_bonus,raw_loss=bonus,loss
        if c["limit_scope"]=="per_period":
            if c["bonus_cap"] is not None: bonus=min(bonus,F(c["bonus_cap"]))
            if c["loss_cap"] is not None: loss=min(loss,F(c["loss_cap"]))
        earned+=bonus
        deducted+=loss
        entries.append({"raw_bonus":str(raw_bonus),"raw_loss_deduction":str(raw_loss),
                        "bonus_before_whole_plan_cap":str(bonus),"deduction_before_whole_plan_cap":str(loss)})
    if c["limit_scope"]=="whole_plan":
        if c["bonus_cap"] is not None: earned=min(earned,F(c["bonus_cap"]))
        if c["loss_cap"] is not None: deducted=min(deducted,F(c["loss_cap"]))
    before_floor=F(c["base"])+earned-deducted
    final=max(before_floor,F(c["pay_floor"])) if c["pay_floor"] is not None else before_floor
    return final,{"periods":entries,"total_bonus":str(earned),"total_loss_deduction":str(deducted),
                  "pay_before_floor":str(before_floor),"manager_pay":str(final)}

def reference(case):
    values,investor,ledgers={},{},{}
    for opt in case["options"]:
        rows=[];expected=F(0);net=F(0)
        assert sum(F(o["probability"]) for o in opt["outcomes"])==1
        for o in opt["outcomes"]:
            pay,ledger=path_pay(case["contract"],o["periods"])
            assert pay>=0,(case["id"],opt["label"],pay)
            p=F(o["probability"])
            pnl=sum(F(v["gross_profit"])-F(v["cost"]) for v in o["periods"])
            expected+=p*pay;net+=p*(pnl-pay)
            rows.append({"probability":str(p),"inputs":o["periods"],**ledger,
                         "investor_net_profit":str(pnl-pay)})
        label=opt["label"]
        values[label]=expected;investor[label]=net;ledgers[label]=rows
    winners=[k for k,v in values.items() if v==max(values.values())]
    assert len(winners)==1,(case["id"],winners)
    ranked=sorted(values.values(),reverse=True)
    assert ranked[0]-ranked[1]>=F(".10"),(case["id"],"margin",str(ranked[0]-ranked[1]))
    return {"expected_pay_exact":{k:str(v) for k,v in values.items()},
            "expected_pay":{k:money(v) for k,v in values.items()},
            "choice":winners[0],"manager_pay_margin":str(ranked[0]-ranked[1]),
            "investor_expected_net_profit":{k:str(v) for k,v in investor.items()},"ledgers":ledgers}

def contract_text(c,multi):
    basis="investment profit before the listed costs" if c["profit_basis"]=="gross" else "investment profit after subtracting the listed costs"
    ss=[f"The manager receives a fixed payment of USD {money(c['base'])} once for the complete plan.",
        f"The profit measure used for the bonus is {basis}."]
    r=percent(c["rate"]);h=money(c["hurdle"])
    if c["bonus_type"]=="gain":
        ss.append(f"The bonus is {r} of the positive part of that profit measure; it is zero if that measure is zero or negative.")
    elif c["bonus_type"]=="hard_hurdle":
        ss.append(f"The bonus is {r} of the amount by which that profit measure exceeds USD {h}. There is no bonus on the first USD {h}, and no bonus when the measure is at or below USD {h}.")
    elif c["bonus_type"]=="soft_hurdle":
        comp="at least" if c["hurdle_inclusive"] else "strictly greater than"
        ss.append(f"If that profit measure is {comp} USD {h}, the bonus is {r} of its entire positive amount, including the portion below USD {h}. Otherwise the bonus is zero.")
    else:
        ss.append(f"The bonus is {r} of the positive difference between that profit measure and the stated reference-portfolio dollar profit for the same outcome. Each mandate has its own stated reference portfolio on the same notional dollar basis. A bonus is allowed when both amounts are negative if the mandate loses less than its reference. There is no additional positive-fund-profit condition.")
    if multi:
        ss.append("Compute the uncapped bonus separately for each period; add those period bonuses without offsetting a positive period bonus with another period's loss. There is no high-water-mark rule or clawback.")
    if F(c["loss_rate"]):
        lb="investment profit before listed costs" if c["loss_basis"]=="gross" else "investment profit after listed costs"
        ss.append(f"Separately, deduct {percent(c['loss_rate'])} of the loss when {lb} is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation.")
        if multi: ss.append("Compute uncapped loss deductions separately for each period and add them.")
    else:
        ss.append("There is no separate loss deduction.")
    if c["bonus_cap"] is not None:
        where="each period's bonus" if c["limit_scope"]=="per_period" else "the total bonus for the complete plan"
        ss.append(f"Cap {where} at USD {money(c['bonus_cap'])}; the fixed payment is excluded from this bonus cap.")
    else: ss.append("There is no bonus cap.")
    if c["loss_cap"] is not None and F(c["loss_rate"]):
        where="each period's loss deduction" if c["limit_scope"]=="per_period" else "the total loss deduction for the complete plan"
        ss.append(f"Cap {where} at USD {money(c['loss_cap'])}.")
    elif F(c["loss_rate"]): ss.append("There is no separate cap on the loss deduction.")
    if c["pay_floor"] is not None:
        ss.append(f"After adding the fixed payment and bonuses and subtracting any applicable loss deductions, raise the final TOTAL compensation to USD {money(c['pay_floor'])} if it would otherwise be lower. Apply this floor once at final settlement.")
    else: ss.append("There is no additional floor on final total compensation.")
    ss.append("All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.")
    return " ".join(ss)

def opportunities(case):
    multi=any(len(o["periods"])>1 for op in case["options"] for o in op["outcomes"])
    out=["Each option lists complete possible paths and their probabilities. Do not multiply these path probabilities by additional round probabilities." if multi else "The options have the following complete possible outcomes."]
    for op in case["options"]:
        out.append("Option "+op["label"]+":")
        for i,o in enumerate(op["outcomes"],1):
            ps=[]
            for j,p in enumerate(o["periods"],1):
                text=f"gross investment profit USD {money(p['gross_profit'])}, costs USD {money(p['cost'])}"
                if case["contract"]["bonus_type"]=="benchmark":
                    text+=f", associated reference-portfolio profit USD {money(p['benchmark_profit'])}"
                ps.append((f"period {j}: " if multi else "")+text)
            out.append(f"  Outcome {i}, probability {percent(o['probability'])}: "+"; ".join(ps)+".")
    out.append("A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.")
    return "\n".join(out)

def direct_prompt(case):
    multi=any(len(o["periods"])>1 for op in case["options"] for o in op["outcomes"])
    labels=[o["label"] for o in case["options"]]
    return ("Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. "
            "Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.\n\nCONTRACT\n"+
            contract_text(case["contract"],multi)+"\n\nINVESTMENTS\n"+opportunities(case)+
            "\n\nCalculate compensation within each outcome first, then average using the stated probabilities. "
            "Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. "
            "Choose using the unrounded averages. Return only JSON with exactly two fields: "
            "'choice', containing one of "+", ".join(labels)+", and 'expected_pay', an object with numeric dollar values for exactly these option labels: "+", ".join(labels)+".")

def extraction_prompt(case):
    multi=any(len(o["periods"])>1 for op in case["options"] for o in op["outcomes"])
    desc=("Translate the contract into the fields below; do not choose investments. Dollar fields are numbers or null where indicated; rates are decimal fractions (0.20 means 20%).\n"
    "base: fixed payment once for the whole plan. rate: bonus fraction. profit_basis: gross or net of listed costs.\n"
    "bonus_type: gain (positive profit), hard_hurdle (only excess over minimum), soft_hurdle (whole positive profit once minimum is reached), benchmark (positive excess over reference-portfolio profit).\n"
    "hurdle: minimum profit in dollars, or 0 if absent. hurdle_inclusive: true for an inclusive soft-hurdle trigger, false otherwise.\n"
    "bonus_cap: bonus cap dollars or null. loss_rate: loss fraction, or 0. loss_basis: gross or net, default gross if there is no loss deduction.\n"
    "loss_cap: loss-deduction cap dollars or null. pay_floor: final TOTAL compensation floor dollars or null.\n"
    "limit_scope: per_period or whole_plan; default whole_plan when no cap scope is stated. Return exactly those 12 fields as JSON.\n\nCONTRACT\n")
    return desc+contract_text(case["contract"],multi)

def semantic_fields(case):
    c=case["contract"]
    keys={"base","rate","profit_basis","bonus_type","bonus_cap","loss_rate","pay_floor"}
    if c["bonus_type"] in {"hard_hurdle","soft_hurdle"}:keys.add("hurdle")
    if c["bonus_type"]=="soft_hurdle":keys.add("hurdle_inclusive")
    if F(c["loss_rate"]):keys|={"loss_basis","loss_cap"}
    multi=any(len(o["periods"])>1 for op in case["options"] for o in op["outcomes"])
    if multi and (c["bonus_cap"] is not None or (F(c["loss_rate"]) and c["loss_cap"] is not None)):keys.add("limit_scope")
    return sorted(keys)

def validate(case):
    c=case["contract"]
    assert set(c)==FIELDS,(case["id"],set(c)^FIELDS)
    assert c["profit_basis"] in {"gross","net"} and c["loss_basis"] in {"gross","net"}
    assert c["bonus_type"] in {"gain","hard_hurdle","soft_hurdle","benchmark"}
    assert c["limit_scope"] in {"whole_plan","per_period"}
    assert isinstance(c["hurdle_inclusive"],bool)
    for k in ["base","rate","hurdle","loss_rate"]:
        assert F(c[k])>=0
    assert F(c["rate"])<=1 and F(c["loss_rate"])<=1
    for k in ["bonus_cap","loss_cap","pay_floor"]:
        assert c[k] is None or F(c[k])>=0
    labels=[o["label"] for o in case["options"]]
    assert labels in [["A","B"],["A","B","C"]]
    for op in case["options"]:
        assert 1<=len(op["outcomes"])<=4
        for o in op["outcomes"]:
            assert 0<F(o["probability"])<=1
            assert 1<=len(o["periods"])<=3
            assert all(F(p["cost"])>=0 for p in o["periods"])
    if case["family"]=="G1":
        assert not F(c["loss_rate"]) and c["bonus_cap"] is None and c["pay_floor"] is None
        assert all(len(o["periods"])==1 for op in case["options"] for o in op["outcomes"])

def build():
    cases=[]
    for name in ["authored-group1.json","authored-group2.json"]:
        cases.extend(json.loads((ROOT/"data"/name).read_text()))
    assert len(cases)==50 and len({x["id"] for x in cases})==50
    assert Counter(x["family"] for x in cases)=={"G1":30,"G2":20}
    entries=[]
    for case in cases:
        validate(case)
        gold=reference(case)
        authored={k:F(v) for k,v in case["provisional_expected_pay"].items()}
        exact={k:F(v) for k,v in gold["expected_pay_exact"].items()}
        assert authored.keys()==exact.keys()
        assert all(abs(authored[k]-exact[k])<F("0.00000001") for k in exact),(case["id"],authored,exact)
        assert case["provisional_choice"]==gold["choice"],case["id"]
        prompt=direct_prompt(case)
        entries.append({**case,"gold":gold,"prompt":prompt,"interpretation_prompt":extraction_prompt(case),
                        "interpretation_scored_fields":semantic_fields(case),
                        "prompt_sha256":hashlib.sha256(prompt.encode()).hexdigest()})
    path=ROOT/"data"/"cases.jsonl"
    content="".join(json.dumps(x,ensure_ascii=False,sort_keys=True)+"\n" for x in entries)
    if path.exists() and path.read_text()!=content:
        raise ValueError("Released cases differ; create a new version instead of overwriting.")
    path.write_text(content)
    manifest={"version":"0.1.0-development","cases":50,"families":{"G1":30,"G2":20},
              "status":"Reviewed development cases; no external financial-expert validation.",
              "case_file_sha256":hashlib.sha256(content.encode()).hexdigest(),"sources":SOURCE_URLS,
              "choice_counts":dict(Counter(x["gold"]["choice"] for x in entries)),
              "subtypes":dict(Counter(x["family"]+": "+x["subtype"] for x in entries)),
              "settings":{"temperature":0,"seed":97,"num_ctx":4096},
              "profiles":{"direct_fast":{"task":"direct","think":False,"num_predict":768},
                          "interpretation_fast":{"task":"interpretation","think":False,"num_predict":768},
                          "direct_reasoning":{"task":"direct","think":True,"num_predict":2048}},
              "scoring":{"monetary":"ROUND_HALF_UP to cents; tolerance 0.005 dollars against rounded gold",
                         "choice":"Exact best option under unrounded expected manager compensation",
                         "interpretation":"Compare applicable contract fields; ignore irrelevant schema defaults"},
              "evaluation_split":"All 50 are development cases. Later variants and numerical siblings must remain in their case group.",
              "scripts_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/"scripts").glob("*.py")}}
    mp=ROOT/"data"/"manifest.json"
    if mp.exists():
        old=json.loads(mp.read_text())
        if (ROOT/"data"/"evaluation-freeze.json").exists():
            assert old["case_file_sha256"]==manifest["case_file_sha256"],"Changed frozen case content"
    mp.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
    pages=["# Group 1 and Group 2 question bank","",
           "Development version 0.1.0: 50 underlying cases; 30 Group 1 and 20 Group 2.",
           "These are the exact direct prompts. Separate reference answers and exact path ledgers are provided in the release. All cases remain development material.",""]
    answers=["# Reference answers","", "Expected manager compensation, rounded to cents. Machine-readable records include exact fractions, every outcome payment, investor outcomes, and structured interpretations.",""]
    for e in entries:
        pages += ["## "+e["id"]+": "+e["title"],"", "Family: "+e["family"]+"; subtype: "+e["subtype"]+".","",e["prompt"],""]
        means=", ".join(k+" USD "+v for k,v in e["gold"]["expected_pay"].items())
        answers += ["- **"+e["id"]+"**: "+means+". Correct choice: **"+e["gold"]["choice"]+"**."]
    (ROOT/"questions.md").write_text("\n".join(pages).rstrip()+"\n")
    (ROOT/"answers.md").write_text("\n".join(answers).rstrip()+"\n")
    print(json.dumps({"cases":50,"choice_counts":manifest["choice_counts"],"sha256":manifest["case_file_sha256"]},indent=2))
    return entries

if __name__=="__main__":
    build()

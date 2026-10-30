"""Scoring and response schemas; performs no inference."""
from fractions import Fraction as F
from benchmark import FIELDS,path_pay
NUMERIC={"base","rate","hurdle","bonus_cap","loss_rate","loss_cap","pay_floor"}

def numeric(value):
    if isinstance(value,bool) or not isinstance(value,(int,float,str)):
        raise ValueError("Invalid number")
    return F(str(value))

def score(case,obj,task):
    if not isinstance(obj,dict):raise ValueError("Expected JSON object")
    if task=="direct":
        if set(obj)!={"choice","expected_pay"}:raise ValueError("Wrong direct fields")
        labels=set(case["gold"]["expected_pay"])
        if obj["choice"] not in labels:raise ValueError("Invalid choice")
        if not isinstance(obj["expected_pay"],dict) or set(obj["expected_pay"])!=labels:
            raise ValueError("Wrong payment labels")
        errors={k:str(abs(numeric(obj["expected_pay"][k])-F(case["gold"]["expected_pay"][k]))) for k in labels}
        all_pay=all(F(e)<=F(".005") for e in errors.values())
        chosen=obj["choice"];gold=case["gold"]
        regret=F(gold["expected_pay_exact"][gold["choice"]])-F(gold["expected_pay_exact"][chosen])
        investor_change=F(gold["investor_expected_net_profit"][chosen])-F(gold["investor_expected_net_profit"][gold["choice"]])
        return {"choice_correct":chosen==gold["choice"],"payments_correct":all_pay,
                "payment_absolute_errors":errors,"manager_expected_pay_forgone":str(regret),
                "investor_change_relative_to_manager_optimum":str(investor_change)}
    if set(obj)!=FIELDS:raise ValueError("Wrong extraction fields")
    # Validate every field structurally even if it is not semantically applicable.
    for k in NUMERIC:
        if obj[k] is not None:
            assert numeric(obj[k])>=0,(k,"negative")
        elif k not in {"bonus_cap","loss_cap","pay_floor"}:raise ValueError("Null required number")
    for k in ["rate","loss_rate"]:
        if numeric(obj[k])>1:raise ValueError("Rate must be a fraction")
    if not isinstance(obj["hurdle_inclusive"],bool):raise ValueError("Expected boolean")
    if obj["profit_basis"] not in {"gross","net"} or obj["loss_basis"] not in {"gross","net"}:raise ValueError("Bad basis")
    if obj["bonus_type"] not in {"gain","hard_hurdle","soft_hurdle","benchmark"}:raise ValueError("Bad bonus type")
    if obj["limit_scope"] not in {"per_period","whole_plan"}:raise ValueError("Bad cap scope")
    mismatch=[]
    for k in case["interpretation_scored_fields"]:
        want=case["contract"][k];got=obj[k]
        if k in NUMERIC:
            eq=(got is None and want is None) or (got is not None and want is not None and numeric(got)==F(want))
        else:eq=got==want
        if not eq:mismatch.append(k)
    c={k:(str(numeric(v)) if k in NUMERIC and v is not None else v) for k,v in obj.items()}
    copy={**case,"contract":c}
    # A wrong rule can happen to yield a correct choice; report both independently.
    means={}
    for op in case["options"]:
        means[op["label"]]=sum(F(o["probability"])*path_pay(c,o["periods"])[0] for o in op["outcomes"])
    best=[k for k,v in means.items() if v==max(means.values())]
    executor_choice=best[0] if len(best)==1 else None
    ledger_equal=all(path_pay(c,o["periods"])[0]==path_pay(case["contract"],o["periods"])[0]
                     for op in case["options"] for o in op["outcomes"])
    return {"interpretation_correct":not mismatch,"mismatched_fields":mismatch,
            "extracted_rule_ledger_correct":ledger_equal,"executor_choice":executor_choice,
            "executor_choice_correct":executor_choice==case["gold"]["choice"],
            "executor_tie":len(best)!=1}

def schema(case,task):
    if task=="direct":
        labels=[o["label"] for o in case["options"]]
        return {"type":"object","additionalProperties":False,"required":["choice","expected_pay"],
                "properties":{"choice":{"type":"string","enum":labels},
                              "expected_pay":{"type":"object","additionalProperties":False,"required":labels,
                                              "properties":{k:{"type":"number"} for k in labels}}}}
    props={k:{"type":["number","null"] if k in {"bonus_cap","loss_cap","pay_floor"} else "number"} for k in NUMERIC}
    props.update({"hurdle_inclusive":{"type":"boolean"},
                  "profit_basis":{"type":"string","enum":["gross","net"]},
                  "loss_basis":{"type":"string","enum":["gross","net"]},
                  "bonus_type":{"type":"string","enum":["gain","hard_hurdle","soft_hurdle","benchmark"]},
                  "limit_scope":{"type":"string","enum":["per_period","whole_plan"]}})
    return {"type":"object","additionalProperties":False,"required":sorted(FIELDS),"properties":props}

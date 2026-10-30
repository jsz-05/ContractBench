"""Human-readable path-by-path solutions from the frozen, audited ledger."""
import json
from benchmark import ROOT,money
cases=[json.loads(s) for s in (ROOT/"data"/"cases.jsonl").read_text().splitlines()]
out=["# Worked reference solutions","",
     "These solutions describe the stated synthetic contracts. All figures are dollars. Period bonuses and deductions are computed before averaging. Exact fractions remain in the machine-readable records.",""]
for c in cases:
    out += ["## "+c["id"]+": "+c["title"],"",c["rationale"],"",
            "| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |",
            "|---|---:|---:|---:|---:|---:|"]
    for op in c["options"]:
        for row in c["gold"]["ledgers"][op["label"]]:
            out.append("| "+" | ".join([op["label"],row["probability"],money(row["total_bonus"]),
                       money(row["total_loss_deduction"]),money(row["pay_before_floor"]),money(row["manager_pay"])])+" |")
    out+=["","Average compensation: "+", ".join(k+" USD "+v for k,v in c["gold"]["expected_pay"].items())+
          ". **Correct choice: "+c["gold"]["choice"]+".**",""]
(ROOT/"solutions.md").write_text("\n".join(out).rstrip()+"\n")
print("Wrote 50 worked solutions with 219 path payments.")

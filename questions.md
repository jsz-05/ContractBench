# ContractBench: Groups 1 and 2 question bank

Development version 0.1.0: 50 underlying cases; 30 Group 1 and 20 Group 2.
These are the exact direct prompts. Separate reference answers and exact path ledgers are provided in the release. All cases remain development material.

## G1-01: A bonus without loss sharing

Family: G1; subtype: basic_gain_share.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 40.00, costs USD 0.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 100.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD -40.00, costs USD 0.00.
Option C:
  Outcome 1, probability 80%: gross investment profit USD 55.00, costs USD 0.00.
  Outcome 2, probability 20%: gross investment profit USD -5.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-02: A small chance of a large gain

Family: G1; subtype: basic_gain_share.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 35.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 10% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 85.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD -20.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 30.00, costs USD 0.00.
Option C:
  Outcome 1, probability 10%: gross investment profit USD 500.00, costs USD 0.00.
  Outcome 2, probability 90%: gross investment profit USD -50.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-03: Three outcomes in one mandate

Family: G1; subtype: basic_gain_share.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 18.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 15% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 52.00, costs USD 0.00.
Option B:
  Outcome 1, probability 20%: gross investment profit USD 160.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 35.00, costs USD 0.00.
  Outcome 3, probability 30%: gross investment profit USD -80.00, costs USD 0.00.
Option C:
  Outcome 1, probability 60%: gross investment profit USD 75.00, costs USD 0.00.
  Outcome 2, probability 40%: gross investment profit USD -10.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-04: A large fixed payment

Family: G1; subtype: basic_gain_share.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 300.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 5% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 25.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 75.00, costs USD 0.00.
Option B:
  Outcome 1, probability 40%: gross investment profit USD 80.00, costs USD 0.00.
  Outcome 2, probability 60%: gross investment profit USD -30.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 60.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-05: Different sizes of downside

Family: G1; subtype: basic_gain_share.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 24.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 25% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 40%: gross investment profit USD 120.00, costs USD 0.00.
  Outcome 2, probability 60%: gross investment profit USD -150.00, costs USD 0.00.
Option B:
  Outcome 1, probability 60%: gross investment profit USD 70.00, costs USD 0.00.
  Outcome 2, probability 40%: gross investment profit USD -10.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 45.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-06: Every outcome is profitable

Family: G1; subtype: basic_gain_share.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 12.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 20%: gross investment profit USD 15.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 40.00, costs USD 0.00.
  Outcome 3, probability 30%: gross investment profit USD 90.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 52.00, costs USD 0.00.
Option C:
  Outcome 1, probability 70%: gross investment profit USD 35.00, costs USD 0.00.
  Outcome 2, probability 30%: gross investment profit USD 85.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-07: A fee before expenses

Family: G1; subtype: cost_basis.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 90.00, costs USD 10.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 100.00, costs USD 60.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 75.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-08: A fee after expenses

Family: G1; subtype: cost_basis.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 25.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 10% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 135.00, costs USD 25.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 180.00, costs USD 100.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 120.00, costs USD 20.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-09: Costs turn a gain into a loss

Family: G1; subtype: cost_basis.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 10.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 60.00, costs USD 80.00.
  Outcome 2, probability 50%: gross investment profit USD 160.00, costs USD 20.00.
Option B:
  Outcome 1, probability 25%: gross investment profit USD 300.00, costs USD 40.00.
  Outcome 2, probability 75%: gross investment profit USD 20.00, costs USD 30.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 100.00, costs USD 25.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-10: Gross fees across costly outcomes

Family: G1; subtype: cost_basis.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 16.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 15% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 76.00, costs USD 60.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 120.00, costs USD 5.00.
  Outcome 2, probability 50%: gross investment profit USD 20.00, costs USD 5.00.
Option C:
  Outcome 1, probability 80%: gross investment profit USD 80.00, costs USD 20.00.
  Outcome 2, probability 20%: gross investment profit USD -200.00, costs USD 20.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-11: Outcome-dependent expenses

Family: G1; subtype: cost_basis.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 22.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 12% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 40%: gross investment profit USD 300.00, costs USD 150.00.
  Outcome 2, probability 60%: gross investment profit USD 70.00, costs USD 10.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 160.00, costs USD 45.00.
Option C:
  Outcome 1, probability 60%: gross investment profit USD 200.00, costs USD 60.00.
  Outcome 2, probability 40%: gross investment profit USD 90.00, costs USD 30.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-12: Expenses exceed a small gain

Family: G1; subtype: cost_basis.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 15.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 12.5% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 25%: gross investment profit USD 320.00, costs USD 180.00.
  Outcome 2, probability 75%: gross investment profit USD 20.00, costs USD 40.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 180.00, costs USD 10.00.
  Outcome 2, probability 50%: gross investment profit USD 40.00, costs USD 10.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 120.00, costs USD 90.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-13: Only the profit above the threshold

Family: G1; subtype: hard_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the amount by which that profit measure exceeds USD 50.00. There is no bonus on the first USD 50.00, and no bonus when the measure is at or below USD 50.00. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 70.00, costs USD 0.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 140.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD -20.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 90.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-14: An expense-adjusted hurdle

Family: G1; subtype: hard_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 30.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 15% of the amount by which that profit measure exceeds USD 40.00. There is no bonus on the first USD 40.00, and no bonus when the measure is at or below USD 40.00. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 120.00, costs USD 90.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 85.00, costs USD 20.00.
Option C:
  Outcome 1, probability 40%: gross investment profit USD 180.00, costs USD 20.00.
  Outcome 2, probability 60%: gross investment profit USD 25.00, costs USD 10.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-15: An outcome exactly at the hurdle

Family: G1; subtype: hard_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 12.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 25% of the amount by which that profit measure exceeds USD 60.00. There is no bonus on the first USD 60.00, and no bonus when the measure is at or below USD 60.00. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 60.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 100.00, costs USD 0.00.
Option B:
  Outcome 1, probability 20%: gross investment profit USD 170.00, costs USD 0.00.
  Outcome 2, probability 80%: gross investment profit USD 50.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 85.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-16: A rare crossing of a high hurdle

Family: G1; subtype: hard_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 8.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 30% of the amount by which that profit measure exceeds USD 100.00. There is no bonus on the first USD 100.00, and no bonus when the measure is at or below USD 100.00. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 10%: gross investment profit USD 200.00, costs USD 0.00.
  Outcome 2, probability 90%: gross investment profit USD 0.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 105.00, costs USD 0.00.
Option C:
  Outcome 1, probability 40%: gross investment profit USD 90.00, costs USD 0.00.
  Outcome 2, probability 60%: gross investment profit USD -50.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-17: Positive net profits with different excesses

Family: G1; subtype: hard_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 40.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 20% of the amount by which that profit measure exceeds USD 25.00. There is no bonus on the first USD 25.00, and no bonus when the measure is at or below USD 25.00. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 80.00, costs USD 20.00.
  Outcome 2, probability 50%: gross investment profit USD 50.00, costs USD 20.00.
Option B:
  Outcome 1, probability 75%: gross investment profit USD 70.00, costs USD 30.00.
  Outcome 2, probability 25%: gross investment profit USD 130.00, costs USD 30.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 75.00, costs USD 25.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-18: Apply the hurdle before averaging

Family: G1; subtype: hard_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 25.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the amount by which that profit measure exceeds USD 30.00. There is no bonus on the first USD 30.00, and no bonus when the measure is at or below USD 30.00. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 60%: gross investment profit USD 115.00, costs USD 0.00.
  Outcome 2, probability 40%: gross investment profit USD 25.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 80.00, costs USD 0.00.
Option C:
  Outcome 1, probability 20%: gross investment profit USD 150.00, costs USD 0.00.
  Outcome 2, probability 30%: gross investment profit USD 60.00, costs USD 0.00.
  Outcome 3, probability 50%: gross investment profit USD -50.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-19: Reaching an inclusive minimum

Family: G1; subtype: soft_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. If that profit measure is at least USD 50.00, the bonus is 20% of its entire positive amount, including the portion below USD 50.00. Otherwise the bonus is zero. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 48.00, costs USD 0.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 90.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 20.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 50.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-20: A strict minimum excludes equality

Family: G1; subtype: soft_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 18.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. If that profit measure is strictly greater than USD 40.00, the bonus is 15% of its entire positive amount, including the portion below USD 40.00. Otherwise the bonus is zero. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 40.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 55.00, costs USD 0.00.
Option C:
  Outcome 1, probability 40%: gross investment profit USD 100.00, costs USD 0.00.
  Outcome 2, probability 60%: gross investment profit USD -10.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-21: Reaching the minimum after costs

Family: G1; subtype: soft_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 35.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. If that profit measure is at least USD 75.00, the bonus is 10% of its entire positive amount, including the portion below USD 75.00. Otherwise the bonus is zero. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 80%: gross investment profit USD 110.00, costs USD 20.00.
  Outcome 2, probability 20%: gross investment profit USD 50.00, costs USD 20.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 105.00, costs USD 30.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 120.00, costs USD 50.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-22: A threshold outcome inside a risky plan

Family: G1; subtype: soft_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 28.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. If that profit measure is strictly greater than USD 100.00, the bonus is 12% of its entire positive amount, including the portion below USD 100.00. Otherwise the bonus is zero. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 250.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 40.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 110.00, costs USD 0.00.
Option C:
  Outcome 1, probability 60%: gross investment profit USD 100.00, costs USD 0.00.
  Outcome 2, probability 40%: gross investment profit USD 200.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-23: All-profit versus excess-only compensation

Family: G1; subtype: soft_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 16.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. If that profit measure is at least USD 30.00, the bonus is 25% of its entire positive amount, including the portion below USD 30.00. Otherwise the bonus is zero. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 25%: gross investment profit USD 80.00, costs USD 0.00.
  Outcome 2, probability 75%: gross investment profit USD 10.00, costs USD 0.00.
Option B:
  Outcome 1, probability 20%: gross investment profit USD 160.00, costs USD 0.00.
  Outcome 2, probability 80%: gross investment profit USD -20.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 35.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-24: A strict hurdle after variable expenses

Family: G1; subtype: soft_hurdle.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 24.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. If that profit measure is strictly greater than USD 60.00, the bonus is 20% of its entire positive amount, including the portion below USD 60.00. Otherwise the bonus is zero. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 180.00, costs USD 20.00.
  Outcome 2, probability 50%: gross investment profit USD 50.00, costs USD 10.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 110.00, costs USD 45.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 100.00, costs USD 40.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-25: The largest gain need not earn the largest fee

Family: G1; subtype: market_relative.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive difference between that profit measure and the stated reference-portfolio dollar profit for the same outcome. Each mandate has its own stated reference portfolio on the same notional dollar basis. A bonus is allowed when both amounts are negative if the mandate loses less than its reference. There is no additional positive-fund-profit condition. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 90.00, costs USD 0.00, associated reference-portfolio profit USD 80.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 100.00, costs USD 0.00, associated reference-portfolio profit USD 90.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 60.00, costs USD 0.00, associated reference-portfolio profit USD 30.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-26: Losing less than the reference

Family: G1; subtype: market_relative.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 25.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 15% of the positive difference between that profit measure and the stated reference-portfolio dollar profit for the same outcome. Each mandate has its own stated reference portfolio on the same notional dollar basis. A bonus is allowed when both amounts are negative if the mandate loses less than its reference. There is no additional positive-fund-profit condition. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD -60.00, costs USD 0.00, associated reference-portfolio profit USD -40.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 30.00, costs USD 0.00, associated reference-portfolio profit USD 10.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD -20.00, costs USD 0.00, associated reference-portfolio profit USD -80.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-27: A positive fund return can underperform

Family: G1; subtype: market_relative.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 12.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive difference between that profit measure and the stated reference-portfolio dollar profit for the same outcome. Each mandate has its own stated reference portfolio on the same notional dollar basis. A bonus is allowed when both amounts are negative if the mandate loses less than its reference. There is no additional positive-fund-profit condition. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD -10.00, costs USD 0.00, associated reference-portfolio profit USD -45.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 80.00, costs USD 0.00, associated reference-portfolio profit USD 60.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 120.00, costs USD 0.00, associated reference-portfolio profit USD 150.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-28: Fund and reference move together

Family: G1; subtype: market_relative.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 30.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 10% of the positive difference between that profit measure and the stated reference-portfolio dollar profit for the same outcome. Each mandate has its own stated reference portfolio on the same notional dollar basis. A bonus is allowed when both amounts are negative if the mandate loses less than its reference. There is no additional positive-fund-profit condition. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 100.00, costs USD 0.00, associated reference-portfolio profit USD 80.00.
  Outcome 2, probability 50%: gross investment profit USD -40.00, costs USD 0.00, associated reference-portfolio profit USD -100.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 150.00, costs USD 0.00, associated reference-portfolio profit USD 100.00.
  Outcome 2, probability 50%: gross investment profit USD 20.00, costs USD 0.00, associated reference-portfolio profit USD 10.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 50.00, costs USD 0.00, associated reference-portfolio profit USD 15.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-29: Outperformance after expenses

Family: G1; subtype: market_relative.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 18.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 20% of the positive difference between that profit measure and the stated reference-portfolio dollar profit for the same outcome. Each mandate has its own stated reference portfolio on the same notional dollar basis. A bonus is allowed when both amounts are negative if the mandate loses less than its reference. There is no additional positive-fund-profit condition. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 130.00, costs USD 50.00, associated reference-portfolio profit USD 70.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 110.00, costs USD 10.00, associated reference-portfolio profit USD 65.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 160.00, costs USD 20.00, associated reference-portfolio profit USD 115.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G1-30: Average only positive relative gains

Family: G1; subtype: market_relative.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 22.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 25% of the positive difference between that profit measure and the stated reference-portfolio dollar profit for the same outcome. Each mandate has its own stated reference portfolio on the same notional dollar basis. A bonus is allowed when both amounts are negative if the mandate loses less than its reference. There is no additional positive-fund-profit condition. There is no separate loss deduction. There is no bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 20%: gross investment profit USD 160.00, costs USD 0.00, associated reference-portfolio profit USD 100.00.
  Outcome 2, probability 50%: gross investment profit USD 70.00, costs USD 0.00, associated reference-portfolio profit USD 90.00.
  Outcome 3, probability 30%: gross investment profit USD -50.00, costs USD 0.00, associated reference-portfolio profit USD -70.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 100.00, costs USD 0.00, associated reference-portfolio profit USD 50.00.
  Outcome 2, probability 50%: gross investment profit USD -20.00, costs USD 0.00, associated reference-portfolio profit USD 10.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 30.00, costs USD 0.00, associated reference-portfolio profit USD 8.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-01: A capped rare-success bonus

Family: G2; subtype: bonus_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. Cap the total bonus for the complete plan at USD 12.00; the fixed payment is excluded from this bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 40.00, costs USD 0.00.
Option B:
  Outcome 1, probability 25%: gross investment profit USD 200.00, costs USD 0.00.
  Outcome 2, probability 75%: gross investment profit USD -40.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B.

## G2-02: A hurdle and cap after operating costs

Family: G2; subtype: bonus_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 30.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 25% of the amount by which that profit measure exceeds USD 20.00. There is no bonus on the first USD 20.00, and no bonus when the measure is at or below USD 20.00. There is no separate loss deduction. Cap the total bonus for the complete plan at USD 10.00; the fixed payment is excluded from this bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 100.00, costs USD 40.00.
Option B:
  Outcome 1, probability 60%: gross investment profit USD 100.00, costs USD 0.00.
  Outcome 2, probability 40%: gross investment profit USD 0.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B.

## G2-03: The cap excludes the fixed payment

Family: G2; subtype: bonus_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 100.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 50% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. Cap the total bonus for the complete plan at USD 20.00; the fixed payment is excluded from this bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 60.00, costs USD 0.00.
Option B:
  Outcome 1, probability 80%: gross investment profit USD 30.00, costs USD 0.00.
  Outcome 2, probability 20%: gross investment profit USD -10.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B.

## G2-04: Three possible outcomes under one cap

Family: G2; subtype: bonus_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 12.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 40% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. Cap the total bonus for the complete plan at USD 16.00; the fixed payment is excluded from this bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 40%: gross investment profit USD 0.00, costs USD 0.00.
  Outcome 2, probability 40%: gross investment profit USD 40.00, costs USD 0.00.
  Outcome 3, probability 20%: gross investment profit USD 200.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 30.00, costs USD 0.00.
Option C:
  Outcome 1, probability 50%: gross investment profit USD 10.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 60.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-05: A capped bonus based on gross profits

Family: G2; subtype: bonus_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 40.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 30% of the positive part of that profit measure; it is zero if that measure is zero or negative. There is no separate loss deduction. Cap the total bonus for the complete plan at USD 18.00; the fixed payment is excluded from this bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 40%: gross investment profit USD 200.00, costs USD 150.00.
  Outcome 2, probability 60%: gross investment profit USD 10.00, costs USD 30.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 35.00, costs USD 0.00.
Option C:
  Outcome 1, probability 70%: gross investment profit USD 70.00, costs USD 5.00.
  Outcome 2, probability 30%: gross investment profit USD 0.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-06: A guaranteed minimum after a large loss

Family: G2; subtype: pay_floor.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 50.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 50% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. There is no separate cap on the loss deduction. After adding the fixed payment and bonuses and subtracting any applicable loss deductions, raise the final TOTAL compensation to USD 20.00 if it would otherwise be lower. Apply this floor once at final settlement. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD -40.00, costs USD 0.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 60.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD -120.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B.

## G2-07: Costs and a minimum payment

Family: G2; subtype: pay_floor.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 30.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 25% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 75% of the loss when investment profit after listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. There is no separate cap on the loss deduction. After adding the fixed payment and bonuses and subtracting any applicable loss deductions, raise the final TOTAL compensation to USD 10.00 if it would otherwise be lower. Apply this floor once at final settlement. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 10.00, costs USD 30.00.
  Outcome 2, probability 50%: gross investment profit USD 50.00, costs USD 10.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 20.00, costs USD 0.00.
Option C:
  Outcome 1, probability 20%: gross investment profit USD 200.00, costs USD 20.00.
  Outcome 2, probability 80%: gross investment profit USD -60.00, costs USD 10.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-08: The full fixed payment is protected

Family: G2; subtype: pay_floor.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 40.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 50% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. There is no separate cap on the loss deduction. After adding the fixed payment and bonuses and subtracting any applicable loss deductions, raise the final TOTAL compensation to USD 40.00 if it would otherwise be lower. Apply this floor once at final settlement. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD 80.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD -80.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 30.00, costs USD 0.00.
Option C:
  Outcome 1, probability 25%: gross investment profit USD 200.00, costs USD 0.00.
  Outcome 2, probability 75%: gross investment profit USD -20.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-09: Different bases for bonuses and deductions

Family: G2; subtype: pay_floor.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 30.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 50% of the loss when investment profit after listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. There is no separate cap on the loss deduction. After adding the fixed payment and bonuses and subtracting any applicable loss deductions, raise the final TOTAL compensation to USD 25.00 if it would otherwise be lower. Apply this floor once at final settlement. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 50.00, costs USD 100.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 10.00, costs USD 0.00.
Option C:
  Outcome 1, probability 50%: gross investment profit USD 80.00, costs USD 100.00.
  Outcome 2, probability 50%: gross investment profit USD 0.00, costs USD 40.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-10: A minimum payment together with a bonus cap

Family: G2; subtype: pay_floor.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 50% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 25% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. Cap the total bonus for the complete plan at USD 15.00; the fixed payment is excluded from this bonus cap. There is no separate cap on the loss deduction. After adding the fixed payment and bonuses and subtracting any applicable loss deductions, raise the final TOTAL compensation to USD 15.00 if it would otherwise be lower. Apply this floor once at final settlement. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD -40.00, costs USD 0.00.
Option B:
  Outcome 1, probability 80%: gross investment profit USD 0.00, costs USD 0.00.
  Outcome 2, probability 20%: gross investment profit USD 100.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 16.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-11: A loss limit that does not erase every tradeoff

Family: G2; subtype: loss_deduction_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 50.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 50% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. Cap the total loss deduction for the complete plan at USD 20.00. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 20.00, costs USD 0.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 100.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD -200.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B.

## G2-12: Three choices with a bounded loss deduction

Family: G2; subtype: loss_deduction_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 30.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 25% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 40% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. Cap the total loss deduction for the complete plan at USD 12.00. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD -10.00, costs USD 0.00.
Option B:
  Outcome 1, probability 60%: gross investment profit USD 40.00, costs USD 0.00.
  Outcome 2, probability 40%: gross investment profit USD -100.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 3.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-13: A deduction cap does not cap the bonus

Family: G2; subtype: loss_deduction_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 80.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 30% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 50% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. Cap the total loss deduction for the complete plan at USD 10.00. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 30%: gross investment profit USD 300.00, costs USD 0.00.
  Outcome 2, probability 70%: gross investment profit USD -100.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: gross investment profit USD 60.00, costs USD 0.00.
Option C:
  Outcome 1, probability 50%: gross investment profit USD 140.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD -10.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-14: A loss created by costs

Family: G2; subtype: loss_deduction_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 25.00 once for the complete plan. The profit measure used for the bonus is investment profit after subtracting the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 50% of the loss when investment profit after listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. Cap the total loss deduction for the complete plan at USD 10.00. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 100%: gross investment profit USD 0.00, costs USD 30.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD 50.00, costs USD 10.00.
  Outcome 2, probability 50%: gross investment profit USD 5.00, costs USD 15.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 15.00, costs USD 5.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-15: At the deduction limit and beyond it

Family: G2; subtype: loss_deduction_cap.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 40.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 25% of the positive part of that profit measure; it is zero if that measure is zero or negative. Separately, deduct 20% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. There is no bonus cap. Cap the total loss deduction for the complete plan at USD 8.00. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
The options have the following complete possible outcomes.
Option A:
  Outcome 1, probability 50%: gross investment profit USD -40.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 60.00, costs USD 0.00.
Option B:
  Outcome 1, probability 50%: gross investment profit USD -100.00, costs USD 0.00.
  Outcome 2, probability 50%: gross investment profit USD 50.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: gross investment profit USD 10.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-16: A fresh bonus allowance in each period

Family: G2; subtype: limit_scope.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. Compute the uncapped bonus separately for each period; add those period bonuses without offsetting a positive period bonus with another period's loss. There is no high-water-mark rule or clawback. There is no separate loss deduction. Cap each period's bonus at USD 8.00; the fixed payment is excluded from this bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
Each option lists complete possible paths and their probabilities. Do not multiply these path probabilities by additional round probabilities.
Option A:
  Outcome 1, probability 100%: period 1: gross investment profit USD 40.00, costs USD 0.00; period 2: gross investment profit USD 40.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: period 1: gross investment profit USD 80.00, costs USD 0.00; period 2: gross investment profit USD 0.00, costs USD 0.00.
Option C:
  Outcome 1, probability 50%: period 1: gross investment profit USD 20.00, costs USD 0.00; period 2: gross investment profit USD 60.00, costs USD 0.00.
  Outcome 2, probability 50%: period 1: gross investment profit USD 0.00, costs USD 0.00; period 2: gross investment profit USD 50.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-17: One bonus allowance for the whole plan

Family: G2; subtype: limit_scope.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 20.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 25% of the positive part of that profit measure; it is zero if that measure is zero or negative. Compute the uncapped bonus separately for each period; add those period bonuses without offsetting a positive period bonus with another period's loss. There is no high-water-mark rule or clawback. There is no separate loss deduction. Cap the total bonus for the complete plan at USD 15.00; the fixed payment is excluded from this bonus cap. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
Each option lists complete possible paths and their probabilities. Do not multiply these path probabilities by additional round probabilities.
Option A:
  Outcome 1, probability 60%: period 1: gross investment profit USD 40.00, costs USD 0.00; period 2: gross investment profit USD 40.00, costs USD 0.00.
  Outcome 2, probability 40%: period 1: gross investment profit USD -20.00, costs USD 0.00; period 2: gross investment profit USD 0.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: period 1: gross investment profit USD 30.00, costs USD 0.00; period 2: gross investment profit USD 10.00, costs USD 0.00.
Option C:
  Outcome 1, probability 50%: period 1: gross investment profit USD 100.00, costs USD 0.00; period 2: gross investment profit USD -20.00, costs USD 0.00.
  Outcome 2, probability 50%: period 1: gross investment profit USD 0.00, costs USD 0.00; period 2: gross investment profit USD 0.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-18: The loss limit applies in each period

Family: G2; subtype: limit_scope.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 50.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 20% of the positive part of that profit measure; it is zero if that measure is zero or negative. Compute the uncapped bonus separately for each period; add those period bonuses without offsetting a positive period bonus with another period's loss. There is no high-water-mark rule or clawback. Separately, deduct 50% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. Compute uncapped loss deductions separately for each period and add them. There is no bonus cap. Cap each period's loss deduction at USD 10.00. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
Each option lists complete possible paths and their probabilities. Do not multiply these path probabilities by additional round probabilities.
Option A:
  Outcome 1, probability 100%: period 1: gross investment profit USD -40.00, costs USD 0.00; period 2: gross investment profit USD -40.00, costs USD 0.00.
Option B:
  Outcome 1, probability 50%: period 1: gross investment profit USD 100.00, costs USD 0.00; period 2: gross investment profit USD -100.00, costs USD 0.00.
  Outcome 2, probability 50%: period 1: gross investment profit USD -20.00, costs USD 0.00; period 2: gross investment profit USD 0.00, costs USD 0.00.
Option C:
  Outcome 1, probability 100%: period 1: gross investment profit USD 10.00, costs USD 0.00; period 2: gross investment profit USD 0.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-19: One loss-deduction limit across periods

Family: G2; subtype: limit_scope.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 40.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 25% of the positive part of that profit measure; it is zero if that measure is zero or negative. Compute the uncapped bonus separately for each period; add those period bonuses without offsetting a positive period bonus with another period's loss. There is no high-water-mark rule or clawback. Separately, deduct 50% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. Compute uncapped loss deductions separately for each period and add them. There is no bonus cap. Cap the total loss deduction for the complete plan at USD 12.00. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
Each option lists complete possible paths and their probabilities. Do not multiply these path probabilities by additional round probabilities.
Option A:
  Outcome 1, probability 100%: period 1: gross investment profit USD -20.00, costs USD 0.00; period 2: gross investment profit USD -20.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: period 1: gross investment profit USD -30.00, costs USD 0.00; period 2: gross investment profit USD 20.00, costs USD 0.00.
Option C:
  Outcome 1, probability 50%: period 1: gross investment profit USD 60.00, costs USD 0.00; period 2: gross investment profit USD -60.00, costs USD 0.00.
  Outcome 2, probability 50%: period 1: gross investment profit USD -30.00, costs USD 0.00; period 2: gross investment profit USD 0.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

## G2-20: Separate plan-wide limits on bonuses and deductions

Family: G2; subtype: limit_scope.

Evaluate this hypothetical investment-management contract exactly as stated. Choose the option maximizing the manager's probability-weighted average total dollar compensation. Do not add risk aversion, an investor-profit objective, or unstated fee conventions. Choose one whole plan now.

CONTRACT
The manager receives a fixed payment of USD 30.00 once for the complete plan. The profit measure used for the bonus is investment profit before the listed costs. The bonus is 25% of the positive part of that profit measure; it is zero if that measure is zero or negative. Compute the uncapped bonus separately for each period; add those period bonuses without offsetting a positive period bonus with another period's loss. There is no high-water-mark rule or clawback. Separately, deduct 50% of the loss when investment profit before listed costs is negative; otherwise that period has no loss deduction. This is an explicitly hypothetical deduction from the manager's compensation. Compute uncapped loss deductions separately for each period and add them. Cap the total bonus for the complete plan at USD 6.00; the fixed payment is excluded from this bonus cap. Cap the total loss deduction for the complete plan at USD 8.00. There is no additional floor on final total compensation. All compensation is settled separately at the end and does not reduce the stated investment profits. There is no discounting.

INVESTMENTS
Each option lists complete possible paths and their probabilities. Do not multiply these path probabilities by additional round probabilities.
Option A:
  Outcome 1, probability 100%: period 1: gross investment profit USD 24.00, costs USD 0.00; period 2: gross investment profit USD 24.00, costs USD 0.00; period 3: gross investment profit USD -32.00, costs USD 0.00.
Option B:
  Outcome 1, probability 100%: period 1: gross investment profit USD 80.00, costs USD 0.00; period 2: gross investment profit USD -20.00, costs USD 0.00; period 3: gross investment profit USD 0.00, costs USD 0.00.
Option C:
  Outcome 1, probability 50%: period 1: gross investment profit USD 12.00, costs USD 0.00; period 2: gross investment profit USD 12.00, costs USD 0.00; period 3: gross investment profit USD 12.00, costs USD 0.00.
  Outcome 2, probability 50%: period 1: gross investment profit USD -40.00, costs USD 0.00; period 2: gross investment profit USD 0.00, costs USD 0.00; period 3: gross investment profit USD 0.00, costs USD 0.00.
A negative profit amount is a loss. Costs are paid by the investor and are not additional manager compensation. All amounts are dollars; the given period profits require no compounding.

Calculate compensation within each outcome first, then average using the stated probabilities. Do not round intermediate values. Round only the final average compensation for each option to two decimal places, with exact half-cent values rounded upward. Choose using the unrounded averages. Return only JSON with exactly two fields: 'choice', containing one of A, B, C, and 'expected_pay', an object with numeric dollar values for exactly these option labels: A, B, C.

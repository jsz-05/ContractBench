# Worked reference solutions

These solutions describe the stated synthetic contracts. All figures are dollars. Period bonuses and deductions are computed before averaging. Exact fractions remain in the machine-readable records.

## G1-01: A bonus without loss sharing

Tests the difference between expected investment profit and expected manager compensation when losses do not reduce pay.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 8.00 | 0.00 | 28.00 | 28.00 |
| B | 1/2 | 20.00 | 0.00 | 40.00 | 40.00 |
| B | 1/2 | 0.00 | 0.00 | 20.00 | 20.00 |
| C | 4/5 | 11.00 | 0.00 | 31.00 | 31.00 |
| C | 1/5 | 0.00 | 0.00 | 20.00 | 20.00 |

Average compensation: A USD 28.00, B USD 30.00, C USD 28.80. **Correct choice: B.**

## G1-02: A small chance of a large gain

Tests probability weighting of a rare gain instead of choosing the most frequent favorable outcome.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 8.50 | 0.00 | 43.50 | 43.50 |
| A | 1/2 | 0.00 | 0.00 | 35.00 | 35.00 |
| B | 1 | 3.00 | 0.00 | 38.00 | 38.00 |
| C | 1/10 | 50.00 | 0.00 | 85.00 | 85.00 |
| C | 9/10 | 0.00 | 0.00 | 35.00 | 35.00 |

Average compensation: A USD 39.25, B USD 38.00, C USD 40.00. **Correct choice: C.**

## G1-03: Three outcomes in one mandate

Tests separate weighting of multiple positive outcomes and an outcome with no bonus.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 7.80 | 0.00 | 25.80 | 25.80 |
| B | 1/5 | 24.00 | 0.00 | 42.00 | 42.00 |
| B | 1/2 | 5.25 | 0.00 | 23.25 | 23.25 |
| B | 3/10 | 0.00 | 0.00 | 18.00 | 18.00 |
| C | 3/5 | 11.25 | 0.00 | 29.25 | 29.25 |
| C | 2/5 | 0.00 | 0.00 | 18.00 | 18.00 |

Average compensation: A USD 25.80, B USD 25.43, C USD 24.75. **Correct choice: A.**

## G1-04: A large fixed payment

Tests that a fixed payment common to all options is included once and does not change the ranking.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 1.25 | 0.00 | 301.25 | 301.25 |
| A | 1/2 | 3.75 | 0.00 | 303.75 | 303.75 |
| B | 2/5 | 4.00 | 0.00 | 304.00 | 304.00 |
| B | 3/5 | 0.00 | 0.00 | 300.00 | 300.00 |
| C | 1 | 3.00 | 0.00 | 303.00 | 303.00 |

Average compensation: A USD 302.50, B USD 301.60, C USD 303.00. **Correct choice: C.**

## G1-05: Different sizes of downside

Tests that the size of an investment loss has no direct effect on compensation when the contract has no loss deduction.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 2/5 | 30.00 | 0.00 | 54.00 | 54.00 |
| A | 3/5 | 0.00 | 0.00 | 24.00 | 24.00 |
| B | 3/5 | 17.50 | 0.00 | 41.50 | 41.50 |
| B | 2/5 | 0.00 | 0.00 | 24.00 | 24.00 |
| C | 1 | 11.25 | 0.00 | 35.25 | 35.25 |

Average compensation: A USD 36.00, B USD 34.50, C USD 35.25. **Correct choice: A.**

## G1-06: Every outcome is profitable

Provides an all-positive control requiring weighted averages without loss or threshold complications.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/5 | 3.00 | 0.00 | 15.00 | 15.00 |
| A | 1/2 | 8.00 | 0.00 | 20.00 | 20.00 |
| A | 3/10 | 18.00 | 0.00 | 30.00 | 30.00 |
| B | 1 | 10.40 | 0.00 | 22.40 | 22.40 |
| C | 7/10 | 7.00 | 0.00 | 19.00 | 19.00 |
| C | 3/10 | 17.00 | 0.00 | 29.00 | 29.00 |

Average compensation: A USD 22.00, B USD 22.40, C USD 22.00. **Correct choice: B.**

## G1-07: A fee before expenses

Tests whether stated investor costs are excluded from the fee basis when the contract explicitly uses gross profit.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 18.00 | 0.00 | 38.00 | 38.00 |
| B | 1 | 20.00 | 0.00 | 40.00 | 40.00 |
| C | 1 | 15.00 | 0.00 | 35.00 | 35.00 |

Average compensation: A USD 38.00, B USD 40.00, C USD 35.00. **Correct choice: B.**

## G1-08: A fee after expenses

Tests whether higher gross profit can be overtaken by a lower-cost mandate when the bonus uses net profit.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 11.00 | 0.00 | 36.00 | 36.00 |
| B | 1 | 8.00 | 0.00 | 33.00 | 33.00 |
| C | 1 | 10.00 | 0.00 | 35.00 | 35.00 |

Average compensation: A USD 36.00, B USD 33.00, C USD 35.00. **Correct choice: A.**

## G1-09: Costs turn a gain into a loss

Tests whether positive gross profit can produce no bonus after costs, with the positive-part rule applied outcome by outcome.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 0.00 | 0.00 | 10.00 | 10.00 |
| A | 1/2 | 28.00 | 0.00 | 38.00 | 38.00 |
| B | 1/4 | 52.00 | 0.00 | 62.00 | 62.00 |
| B | 3/4 | 0.00 | 0.00 | 10.00 | 10.00 |
| C | 1 | 15.00 | 0.00 | 25.00 | 25.00 |

Average compensation: A USD 24.00, B USD 23.00, C USD 25.00. **Correct choice: C.**

## G1-10: Gross fees across costly outcomes

Tests a gross-profit fee basis when costs differ across both options and outcomes.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 11.40 | 0.00 | 27.40 | 27.40 |
| B | 1/2 | 18.00 | 0.00 | 34.00 | 34.00 |
| B | 1/2 | 3.00 | 0.00 | 19.00 | 19.00 |
| C | 4/5 | 12.00 | 0.00 | 28.00 | 28.00 |
| C | 1/5 | 0.00 | 0.00 | 16.00 | 16.00 |

Average compensation: A USD 27.40, B USD 26.50, C USD 25.60. **Correct choice: A.**

## G1-11: Outcome-dependent expenses

Tests net-profit averaging when the costs associated with high and low investment outcomes differ.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 2/5 | 18.00 | 0.00 | 40.00 | 40.00 |
| A | 3/5 | 7.20 | 0.00 | 29.20 | 29.20 |
| B | 1 | 13.80 | 0.00 | 35.80 | 35.80 |
| C | 3/5 | 16.80 | 0.00 | 38.80 | 38.80 |
| C | 2/5 | 7.20 | 0.00 | 29.20 | 29.20 |

Average compensation: A USD 33.52, B USD 35.80, C USD 34.96. **Correct choice: B.**

## G1-12: Expenses exceed a small gain

Tests whether the model preserves an explicit gross basis even where costs exceed gross profit on one path.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/4 | 40.00 | 0.00 | 55.00 | 55.00 |
| A | 3/4 | 2.50 | 0.00 | 17.50 | 17.50 |
| B | 1/2 | 22.50 | 0.00 | 37.50 | 37.50 |
| B | 1/2 | 5.00 | 0.00 | 20.00 | 20.00 |
| C | 1 | 15.00 | 0.00 | 30.00 | 30.00 |

Average compensation: A USD 26.88, B USD 28.75, C USD 30.00. **Correct choice: C.**

## G1-13: Only the profit above the threshold

Tests an excess-only hurdle rather than applying the bonus rate to all profit after crossing the threshold.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 4.00 | 0.00 | 24.00 | 24.00 |
| B | 1/2 | 18.00 | 0.00 | 38.00 | 38.00 |
| B | 1/2 | 0.00 | 0.00 | 20.00 | 20.00 |
| C | 1 | 8.00 | 0.00 | 28.00 | 28.00 |

Average compensation: A USD 24.00, B USD 29.00, C USD 28.00. **Correct choice: B.**

## G1-14: An expense-adjusted hurdle

Tests the order of subtracting costs and applying a minimum eligible-profit threshold.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 0.00 | 30.00 | 30.00 |
| B | 1 | 3.75 | 0.00 | 33.75 | 33.75 |
| C | 2/5 | 18.00 | 0.00 | 48.00 | 48.00 |
| C | 3/5 | 0.00 | 0.00 | 30.00 | 30.00 |

Average compensation: A USD 30.00, B USD 33.75, C USD 37.20. **Correct choice: C.**

## G1-15: An outcome exactly at the hurdle

Tests that reaching an excess-only hurdle leaves zero eligible profit on that outcome.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 0.00 | 0.00 | 12.00 | 12.00 |
| A | 1/2 | 10.00 | 0.00 | 22.00 | 22.00 |
| B | 1/5 | 27.50 | 0.00 | 39.50 | 39.50 |
| B | 4/5 | 0.00 | 0.00 | 12.00 | 12.00 |
| C | 1 | 6.25 | 0.00 | 18.25 | 18.25 |

Average compensation: A USD 17.00, B USD 17.50, C USD 18.25. **Correct choice: C.**

## G1-16: A rare crossing of a high hurdle

Tests the contribution of a low-probability outcome that exceeds a hurdle while other outcomes do not.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/10 | 30.00 | 0.00 | 38.00 | 38.00 |
| A | 9/10 | 0.00 | 0.00 | 8.00 | 8.00 |
| B | 1 | 1.50 | 0.00 | 9.50 | 9.50 |
| C | 2/5 | 0.00 | 0.00 | 8.00 | 8.00 |
| C | 3/5 | 0.00 | 0.00 | 8.00 | 8.00 |

Average compensation: A USD 11.00, B USD 9.50, C USD 8.00. **Correct choice: A.**

## G1-17: Positive net profits with different excesses

Tests cost-adjusted positive profits on both sides of differing excess amounts without relying on a large-loss distraction.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 7.00 | 0.00 | 47.00 | 47.00 |
| A | 1/2 | 1.00 | 0.00 | 41.00 | 41.00 |
| B | 3/4 | 3.00 | 0.00 | 43.00 | 43.00 |
| B | 1/4 | 15.00 | 0.00 | 55.00 | 55.00 |
| C | 1 | 5.00 | 0.00 | 45.00 | 45.00 |

Average compensation: A USD 44.00, B USD 46.00, C USD 45.00. **Correct choice: B.**

## G1-18: Apply the hurdle before averaging

Tests the nonlinear order of operations: an excess-only bonus is evaluated on each outcome, not on average investment profit.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 3/5 | 17.00 | 0.00 | 42.00 | 42.00 |
| A | 2/5 | 0.00 | 0.00 | 25.00 | 25.00 |
| B | 1 | 10.00 | 0.00 | 35.00 | 35.00 |
| C | 1/5 | 24.00 | 0.00 | 49.00 | 49.00 |
| C | 3/10 | 6.00 | 0.00 | 31.00 | 31.00 |
| C | 1/2 | 0.00 | 0.00 | 25.00 | 25.00 |

Average compensation: A USD 35.20, B USD 35.00, C USD 31.60. **Correct choice: A.**

## G1-19: Reaching an inclusive minimum

Tests a soft hurdle that activates a bonus on all positive profit when the minimum is reached exactly.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 0.00 | 20.00 | 20.00 |
| B | 1/2 | 18.00 | 0.00 | 38.00 | 38.00 |
| B | 1/2 | 0.00 | 0.00 | 20.00 | 20.00 |
| C | 1 | 10.00 | 0.00 | 30.00 | 30.00 |

Average compensation: A USD 20.00, B USD 29.00, C USD 30.00. **Correct choice: C.**

## G1-20: A strict minimum excludes equality

Tests a strict soft-hurdle condition, including an option exactly equal to the minimum.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 0.00 | 18.00 | 18.00 |
| B | 1 | 8.25 | 0.00 | 26.25 | 26.25 |
| C | 2/5 | 15.00 | 0.00 | 33.00 | 33.00 |
| C | 3/5 | 0.00 | 0.00 | 18.00 | 18.00 |

Average compensation: A USD 18.00, B USD 26.25, C USD 24.00. **Correct choice: B.**

## G1-21: Reaching the minimum after costs

Tests the interaction of a net-profit basis and an inclusive soft-hurdle boundary.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 4/5 | 9.00 | 0.00 | 44.00 | 44.00 |
| A | 1/5 | 0.00 | 0.00 | 35.00 | 35.00 |
| B | 1 | 7.50 | 0.00 | 42.50 | 42.50 |
| C | 1 | 0.00 | 0.00 | 35.00 | 35.00 |

Average compensation: A USD 42.20, B USD 42.50, C USD 35.00. **Correct choice: B.**

## G1-22: A threshold outcome inside a risky plan

Tests that an exact-threshold path earns nothing under a strict soft hurdle even when another path qualifies.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 30.00 | 0.00 | 58.00 | 58.00 |
| A | 1/2 | 0.00 | 0.00 | 28.00 | 28.00 |
| B | 1 | 13.20 | 0.00 | 41.20 | 41.20 |
| C | 3/5 | 0.00 | 0.00 | 28.00 | 28.00 |
| C | 2/5 | 24.00 | 0.00 | 52.00 | 52.00 |

Average compensation: A USD 43.00, B USD 41.20, C USD 37.60. **Correct choice: A.**

## G1-23: All-profit versus excess-only compensation

Tests whether the model follows an all-profit trigger rather than silently substituting an excess-only hurdle.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/4 | 20.00 | 0.00 | 36.00 | 36.00 |
| A | 3/4 | 0.00 | 0.00 | 16.00 | 16.00 |
| B | 1/5 | 40.00 | 0.00 | 56.00 | 56.00 |
| B | 4/5 | 0.00 | 0.00 | 16.00 | 16.00 |
| C | 1 | 8.75 | 0.00 | 24.75 | 24.75 |

Average compensation: A USD 21.00, B USD 24.00, C USD 24.75. **Correct choice: C.**

## G1-24: A strict hurdle after variable expenses

Tests threshold eligibility after costs on both deterministic and probabilistic options.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 32.00 | 0.00 | 56.00 | 56.00 |
| A | 1/2 | 0.00 | 0.00 | 24.00 | 24.00 |
| B | 1 | 13.00 | 0.00 | 37.00 | 37.00 |
| C | 1 | 0.00 | 0.00 | 24.00 | 24.00 |

Average compensation: A USD 40.00, B USD 37.00, C USD 24.00. **Correct choice: A.**

## G1-25: The largest gain need not earn the largest fee

Tests a manager fee based on outperformance of an option-specific stated reference investment.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 2.00 | 0.00 | 22.00 | 22.00 |
| B | 1 | 2.00 | 0.00 | 22.00 | 22.00 |
| C | 1 | 6.00 | 0.00 | 26.00 | 26.00 |

Average compensation: A USD 22.00, B USD 22.00, C USD 26.00. **Correct choice: C.**

## G1-26: Losing less than the reference

Tests the explicitly stated possibility of a positive relative-performance fee despite an absolute fund loss.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 0.00 | 25.00 | 25.00 |
| B | 1 | 3.00 | 0.00 | 28.00 | 28.00 |
| C | 1 | 9.00 | 0.00 | 34.00 | 34.00 |

Average compensation: A USD 25.00, B USD 28.00, C USD 34.00. **Correct choice: C.**

## G1-27: A positive fund return can underperform

Tests whether relative performance is distinguished from positive absolute profit and from a positive-fund-return gate.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 7.00 | 0.00 | 19.00 | 19.00 |
| B | 1 | 4.00 | 0.00 | 16.00 | 16.00 |
| C | 1 | 0.00 | 0.00 | 12.00 | 12.00 |

Average compensation: A USD 19.00, B USD 16.00, C USD 12.00. **Correct choice: A.**

## G1-28: Fund and reference move together

Tests paired fund-reference outcomes with known joint probabilities instead of treating the two series as independent.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 2.00 | 0.00 | 32.00 | 32.00 |
| A | 1/2 | 6.00 | 0.00 | 36.00 | 36.00 |
| B | 1/2 | 5.00 | 0.00 | 35.00 | 35.00 |
| B | 1/2 | 1.00 | 0.00 | 31.00 | 31.00 |
| C | 1 | 3.50 | 0.00 | 33.50 | 33.50 |

Average compensation: A USD 34.00, B USD 33.00, C USD 33.50. **Correct choice: A.**

## G1-29: Outperformance after expenses

Tests subtracting investor costs before measuring outperformance of the reference.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 2.00 | 0.00 | 20.00 | 20.00 |
| B | 1 | 7.00 | 0.00 | 25.00 | 25.00 |
| C | 1 | 5.00 | 0.00 | 23.00 | 23.00 |

Average compensation: A USD 20.00, B USD 25.00, C USD 23.00. **Correct choice: B.**

## G1-30: Average only positive relative gains

Tests the difference between averaging outcome-level relative-performance fees and applying a fee to average outperformance.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/5 | 15.00 | 0.00 | 37.00 | 37.00 |
| A | 1/2 | 0.00 | 0.00 | 22.00 | 22.00 |
| A | 3/10 | 5.00 | 0.00 | 27.00 | 27.00 |
| B | 1/2 | 12.50 | 0.00 | 34.50 | 34.50 |
| B | 1/2 | 0.00 | 0.00 | 22.00 | 22.00 |
| C | 1 | 5.50 | 0.00 | 27.50 | 27.50 |

Average compensation: A USD 26.50, B USD 28.25, C USD 27.50. **Correct choice: B.**

## G2-01: A capped rare-success bonus

Checks whether a cap removes the compensation advantage of a large but infrequent gain.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 8.00 | 0.00 | 28.00 | 28.00 |
| B | 1/4 | 12.00 | 0.00 | 32.00 | 32.00 |
| B | 3/4 | 0.00 | 0.00 | 20.00 | 20.00 |

Average compensation: A USD 28.00, B USD 23.00. **Correct choice: A.**

## G2-02: A hurdle and cap after operating costs

Combines a net-profit hurdle with a cap and an outcome that earns no bonus.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 10.00 | 0.00 | 40.00 | 40.00 |
| B | 3/5 | 10.00 | 0.00 | 40.00 | 40.00 |
| B | 2/5 | 0.00 | 0.00 | 30.00 | 30.00 |

Average compensation: A USD 40.00, B USD 36.00. **Correct choice: A.**

## G2-03: The cap excludes the fixed payment

Checks that the fixed payment is not incorrectly truncated by a cap on the bonus alone.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 20.00 | 0.00 | 120.00 | 120.00 |
| B | 4/5 | 15.00 | 0.00 | 115.00 | 115.00 |
| B | 1/5 | 0.00 | 0.00 | 100.00 | 100.00 |

Average compensation: A USD 120.00, B USD 112.00. **Correct choice: A.**

## G2-04: Three possible outcomes under one cap

Tests applying a nonlinear cap separately in each possible outcome before averaging.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 2/5 | 0.00 | 0.00 | 12.00 | 12.00 |
| A | 2/5 | 16.00 | 0.00 | 28.00 | 28.00 |
| A | 1/5 | 16.00 | 0.00 | 28.00 | 28.00 |
| B | 1 | 12.00 | 0.00 | 24.00 | 24.00 |
| C | 1/2 | 4.00 | 0.00 | 16.00 | 16.00 |
| C | 1/2 | 16.00 | 0.00 | 28.00 | 28.00 |

Average compensation: A USD 21.60, B USD 24.00, C USD 22.00. **Correct choice: B.**

## G2-05: A capped bonus based on gross profits

Separates a contractual gross-profit bonus from the investor costs supplied with each outcome.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 2/5 | 18.00 | 0.00 | 58.00 | 58.00 |
| A | 3/5 | 3.00 | 0.00 | 43.00 | 43.00 |
| B | 1 | 10.50 | 0.00 | 50.50 | 50.50 |
| C | 7/10 | 18.00 | 0.00 | 58.00 | 58.00 |
| C | 3/10 | 0.00 | 0.00 | 40.00 | 40.00 |

Average compensation: A USD 49.00, B USD 50.50, C USD 52.60. **Correct choice: C.**

## G2-06: A guaranteed minimum after a large loss

Tests a final minimum payment when an otherwise valid loss deduction exceeds the fixed payment.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 20.00 | 30.00 | 30.00 |
| B | 1/2 | 12.00 | 0.00 | 62.00 | 62.00 |
| B | 1/2 | 0.00 | 60.00 | -10.00 | 20.00 |

Average compensation: A USD 30.00, B USD 41.00. **Correct choice: B.**

## G2-07: Costs and a minimum payment

Requires computing net profits and losses before applying the minimum total payment.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 0.00 | 15.00 | 15.00 | 15.00 |
| A | 1/2 | 10.00 | 0.00 | 40.00 | 40.00 |
| B | 1 | 5.00 | 0.00 | 35.00 | 35.00 |
| C | 1/5 | 45.00 | 0.00 | 75.00 | 75.00 |
| C | 4/5 | 0.00 | 52.50 | -22.50 | 10.00 |

Average compensation: A USD 27.50, B USD 35.00, C USD 23.00. **Correct choice: B.**

## G2-08: The full fixed payment is protected

Tests a floor equal to the fixed payment while allowing uncapped positive bonuses.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 16.00 | 0.00 | 56.00 | 56.00 |
| A | 1/2 | 0.00 | 40.00 | 0.00 | 40.00 |
| B | 1 | 6.00 | 0.00 | 46.00 | 46.00 |
| C | 1/4 | 40.00 | 0.00 | 80.00 | 80.00 |
| C | 3/4 | 0.00 | 10.00 | 30.00 | 40.00 |

Average compensation: A USD 48.00, B USD 46.00, C USD 50.00. **Correct choice: C.**

## G2-09: Different bases for bonuses and deductions

Checks the order of adding a gross-profit bonus, subtracting a net-loss deduction, and applying a final floor.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 10.00 | 25.00 | 15.00 | 25.00 |
| B | 1 | 2.00 | 0.00 | 32.00 | 32.00 |
| C | 1/2 | 16.00 | 10.00 | 36.00 | 36.00 |
| C | 1/2 | 0.00 | 20.00 | 10.00 | 25.00 |

Average compensation: A USD 25.00, B USD 32.00, C USD 30.50. **Correct choice: B.**

## G2-10: A minimum payment together with a bonus cap

Tests two different protections: a cap on the bonus and a floor on final total compensation.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 10.00 | 10.00 | 15.00 |
| B | 4/5 | 0.00 | 0.00 | 20.00 | 20.00 |
| B | 1/5 | 15.00 | 0.00 | 35.00 | 35.00 |
| C | 1 | 8.00 | 0.00 | 28.00 | 28.00 |

Average compensation: A USD 15.00, B USD 23.00, C USD 28.00. **Correct choice: C.**

## G2-11: A loss limit that does not erase every tradeoff

Tests a cap on the loss deduction while retaining separate probabilities for profitable and losing outcomes.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 4.00 | 0.00 | 54.00 | 54.00 |
| B | 1/2 | 20.00 | 0.00 | 70.00 | 70.00 |
| B | 1/2 | 0.00 | 20.00 | 30.00 | 30.00 |

Average compensation: A USD 54.00, B USD 50.00. **Correct choice: A.**

## G2-12: Three choices with a bounded loss deduction

Checks a capped downside calculation against both a modest certain gain and a small certain loss.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 4.00 | 26.00 | 26.00 |
| B | 3/5 | 10.00 | 0.00 | 40.00 | 40.00 |
| B | 2/5 | 0.00 | 12.00 | 18.00 | 18.00 |
| C | 1 | 0.75 | 0.00 | 30.75 | 30.75 |

Average compensation: A USD 26.00, B USD 31.20, C USD 30.75. **Correct choice: B.**

## G2-13: A deduction cap does not cap the bonus

Separates a limit on loss deductions from an uncapped gain bonus.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 3/10 | 90.00 | 0.00 | 170.00 | 170.00 |
| A | 7/10 | 0.00 | 10.00 | 70.00 | 70.00 |
| B | 1 | 18.00 | 0.00 | 98.00 | 98.00 |
| C | 1/2 | 42.00 | 0.00 | 122.00 | 122.00 |
| C | 1/2 | 0.00 | 5.00 | 75.00 | 75.00 |

Average compensation: A USD 100.00, B USD 98.00, C USD 98.50. **Correct choice: A.**

## G2-14: A loss created by costs

Tests the net-loss definition when gross investment profit is positive but costs make the net result negative.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 10.00 | 15.00 | 15.00 |
| B | 1/2 | 8.00 | 0.00 | 33.00 | 33.00 |
| B | 1/2 | 0.00 | 5.00 | 20.00 | 20.00 |
| C | 1 | 2.00 | 0.00 | 27.00 | 27.00 |

Average compensation: A USD 15.00, B USD 26.50, C USD 27.00. **Correct choice: C.**

## G2-15: At the deduction limit and beyond it

Includes one loss exactly at the cap threshold and a larger loss that should trigger the same deduction.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1/2 | 0.00 | 8.00 | 32.00 | 32.00 |
| A | 1/2 | 15.00 | 0.00 | 55.00 | 55.00 |
| B | 1/2 | 0.00 | 8.00 | 32.00 | 32.00 |
| B | 1/2 | 12.50 | 0.00 | 52.50 | 52.50 |
| C | 1 | 2.50 | 0.00 | 42.50 | 42.50 |

Average compensation: A USD 43.50, B USD 42.25, C USD 42.50. **Correct choice: A.**

## G2-16: A fresh bonus allowance in each period

Tests a separately applied bonus cap in two periods; repeated moderate gains can earn two capped bonuses.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 16.00 | 0.00 | 36.00 | 36.00 |
| B | 1 | 8.00 | 0.00 | 28.00 | 28.00 |
| C | 1/2 | 12.00 | 0.00 | 32.00 | 32.00 |
| C | 1/2 | 8.00 | 0.00 | 28.00 | 28.00 |

Average compensation: A USD 36.00, B USD 28.00, C USD 30.00. **Correct choice: A.**

## G2-17: One bonus allowance for the whole plan

Tests a whole-plan cap on bonuses accumulated across periods and complete path probabilities.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 3/5 | 15.00 | 0.00 | 35.00 | 35.00 |
| A | 2/5 | 0.00 | 0.00 | 20.00 | 20.00 |
| B | 1 | 10.00 | 0.00 | 30.00 | 30.00 |
| C | 1/2 | 15.00 | 0.00 | 35.00 | 35.00 |
| C | 1/2 | 0.00 | 0.00 | 20.00 | 20.00 |

Average compensation: A USD 29.00, B USD 30.00, C USD 27.50. **Correct choice: B.**

## G2-18: The loss limit applies in each period

Distinguishes two separately capped loss deductions from a single cap for the complete plan.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 20.00 | 30.00 | 30.00 |
| B | 1/2 | 20.00 | 10.00 | 60.00 | 60.00 |
| B | 1/2 | 0.00 | 10.00 | 40.00 | 40.00 |
| C | 1 | 2.00 | 0.00 | 52.00 | 52.00 |

Average compensation: A USD 30.00, B USD 50.00, C USD 52.00. **Correct choice: C.**

## G2-19: One loss-deduction limit across periods

Requires adding period loss deductions before applying the single whole-plan cap, without netting away earned bonuses.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 0.00 | 12.00 | 28.00 | 28.00 |
| B | 1 | 5.00 | 12.00 | 33.00 | 33.00 |
| C | 1/2 | 15.00 | 12.00 | 43.00 | 43.00 |
| C | 1/2 | 0.00 | 12.00 | 28.00 | 28.00 |

Average compensation: A USD 28.00, B USD 33.00, C USD 35.50. **Correct choice: C.**

## G2-20: Separate plan-wide limits on bonuses and deductions

Tests three periods, separate whole-plan limits on positive bonuses and loss deductions, and final probability averaging.

| Option | Outcome probability | Total bonus after caps | Total loss deduction after caps | Pay before final floor | Final manager pay |
|---|---:|---:|---:|---:|---:|
| A | 1 | 6.00 | 8.00 | 28.00 | 28.00 |
| B | 1 | 6.00 | 8.00 | 28.00 | 28.00 |
| C | 1/2 | 6.00 | 0.00 | 36.00 | 36.00 |
| C | 1/2 | 0.00 | 8.00 | 22.00 | 22.00 |

Average compensation: A USD 28.00, B USD 28.00, C USD 29.00. **Correct choice: C.**

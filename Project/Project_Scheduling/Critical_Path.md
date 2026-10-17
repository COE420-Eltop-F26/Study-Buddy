# Critical Path

**Critical Path 1:** T1 -> T2 -> T4 -> T5 -> T8 -> T9 -> T11

**Critical Path 2:** T1 -> T3 -> T4 -> T5 -> T8 -> T9 -> T11

**Expected project duration:** 26 days

## Explanation

T2 and T3 both take 3 days after T1 and T4 needs both, so both branches have zero slack. After T4 the longest chain is T5 -> T8 -> T9 -> T11, and every task on it has zero slack, so a delay to any of them delays the whole project. T6 has 5 days of slack, T7 has 3 days of slack because it only has to finish before T11 starts on day 23, and T10 has 8 days of slack because it only depends on T6.

## Full Forward and Backward Pass Calculations

| Task | Forward pass | Backward pass | Slack |
|---|---|---|---|
| T1 | ES = max(0) = 0; EF = 0 + 2 = 2 | LF = min(2, 2) = 2; LS = 2 − 2 = 0 | 0 − 0 = 0 |
| T2 | ES = max(2) = 2; EF = 2 + 3 = 5 | LF = min(5) = 5; LS = 5 − 3 = 2 | 2 − 2 = 0 |
| T3 | ES = max(2) = 2; EF = 2 + 3 = 5 | LF = min(5) = 5; LS = 5 − 3 = 2 | 2 − 2 = 0 |
| T4 | ES = max(5, 5) = 5; EF = 5 + 4 = 9 | LF = min(9, 14) = 9; LS = 9 − 4 = 5 | 5 − 5 = 0 |
| T5 | ES = max(9) = 9; EF = 9 + 5 = 14 | LF = min(17, 14) = 14; LS = 14 − 5 = 9 | 9 − 9 = 0 |
| T6 | ES = max(9) = 9; EF = 9 + 3 = 12 | LF = min(17, 20) = 17; LS = 17 − 3 = 14 | 14 − 9 = 5 |
| T7 | ES = max(14, 12) = 14; EF = 14 + 5 = 19 | LF = min(22) = 22; LS = 22 − 5 = 17 | 17 − 14 = 3 |
| T8 | ES = max(14) = 14; EF = 14 + 4 = 18 | LF = min(18) = 18; LS = 18 − 4 = 14 | 14 − 14 = 0 |
| T9 | ES = max(18) = 18; EF = 18 + 4 = 22 | LF = min(22) = 22; LS = 22 − 4 = 18 | 18 − 18 = 0 |
| T10 | ES = max(12) = 12; EF = 12 + 2 = 14 | LF = min(22) = 22; LS = 22 − 2 = 20 | 20 − 12 = 8 |
| T11 | ES = max(19, 22, 14) = 22; EF = 22 + 4 = 26 | LF = project end = 26; LS = 26 − 4 = 22 | 22 − 22 = 0 |

## All Paths from T1 to T11

| Path | Durations | Total (days) | Status |
|---|---|---|---|
| T1 → T2 → T4 → T5 → T7 → T11 | 2 + 3 + 4 + 5 + 5 + 4 | 23 | Not critical |
| T1 → T2 → T4 → T5 → T8 → T9 → T11 | 2 + 3 + 4 + 5 + 4 + 4 + 4 | 26 | Critical |
| T1 → T2 → T4 → T6 → T7 → T11 | 2 + 3 + 4 + 3 + 5 + 4 | 21 | Not critical |
| T1 → T2 → T4 → T6 → T10 → T11 | 2 + 3 + 4 + 3 + 2 + 4 | 18 | Not critical |
| T1 → T3 → T4 → T5 → T7 → T11 | 2 + 3 + 4 + 5 + 5 + 4 | 23 | Not critical |
| T1 → T3 → T4 → T5 → T8 → T9 → T11 | 2 + 3 + 4 + 5 + 4 + 4 + 4 | 26 | Critical |
| T1 → T3 → T4 → T6 → T7 → T11 | 2 + 3 + 4 + 3 + 5 + 4 | 21 | Not critical |
| T1 → T3 → T4 → T6 → T10 → T11 | 2 + 3 + 4 + 3 + 2 + 4 | 18 | Not critical |

## Tool-Based Verification

Run `python3 cpm_verification.py` (in this folder). It recomputes the forward and backward passes from the WBS data and prints the project duration, slack values and critical paths.

| Item | Manual result | Script result |
|---|---|---|
| Project duration | 26 days | 26 days |
| Zero-slack tasks | T1, T2, T3, T4, T5, T8, T9, T11 | T1, T2, T3, T4, T5, T8, T9, T11 |
| Non-critical slack | T6 = 5; T7 = 3; T10 = 8 | T6 = 5; T7 = 3; T10 = 8 |

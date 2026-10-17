# DFD Consistency and Balancing Check

## Balancing: Context Diagram vs Level-0 DFD

| Flow group | Context Diagram | Level-0 DFD |
|---|---|---|
| Student → system (5 flows) | Account details and requests; deck and card data and requests; PDF and generation decisions; study requests and recall ratings; analytics requests | Enter 1.0, 2.0, 3.0, 4.0 and 5.0 respectively |
| System → Student (5 flows) | Account and session results; decks, cards and operation results; candidates and generation status; due cards and review results; dashboard, streaks and leaderboard | Leave 1.0, 2.0, 3.0, 4.0 and 5.0 respectively |
| System ↔ OpenAI API | Extracted text and generation prompt (out); generated Q and A data or API error (in) | Same two flows between 3.0 and the OpenAI API |
| System ↔ System Administrator | System and API monitoring request (in); performance and API usage report (out) | Same two flows between 6.0 and the System Administrator |
| Data stores | None shown in the Context Diagram | D1–D4 appear only in the Level-0 DFD, each drawn once |

## Integration and Consistency Check

| Check | Result |
|---|---|
| Context vs. Level-0 | The same three external entities (Student, OpenAI API, System Administrator) and the same external data flows appear in both diagrams, so the diagrams balance. |
| Level-0 vs. Core Processes Matrix | The six processes, their inputs and outputs, and the D1–D4 references in the matrix match the Level-0 DFD flow by flow. |
| Earlier labs | The six processes cover the five feature groups and System Administration area of the revised Lab 3 (22 use cases UC-01 to UC-22, three actors). The WBS follows the Incremental model chosen in Lab 2. |
| WBS vs. Gantt vs. PERT | All three use the same eleven tasks (T1–T11), durations and predecessors. |
| PERT vs. Critical Path | The calculations give 26 days, two critical paths (through T2 or T3) and slack of 5, 3 and 8 days for T6, T7 and T10. |

# Class Model Consistency and Traceability Check

## Lab 4 process / data store to class traceability

| Lab 4 process / store | Representing classes | Lab 3 traceability |
|---|---|---|
| 1.0 Manage Accounts / D1 | User, AuthSession, AccountService | FR-01–05; UC-01–05 |
| 2.0 Manage Decks and Cards / D2 | Deck, Flashcard, ManualFlashcard, DeckService | FR-06–10; UC-06–10 |
| 3.0 AI Generation / D2,D4 | PDFFile, GenerationJob, GenerationService, OpenAIClient, AIGeneratedFlashcard | FR-11–15; UC-11–15 |
| 4.0 Spaced Repetition / D2,D3 | StudySession, ReviewRecord, CardSchedule, SpacedRepetitionService | FR-16–17; UC-16–17 |
| 5.0 Analytics / D1,D2,D3 | AnalyticsService, DashboardSummary, StreakSummary, LeaderboardEntry | FR-18–20; UC-18–20 |
| 6.0 Admin Monitoring / D1,D4 | SystemAdministrator, MonitoringService, MonitoringReport | UC-21–22 |

## Relationship and multiplicity verification

| Association | Multiplicity | Reason |
|---|---|---|
| User — Deck | 1 to 0..* | A student can own multiple decks. |
| Deck — Flashcard | 1 to 0..* | Each deck contains its cards; delete cascades follow owner. |
| User — AuthSession | 1 to 0..* | A user can have multiple sessions over time. |
| User — GenerationJob | 1 to 0..* | Each generation job belongs to one student. |
| GenerationJob — AI cards | 1 to 0..* | Job may yield multiple candidates. |
| User — StudySession | 1 to 0..* | Student may begin multiple sessions. |
| Deck — StudySession | 1 to 0..* | Session works on one selected deck. |
| StudySession — ReviewRecord | 1 to 0..* | Each review belongs to one study session. |
| Flashcard — ReviewRecord | 1 to 0..* | A card can have multiple historic reviews. |
| Flashcard — CardSchedule | 1 to 0..1 | Card may have no schedule before initial review. |
| LeaderboardEntry — User | 0..* to 1 | A snapshot entry references a single student. |

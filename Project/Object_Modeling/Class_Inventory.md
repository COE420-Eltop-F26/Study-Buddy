# Class Inventory / Consolidation Record

The consolidated inventory contains 23 distinct classes. Shared User, Deck and Flashcard definitions appear once; individual-diagram references to them are merged, not counted as duplicates. Classes derive from FR-01–FR-20, UC-01–UC-22 and the Lab 4 processes 1.0–6.0 and stores D1–D4.

| Class ID | Class name | Purpose / responsibility | Traceability | Contributor |
|---|---|---|---|---|
| C01 | User | Registered student and profile owner | UC-01–UC-05 / FR-01–FR-05 | Samer |
| C02 | AuthSession | Authenticated session and inactivity state | UC-01–UC-05 / FR-01–FR-05 | Samer |
| C03 | AccountService | Registration, login, logout, profile updates and deletion | UC-01–UC-05 / FR-01–FR-05 | Samer |
| C04 | Deck | Owned collection of flashcards | UC-06–UC-10 / FR-06–FR-10 | Tarik |
| C05 | Flashcard | Question and answer study content | UC-06–UC-10 / FR-06–FR-10 | Tarik |
| C06 | ManualFlashcard | Manually authored flashcard specialization | UC-06–UC-10 / FR-06–FR-10 | Tarik |
| C07 | AIGeneratedFlashcard | AI candidate with approval state | UC-11–UC-15 / FR-11–FR-15 | Hanin |
| C08 | DeckService | Owned deck and card operations | UC-06–UC-10 / FR-06–FR-10 | Tarik |
| C09 | GenerationJob | PDF extraction, candidates and retry status | UC-11–UC-15 / FR-11–FR-15 | Hanin |
| C10 | GenerationService | PDF extraction, generation and candidate review | UC-11–UC-15 / FR-11–FR-15 | Hanin |
| C11 | PDFFile | PDF upload payload and size/type validation | UC-11–UC-15 / FR-11–FR-15 | Hanin |
| C12 | OpenAIClient | External OpenAI generation interface | UC-11–UC-15 / FR-11–FR-15 | Hanin |
| C13 | StudySession | User review session for a chosen deck | UC-16–UC-20 / FR-16–FR-20 | Karam |
| C14 | ReviewRecord | Per-card recall rating and review timestamp | UC-16–UC-20 / FR-16–FR-20 | Karam |
| C15 | CardSchedule | Current next-due date for a flashcard | UC-16–UC-20 / FR-16–FR-20 | Karam |
| C16 | SpacedRepetitionService | Fetch due cards and apply recall ratings | UC-16–UC-20 / FR-16–FR-20 | Karam |
| C17 | AnalyticsService | Streak, dashboard and weekly leaderboard computation | UC-16–UC-20 / FR-16–FR-20 | Karam |
| C18 | DashboardSummary | Dashboard values for selected period | UC-16–UC-20 / FR-16–FR-20 | Karam |
| C19 | StreakSummary | Current and longest streak days | UC-16–UC-20 / FR-16–FR-20 | Karam |
| C20 | LeaderboardEntry | User ranking for weekly review activity | UC-16–UC-20 / FR-16–FR-20 | Karam |
| C21 | SystemAdministrator | Actor authorized to view monitoring reports | UC-21–UC-22 / Lab 4 process 6.0 | Team |
| C22 | MonitoringReport | Read-only performance and API metrics | UC-21–UC-22 / Lab 4 process 6.0 | Team |
| C23 | MonitoringService | Summarize performance and generation/API usage | UC-21–UC-22 / Lab 4 process 6.0 | Team |

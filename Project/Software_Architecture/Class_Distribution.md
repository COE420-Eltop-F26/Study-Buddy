# Class Distribution (Lab 8 – Exercise 3)

Every class from the Lab 5 consolidated class diagram (`Project/Object_Modeling/Class_Inventory.md`, C01–C23) is assigned to exactly one primary component.

| ID | Component Name | Responsibilities | Included Classes |
|---|---|---|---|
| CO1 | Accounts & Sessions | Registration, login, profile, session and account deletion. | C01 User, C02 AuthSession, C03 AccountService |
| CO2 | Decks & Cards | Deck ownership, manual cards, card saving and deletion. | C04 Deck, C05 Flashcard, C06 ManualFlashcard, C08 DeckService |
| CO3 | AI Generation | PDF validation, text extraction, candidate generation, approval and retry. | C07 AIGeneratedFlashcard, C09 GenerationJob, C10 GenerationService, C11 PDFFile, C12 OpenAIClient |
| CO4 | Study & Analytics | Due cards, recall ratings, schedules, study statistics and weekly rankings. | C13 StudySession, C14 ReviewRecord, C15 CardSchedule, C16 SpacedRepetitionService, C17 AnalyticsService, C18 DashboardSummary, C19 StreakSummary, C20 LeaderboardEntry |
| CO5 | System Monitoring | Read-only performance, generation-job and API usage reporting. | C21 SystemAdministrator, C22 MonitoringReport, C23 MonitoringService |

**Class totals:** CO1 = 3; CO2 = 4; CO3 = 5; CO4 = 8; CO5 = 3. **Total = 23 unique classes.**

Classes are grouped by functionality and relationships. AIGeneratedFlashcard (CO3) specializes Flashcard (CO2); this generalization is shown in the component diagram, and approved AI cards reach CO2 only through the ICardWriting interface.

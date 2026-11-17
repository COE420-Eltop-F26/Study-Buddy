# Component Descriptions (Lab 8 – Exercise 3)

The architecture has five components in the service (business logic) layer. Interfaces are shown graphically in `Component_Diagram/Software_Architecture_Component_Diagram.pdf`.

| ID | Component / owner | Responsibilities | Supported functionality | Provided interfaces | Required interfaces |
|---|---|---|---|---|---|
| CO1 | Accounts & Sessions / Samer Salem | Registration, login, profile, session and account deletion. | UC-01 Register Account, UC-02 Log In, UC-03 Log Out, UC-04 Update Profile, UC-05 Delete Account (FR-01–FR-05) | IAccountAccess, ISessionValidation, IUserMetadata, ISessionMetrics | IDeckCleanup (CO2), IStudyCleanup (CO4) |
| CO2 | Decks & Cards / Tarik Mamlouk | Deck ownership, manual cards, card saving and deletion. | UC-06 Create Deck, UC-07 Add Flashcard Manually, UC-08 Edit Deck, UC-09 Delete Deck, UC-10 View Deck List (FR-06–FR-10) | IDeckManagement, IDeckCleanup, ICardWriting, IDeckReading | ISessionValidation (CO1) |
| CO3 | AI Generation / Hanin Hamida | PDF validation, text extraction, candidate generation, approval and retry. | UC-11 Upload PDF, UC-12 Extract PDF Text, UC-13 Generate Flashcards via AI, UC-14 Review AI-Generated Flashcards, UC-15 Retry Failed Generation (FR-11–FR-15) | IAIGeneration, IGenerationMetrics | ICardWriting (CO2); external OpenAI API |
| CO4 | Study & Analytics / Karam Sawas | Due cards, recall ratings, schedules, study statistics and weekly rankings. | UC-16 Start Study Session, UC-17 Rate Card Recall, UC-18 View Study Streak, UC-19 View Dashboard, UC-20 View Leaderboard (FR-16–FR-20) | IStudyAnalytics, IStudyCleanup | IDeckReading (CO2), IUserMetadata (CO1) |
| CO5 | System Monitoring / Team | Read-only performance, generation-job and API usage reporting. | UC-21 Monitor System Performance, UC-22 Monitor OpenAI API Usage and Costs (Lab 4 process 6.0) | IMonitoring | ISessionMetrics (CO1), IGenerationMetrics (CO3) |

## Interface operations

| Interface | Provider → Required by | Operations (name, typed parameters, return type) | Source class |
|---|---|---|---|
| IAccountAccess | CO1 → Web Client | `register(name: String, email: String, password: String): User`; `logIn(email: String, password: String): AuthSession`; `logOut(sessionId: String): void`; `updateProfile(userId: String, name: String, password: String): void`; `deleteAccount(userId: String): void` | AccountService |
| IDeckManagement | CO2 → Web Client | `createDeck(ownerId: String, title: String, description: String): Deck`; `listDecks(ownerId: String): List<Deck>`; `deleteDeck(ownerId: String, deckId: String): void`; `addManualCard(ownerId: String, deckId: String, question: String, answer: String): Flashcard` | DeckService |
| IAIGeneration | CO3 → Web Client | `uploadPDF(ownerId: String, file: PDFFile): GenerationJob`; `generateCards(jobId: String): List<AIGeneratedFlashcard>`; `approveCard(jobId: String, cardId: String, deckId: String): void`; `retryGeneration(jobId: String): void` | GenerationService |
| IStudyAnalytics | CO4 → Web Client | `startSession(userId: String, deckId: String): StudySession`; `getDueCards(userId: String, deckId: String): List<Flashcard>`; `rateCard(userId: String, cardId: String, rating: RecallRating): ReviewRecord`; `getDashboard(userId: String, from: Date, to: Date): DashboardSummary`; `getStreak(userId: String): StreakSummary`; `getWeeklyLeaderboard(): List<LeaderboardEntry>` | SpacedRepetitionService, AnalyticsService |
| IMonitoring | CO5 → Web Client (administrator) | `getPerformanceMetrics(): MonitoringReport`; `getAPIUsageAndCost(): MonitoringReport` | MonitoringService |
| ISessionValidation | CO1 → CO2 | `isValid(now: DateTime): Boolean`; `verifyOwnership(ownerId: String): Boolean` | AuthSession, User (Lab 6 update) |
| IDeckCleanup | CO2 → CO1 | `deleteOwnedContent(userId: String): void` | DeckService (Lab 6 update) |
| IStudyCleanup | CO4 → CO1 | `deleteStudyData(userId: String): void` | SpacedRepetitionService (Lab 6 update) |
| ICardWriting | CO2 → CO3 | `addCard(card: Flashcard): void` | Deck |
| IDeckReading | CO2 → CO4 | `listDecks(ownerId: String): List<Deck>`; `getCards(): List<Flashcard>` * | DeckService, Deck |
| IUserMetadata | CO1 → CO4 | `getUser(userId: String): User` * | AccountService |
| ISessionMetrics | CO1 → CO5 | `getActiveSessions(): List<AuthSession>` * | AccountService |
| IGenerationMetrics | CO3 → CO5 | `getJobs(from: DateTime, to: DateTime): List<GenerationJob>` * | GenerationService |

\* Operation added to the class model in Lab 8; see `Project/Behavioral_Modeling/Class_Model_Updates.md`.

## External services and data stores

- **OpenAI API** (external service): used by CO3 through `OpenAIClient.requestFlashcards(text: String)` over HTTPS.
- **MySQL database** (data access layer, DAO / JDBC): D1 Users & Sessions (CO1), D2 Decks & Cards (CO2), D3 Study Records & Schedules (CO4), D4 Generation Jobs (CO3). These are data stores, not architectural components.

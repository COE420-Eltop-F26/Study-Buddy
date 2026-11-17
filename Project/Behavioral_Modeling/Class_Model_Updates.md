# Class Model Updates from Lab 6

The Lab 6 sequence diagrams call the following operations that are not listed in the Lab 5 class diagram. They are added to the class model so the diagrams and the class model stay consistent.

| Class | Added operation | Used in |
|---|---|---|
| User | `verifyAccountOwner(userId): Boolean` | UC-05 Delete Account |
| User | `deleteUserRecord(userId): void` | UC-05 Delete Account |
| User | `verifyOwnership(ownerId): Boolean` | UC-06 Create Deck |
| DeckService | `deleteOwnedContent(userId): void` | UC-05 Delete Account |
| SpacedRepetitionService | `deleteStudyData(userId): void` | UC-05 Delete Account |

## Signature alignment

| Class | Lab 5 signature | Shown in Lab 6 diagram | Used in |
|---|---|---|---|
| GenerationJob | `markCompleted()` | `markCompleted(status)` | UC-13 |
| GenerationJob | `markFailed(message)` | `markFailed(error)` | UC-13 |

Object creation shown in the diagrams (new Deck, generation job, study session, review record) uses the class constructors and does not add operations.

## Lab 8 additions (component interfaces)

The Lab 8 component interfaces use four operations that are not in the Lab 5 class diagram. They are added to the providing classes so that the class model, the interfaces and the component diagram (`Project/Software_Architecture/Component_Diagram/`) stay consistent.

| Class | Added operation | Interface | Reason |
|---|---|---|---|
| Deck | `getCards(): List<Flashcard>` | IDeckReading (CO2 → CO4) | CO4 needs the cards of an owned deck to select due cards (UC-16, UC-17; FR-16). |
| AccountService | `getUser(userId: String): User` | IUserMetadata (CO1 → CO4) | CO4 needs user display data for streaks, dashboard and leaderboard (UC-18–UC-20; FR-18–FR-20). |
| AccountService | `getActiveSessions(): List<AuthSession>` | ISessionMetrics (CO1 → CO5) | CO5 reports active-session activity as part of system performance (UC-21). |
| GenerationService | `getJobs(from: DateTime, to: DateTime): List<GenerationJob>` | IGenerationMetrics (CO3 → CO5) | CO5 reads generation jobs and token usage for the API usage and cost report (UC-22). |

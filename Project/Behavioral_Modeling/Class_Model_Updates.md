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

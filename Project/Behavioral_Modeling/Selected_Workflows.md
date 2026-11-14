# Selected Workflows (Lab 7)

The Activity Diagrams model the same five use cases selected and modeled with Sequence Diagrams in Lab 6 (see `Selected_Use_Cases.md` and `Sequence_Diagrams/`). No new use cases were selected.

| Use Case | Workflow / Actor | Contributor Area | Relevant requirements | Outcomes modeled | Activity Diagram |
|---|---|---|---|---|---|
| UC-05 | Delete Account / Student | Samer Salem | FR-05; NFR-04 | Ownership check, cancellation, cleanup failure/rollback, successful deletion | `Activity_Diagrams/AD_UC05_Delete_Account.pdf` |
| UC-06 | Create Deck / Student | Tarik Mamlouk | FR-06 | Invalid session, invalid title, successful deck creation | `Activity_Diagrams/AD_UC06_Create_Deck.pdf` |
| UC-13 | Generate Flashcards via AI / Student | Hanin Hamida | FR-11–FR-13, FR-15; NFR-13–NFR-14 | Invalid PDF, unreadable text, AI success/error, retry; candidates not saved | `Activity_Diagrams/AD_UC13_Generate_Flashcards_via_AI.pdf` |
| UC-14 | Review AI-Generated Flashcards / Student | Hanin Hamida | FR-14 | Edit, approve, discard, loop over candidates; discard never persisted in deck | `Activity_Diagrams/AD_UC14_Review_AI_Generated_Flashcards.pdf` |
| UC-17 | Rate Card Recall / Student | Karam Sawas | FR-16–FR-17; NFR-18 | No due cards, valid/invalid rating, schedule update, record review, continue | `Activity_Diagrams/AD_UC17_Rate_Card_Recall.pdf` |

## Diagram files

Diagrams were created with PlantUML. Each diagram has an editable source (`.puml`) and a readable PDF export in `Activity_Diagrams/`.

## Consistency

The review and validation answers, the consistency table and the written consistency confirmation are in `Documents/Lab7_Report_StudyBuddy_Final.docx`.

# Selected Use Cases (Lab 6)

Five major use cases were selected from the approved Lab 3 use cases (`Project/Requirements/Use_Cases.md`). Together they cover all four team feature areas and are supported by the Lab 5 classes (`Project/Object_Modeling/`).

| Use Case ID | Use Case Name | Primary Actor | Purpose | Reason for Selection |
|---|---|---|---|---|
| UC-05 | Delete Account | Student | Permanently delete user data | Addresses corrected Lab 4 deletion flow and transactional cleanup. |
| UC-06 | Create Deck | Student | Create an owned flashcard deck | Covers authentication, deck ownership, and a core CRUD operation. |
| UC-13 | Generate Flashcards via AI | Student | Generate candidate Q/A from a PDF | Covers PDF validation, external API, success/failure and generation jobs. |
| UC-14 | Review AI-Generated Flashcards | Student | Edit, approve or discard candidates | Demonstrates iterative conditional approval; only approved cards are saved. |
| UC-17 | Rate Card Recall | Student | Rate studied flashcards and reschedule them | Covers historical reviews, due schedule, and four recall ratings. |

Selected workflows represent all four team areas. UC-13 and UC-14 are separate diagrams because generation and user approval are distinct use cases; the generation result remains a candidate until reviewed.

## Contributor areas and participants

| Use case | Contributor area | Participants | Diagram |
|---|---|---|---|
| UC-05 | Samer Salem | Student, AccountService, User, DeckService, SpacedRepetitionService, AuthSession | `Sequence_Diagrams/UC-05_Delete_Account.png` |
| UC-06 | Tarik Mamlouk | Student, AuthSession, DeckService, User, Deck | `Sequence_Diagrams/UC-06_Create_Deck.png` |
| UC-13 | Hanin Hamida | Student, GenerationService, PDFFile, GenerationJob, OpenAIClient | `Sequence_Diagrams/UC-13_Generate_Flashcards_via_AI.png` |
| UC-14 | Hanin Hamida | Student, GenerationService, GenerationJob, AIGeneratedFlashcard, Deck | `Sequence_Diagrams/UC-14_Review_AI_Generated_Flashcards.png` |
| UC-17 | Karam Sawas | Student, SpacedRepetitionService, StudySession, Flashcard, CardSchedule, ReviewRecord | `Sequence_Diagrams/UC-17_Rate_Card_Recall.png` |

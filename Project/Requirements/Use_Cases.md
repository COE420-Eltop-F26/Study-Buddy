# Use Cases (UC)

## Samer Salem (B00099718) — Authentication & Account Management

| UC ID | Use Case Name | Primary Actor | Short Description | Contributor |
|---|---|---|---|---|
| UC-01 | Register Account | Student | A new user creates an account by providing a name, email, and password. | Samer Salem |
| UC-02 | Log In | Student | A registered user authenticates with their email and password to access their account. | Samer Salem |
| UC-03 | Log Out | Student | A logged-in user ends their current session. | Samer Salem |
| UC-04 | Update Profile | Student | A logged-in user edits their name or password. | Samer Salem |
| UC-05 | Delete Account | Student | A logged-in user permanently removes their account and all associated data. | Samer Salem |

## Tarik Mamlouk (B00102420) — Deck & Card Management

| UC ID | Use Case Name | Primary Actor | Short Description | Contributor |
|---|---|---|---|---|
| UC-06 | Create Deck | Student | A user creates a new, empty deck with a title and description. | Tarik Mamlouk |
| UC-07 | Add Flashcard Manually | Student | A user manually adds a question/answer flashcard to one of their decks. | Tarik Mamlouk |
| UC-08 | Edit Deck | Student | A user updates a deck's title, description, or the cards it contains. | Tarik Mamlouk |
| UC-09 | Delete Deck | Student | A user removes a deck and all cards it contains. | Tarik Mamlouk |
| UC-10 | View Deck List | Student | A user views a list of all decks they own. | Tarik Mamlouk |

## Hanin Hamida (G00101852) — AI Flashcard Generation

| UC ID | Use Case Name | Primary Actor | Short Description | Contributor |
|---|---|---|---|---|
| UC-11 | Upload PDF | Student | A user uploads a PDF file to be used as source material for AI flashcard generation. | Hanin Hamida |
| UC-12 | Extract PDF Text | Student | The system extracts readable text content from the uploaded PDF for processing. | Hanin Hamida |
| UC-13 | Generate Flashcards via AI | Student | The system sends extracted text to the OpenAI API, which returns a set of candidate flashcards. Secondary actor: OpenAI API. | Hanin Hamida |
| UC-14 | Review AI-Generated Flashcards | Student | A user reviews, edits, or discards AI-suggested flashcards before saving them to a deck. | Hanin Hamida |
| UC-15 | Retry Failed Generation | Student | A user retries flashcard generation after a failed attempt (e.g., API error). | Hanin Hamida |

## Karam Sawas (B00100437) — Study & Analytics

| UC ID | Use Case Name | Primary Actor | Short Description | Contributor |
|---|---|---|---|---|
| UC-16 | Start Study Session | Student | A user begins reviewing cards that are due in a chosen deck. | Karam Sawas |
| UC-17 | Rate Card Recall | Student | A user rates how well they recalled a card, updating its spaced repetition schedule. | Karam Sawas |
| UC-18 | View Study Streak | Student | A user views their current and longest consecutive-day study streak. | Karam Sawas |
| UC-19 | View Dashboard | Student | A user views a summary of their study statistics and progress. | Karam Sawas |
| UC-20 | View Leaderboard | Student | A user views a ranked list of users by weekly study activity. | Karam Sawas |

## Team Consolidated Use Cases

All 20 individually contributed Use Cases were reviewed by the team and confirmed to represent distinct, meaningful interactions with the system, with no artificial or duplicate entries. Each Use Case falls within one of the four feature areas established in the Functional Requirements (authentication, deck/card management, AI generation, and study/analytics), keeping the consolidated set organized and consistent with the FRs. No Use Cases were merged or removed during consolidation. The final consolidated list consists of UC-01 through UC-20 as listed above.

## Use Case Relationships

| Relationship ID | Base Use Case | Related Use Case | Relationship | Justification |
|---|---|---|---|---|
| R-01 | UC-16 Start Study Session | UC-02 Log In | `<<include>>` | A user must always be authenticated before a study session can begin; login is a mandatory part of the flow. |
| R-02 | UC-06 Create Deck | UC-02 Log In | `<<include>>` | Deck creation always requires an authenticated session so the new deck can be associated with an owner. |
| R-03 | UC-07 Add Flashcard Manually | UC-02 Log In | `<<include>>` | Adding a card always requires an authenticated session to associate ownership. |
| R-04 | UC-13 Generate Flashcards via AI | UC-12 Extract PDF Text | `<<include>>` | AI generation always requires extracted text as input and cannot run without it. |
| R-05 | UC-14 Review AI-Generated Flashcards | UC-13 Generate Flashcards via AI | `<<include>>` | Review always follows a successful generation; it cannot occur without generated candidates to review. |
| R-06 | UC-11 Upload PDF | UC-15 Retry Failed Generation | `<<extend>>` | Retrying is optional and only occurs conditionally, when the initial generation attempt fails. |
| R-07 | UC-17 Rate Card Recall | UC-18 View Study Streak | `<<extend>>` | An updated streak notification is only shown conditionally (e.g., when a streak milestone is reached), not on every card rating. |
| R-08 | UC-19 View Dashboard | UC-20 View Leaderboard | `<<extend>>` | Viewing the leaderboard is an optional action a user may take from the dashboard, not a mandatory part of viewing it. |

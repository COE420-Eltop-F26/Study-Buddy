# Functional Requirements (FR)

## Samer Salem (B00099718) — Authentication & Account Management

| FR ID | Functional Requirement | Source Scenario/Stakeholder | Contributor |
|---|---|---|---|
| FR-01 | The system shall allow a new user to register an account using a full name, email address, and password. | S-01; Students (end users) | Samer Salem |
| FR-02 | The system shall allow a registered user to log in using their email and password, creating an authenticated session. | S-01, S-03; Students | Samer Salem |
| FR-03 | The system shall allow a logged-in user to log out, terminating their active session. | Students | Samer Salem |
| FR-04 | The system shall allow a logged-in user to update their profile information, including their name and password. | S-05; Students | Samer Salem |
| FR-05 | The system shall allow a logged-in user to permanently delete their account and all associated decks, cards, and study data. | Students | Samer Salem |

## Tarik Mamlouk (B00102420) — Deck & Card Management

| FR ID | Functional Requirement | Source Scenario/Stakeholder | Contributor |
|---|---|---|---|
| FR-06 | The system shall allow a logged-in user to create a new deck by specifying a deck title and optional description. | S-01; Students | Tarik Mamlouk |
| FR-07 | The system shall allow a user to manually add a flashcard to a deck by entering a question and an answer. | S-01; Students | Tarik Mamlouk |
| FR-08 | The system shall allow a user to edit the title, description, or cards of an existing deck they own. | S-05; Students | Tarik Mamlouk |
| FR-09 | The system shall allow a user to delete a deck they own, along with all cards it contains, after confirming the action. | S-05; Students | Tarik Mamlouk |
| FR-10 | The system shall allow a user to view a list of all decks they own, sorted by most recently studied. | S-05; Students | Tarik Mamlouk |

## Hanin Hamida (G00101852) — AI Flashcard Generation

| FR ID | Functional Requirement | Source Scenario/Stakeholder | Contributor |
|---|---|---|---|
| FR-11 | The system shall allow a user to upload a PDF file (up to 20 MB) as source material for flashcard generation. | S-02; Students | Hanin Hamida |
| FR-12 | The system shall extract text content from an uploaded PDF using Apache PDFBox before sending it for AI processing. | S-02; Students | Hanin Hamida |
| FR-13 | The system shall send extracted PDF text to the OpenAI API and generate a set of question-and-answer flashcards. | S-02; Students, OpenAI (API provider) | Hanin Hamida |
| FR-14 | The system shall allow a user to review, edit, or discard each AI-generated flashcard before it is saved to a deck. | S-02; Students | Hanin Hamida |
| FR-15 | The system shall notify the user if flashcard generation fails (e.g., unreadable PDF or API error) and allow the user to retry. | S-02; Students | Hanin Hamida |

## Karam Sawas (B00100437) — Study & Analytics

| FR ID | Functional Requirement | Source Scenario/Stakeholder | Contributor |
|---|---|---|---|
| FR-16 | The system shall present due cards to a user during a study session according to a spaced repetition schedule. | S-03; Students | Karam Sawas |
| FR-17 | The system shall allow a user to rate their recall of each card ("Again," "Hard," "Good," "Easy") and adjust the next review date accordingly. | S-03; Students | Karam Sawas |
| FR-18 | The system shall track and display a user's current and longest study streak (consecutive days studied). | S-04; Students | Karam Sawas |
| FR-19 | The system shall display a personal dashboard showing cards studied, decks created, and overall accuracy over a selected time period. | S-04; Students | Karam Sawas |
| FR-20 | The system shall display a leaderboard ranking users by weekly study activity. | S-04; Students | Karam Sawas |

## Team Consolidated Functional Requirements

After individual submissions, the team reviewed all 20 FRs together. No duplicate or conflicting requirements were found, since each member's contribution was scoped to a distinct feature area (authentication, deck/card management, AI generation, and study/analytics) agreed on before starting. All 20 FRs were confirmed to be within the project scope defined in Lab 2 and were retained without modification, other than minor wording cleanup for consistency of style (e.g., all requirements phrased as "The system shall..."). The consolidated list therefore consists of FR-01 through FR-20 as listed above, numbered in contributor order and traceable to each team member.

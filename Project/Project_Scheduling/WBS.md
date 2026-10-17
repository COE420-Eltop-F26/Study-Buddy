# Work Breakdown Structure (WBS)

The expected time E of each task in the network schedule is the duration given here.

| ID | Task name | Description | Predecessors | Days |
|---|---|---|---|---|
| T1 | Refine StudyBuddy requirements | Consolidate the Lab 2 and Lab 3 requirements, use cases and actors into the final project baseline. | None | 2 |
| T2 | Design database and DAO layer | Design the database tables and the DAO layer for users, decks, cards, study records and generation jobs. | T1 | 3 |
| T3 | Design web UI and navigation | Design the web pages, navigation and wireframes for the student and administrator views. | T1 | 3 |
| T4 | Implement authentication and accounts | Deliver registration, login, logout, profile update and account deletion with session handling. | T2, T3 | 4 |
| T5 | Implement deck and card management | Deliver deck create/edit/delete, manual card entry and deck list views. | T4 | 5 |
| T6 | Implement PDF upload and text extraction | Deliver PDF upload, validation and text extraction. | T4 | 3 |
| T7 | Implement AI generation and review | Connect the OpenAI API, generate candidate cards, review and approve cards, and retry failed jobs. | T5, T6 | 5 |
| T8 | Implement spaced repetition | Deliver study sessions, recall ratings and next-review scheduling. | T5 | 4 |
| T9 | Implement analytics and leaderboard | Deliver streaks, the study dashboard and the leaderboard. | T8 | 4 |
| T10 | Implement admin monitoring dashboard | Deliver the system performance and OpenAI API usage and cost views for the administrator. | T6 | 2 |
| T11 | Integrate, test, and prepare demo | Integrate all modules, run end-to-end tests and prepare the final demonstration and documentation. | T7, T9, T10 | 4 |

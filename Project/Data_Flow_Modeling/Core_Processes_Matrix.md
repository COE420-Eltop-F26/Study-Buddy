# Core Processes Matrix

The six processes below are the same processes shown in the Level-0 DFD (`Level_0_DFD/`). Inputs and outputs use the data store references D1-D4.

## Data Stores

| Store | Name | Stored data |
|---|---|---|
| D1 | Users and Sessions | Accounts, authentication and session data, display name, time zone. |
| D2 | Decks and Cards | Deck ownership, card content, deck and card totals. |
| D3 | Study Records | Review history, ratings, due dates, timestamps and study activity. |
| D4 | Generation Jobs | Extracted PDF text, generated candidates and AI generation job status. |

## Matrix

| Process number and name | Input data | Output data | Rules |
|---|---|---|---|
| 1.0 Manage Accounts | Account details; registration, login, logout, profile update and account deletion requests; user and session records from D1. | Account and session results; new and updated account and session records to D1. | Validate the full name, email and password on registration; store passwords as salted hashes; authenticate credentials; create and end sessions; only the account owner can update the profile or delete the account, and deleting an account removes its decks, cards and study data. |
| 2.0 Manage Decks and Cards | Deck and card data and requests; deck and card records from D2. | Decks, cards and operation results; deck and card updates to D2; deletion updates to D3. | Require a valid session; enforce ownership; validate deck and card fields; create, view, edit and delete only the user's own content; deletion updates related study records. |
| 3.0 Generate and Review AI Cards | PDF and generation decisions (review, edit, discard, approve, retry); generated Q and A data or API error from the OpenAI API; generation job records from D4. | Candidates and generation status; extracted text and generation prompt to the OpenAI API; extracted text and job status to D4; approved cards to D2. | Accept only PDF files up to 20 MB; extract text with Apache PDFBox; send the extracted text to OpenAI; on failure show an error and keep the job data so the user can retry; save only the cards the user has reviewed and approved. |
| 4.0 Run Spaced Repetition | Study requests and recall ratings; owned cards from D2; review history from D3. | Due cards and review results; review ratings and schedules to D3. | Show only the user's own cards that are due; accept Again, Hard, Good and Easy ratings; recalculate the next review date after every rating; record each review. |
| 5.0 Produce Study Analytics | Analytics requests; display name and time zone from D1; deck and card totals from D2; review records from D3. | Dashboard, streaks and leaderboard. | Aggregate the user's study history and totals; calculate accuracy and streaks in the user's time zone; rank weekly activity for the leaderboard; return display data only. |
| 6.0 Monitor System and API Usage | System and API monitoring request; session and response-time data from D1; API usage and job status data from D4. | Performance and API usage report. | Read-only access to D1 and D4 metadata; never modify user, deck, card or study data; summarize response-time and job-status metrics and OpenAI usage and cost for the System Administrator. |

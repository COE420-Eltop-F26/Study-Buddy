# Non-Functional Requirements (NFR)

## Samer Salem (B00099718) — Authentication & Account Management

| NFR ID | Category | Non-Functional Requirement | Contributor |
|---|---|---|---|
| NFR-01 | Security | The system shall store user passwords using a salted hashing algorithm (e.g., bcrypt) and shall never store passwords in plaintext. | Samer Salem |
| NFR-02 | Security | The system shall invalidate a user's session after 30 minutes of inactivity. | Samer Salem |
| NFR-03 | Usability | The registration and login forms shall display a clear, specific error message (e.g., "Email already registered") within 1 second of an invalid submission. | Samer Salem |
| NFR-04 | Reliability | The account deletion process shall be atomic — either all of a user's data is removed, or none of it is, even if the process is interrupted. | Samer Salem |
| NFR-05 | Portability | The authentication pages shall render correctly on the latest versions of Chrome, Safari, and Firefox. | Samer Salem |

## Tarik Mamlouk (B00102420) — Deck & Card Management

| NFR ID | Category | Non-Functional Requirement | Contributor |
|---|---|---|---|
| NFR-06 | Performance | A user's deck list shall load in under 500ms for a user with up to 100 decks. | Tarik Mamlouk |
| NFR-07 | Usability | Creating a new manual flashcard shall require no more than 3 user interactions (clicks/taps) from the deck page. | Tarik Mamlouk |
| NFR-08 | Reliability | Deck and card edits shall be saved to the database within 1 second of submission, with a visible confirmation shown to the user. | Tarik Mamlouk |
| NFR-09 | Maintainability | The deck/card CRUD codebase shall follow a layered architecture (servlet, service, DAO) so future features can be added without modifying existing CRUD logic. | Tarik Mamlouk |
| NFR-10 | Robustness | The system shall reject deck deletion requests from users who do not own the deck, returning an appropriate error rather than failing silently. | Tarik Mamlouk |

## Hanin Hamida (G00101852) — AI Flashcard Generation

| NFR ID | Category | Non-Functional Requirement | Contributor |
|---|---|---|---|
| NFR-11 | Performance | AI flashcard generation for a 10-page PDF shall complete within 15 seconds under normal API response times. | Hanin Hamida |
| NFR-12 | Scalability | The PDF upload and generation feature shall support at least 20 concurrent generation requests without degraded response time. | Hanin Hamida |
| NFR-13 | Security | Uploaded PDF files shall be validated for file type and size before processing, rejecting non-PDF files and files over 20 MB. | Hanin Hamida |
| NFR-14 | Reliability | If the OpenAI API is unavailable, the system shall display a clear error message rather than an unhandled exception, and shall preserve the uploaded PDF for retry. | Hanin Hamida |
| NFR-15 | Usability | The AI-generated flashcard review screen shall clearly visually distinguish AI-generated cards from manually created ones. | Hanin Hamida |

## Karam Sawas (B00100437) — Study & Analytics

| NFR ID | Category | Non-Functional Requirement | Contributor |
|---|---|---|---|
| NFR-16 | Performance | The dashboard shall load a user's study statistics in under 500ms for a user with up to 10,000 study records. | Karam Sawas |
| NFR-17 | Scalability | The leaderboard shall support ranking at least 5,000 active users without noticeable delay. | Karam Sawas |
| NFR-18 | Reliability | The spaced repetition scheduling algorithm shall correctly calculate the next review date for 100% of submitted card ratings, with no lost or skipped cards. | Karam Sawas |
| NFR-19 | Usability | Study session feedback buttons ("Again," "Hard," "Good," "Easy") shall be large enough for accurate use on mobile screen widths as small as 375px. | Karam Sawas |
| NFR-20 | Robustness | The streak calculation shall correctly handle time zone differences so a user's "day" is calculated consistently regardless of server location. | Karam Sawas |

## Team Consolidated Non-Functional Requirements

The team reviewed all 20 NFRs together and found them to address distinct quality attributes (security, performance, usability, reliability, scalability, maintainability, portability, and robustness) without overlap, since each member focused on the feature area they also covered in the Functional Requirements. All NFRs were confirmed to be realistic and measurable/verifiable, and no conflicts were identified. The consolidated list consists of NFR-01 through NFR-20 as listed above, numbered in contributor order and traceable to each team member.

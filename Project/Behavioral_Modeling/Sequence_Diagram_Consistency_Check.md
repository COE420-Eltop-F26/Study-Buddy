# Sequence Diagram Consistency Check (Lab 6)

| Diagram | Lab 3 traceability | Lab 5 classes | Lab 4 process / store check |
|---|---|---|---|
| UC-05 | FR-05, NFR-04; UC-05 | AccountService, User, AuthSession, DeckService, SpacedRepetitionService | Corrected Lab 4: deletion affects D1, D2 and D3; atomic cleanup |
| UC-06 | FR-06; UC-06 | AuthSession, DeckService, User, Deck | Lab 4 process 2.0, store D2; owner/session requirements |
| UC-13 | FR-11–FR-13, FR-15; UC-13 | PDFFile, GenerationService, GenerationJob, OpenAIClient | Lab 4 process 3.0, store D4 and external OpenAI API |
| UC-14 | FR-14; UC-14 | GenerationService, GenerationJob, AIGeneratedFlashcard, Deck | Lab 4 process 3.0, approved cards to D2 only |
| UC-17 | FR-16–FR-17; UC-17 | SpacedRepetitionService, StudySession, Flashcard, CardSchedule, ReviewRecord | Lab 4 process 4.0, stores D2 and D3 |

## Verification findings and class model reconciliation

- Every diagram uses a selected approved use case and the Student actor. The OpenAI API is represented by the existing OpenAIClient class, not by a new internal actor.
- Methods already present in Lab 5 are reused verbatim where possible: deleteAccount, createDeck, uploadPDF, extractText, generateCards, requestFlashcards, approveCard, approve, discard, addCard, startSession, getDueCards, rateCard, updateAfterRating, isValid and invalidate.
- Some design-level calls are not explicitly specified as operations in Lab 5. They are listed in `Class_Model_Updates.md` as additions to the class model.
- Account deletion is coordinated as one transaction across D1, D2 and D3. The account owner must be authenticated and authorized; rollback is required by NFR-04.
- No additional persistent data stores beyond D1–D4 are assumed.
- The sequence diagrams are design models; they do not establish that the application or database transactions have been implemented or tested.

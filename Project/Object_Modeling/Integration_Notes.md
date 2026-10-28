# Integration Notes

Significant decisions made when consolidating the four individual class models.

| Integration issue | Consolidation decision / rationale |
|---|---|
| Duplicate shared classes | Merge User, Deck and Flashcard into one common definition; keep references from each team area. |
| Card specialization | ManualFlashcard and AIGeneratedFlashcard inherit from Flashcard. AI candidates are saved into decks only after approval. |
| Review history vs current schedule | ReviewRecord records each rating, while CardSchedule records the current next-due state; both correspond to D3. |
| System monitoring | SystemAdministrator and MonitoringService request read-only MonitoringReport data consistent with process 6.0. |
| Persistence boundary | No additional persistent DFD stores are invented beyond D1–D4. Domain services and summary objects need not be persistent entities. |
| Composition and deletion | Deck/Flashcard and StudySession/ReviewRecord are modeled as lifecycle dependencies; actual cascades must satisfy account/deck deletion requirements. |
| Enumerated types | RecallRating has the values Again, Hard, Good and Easy (FR-17). GenerationStatus has the values pending, completed and failed (FR-15 failure and retry). |

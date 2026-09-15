# Software Process Model

## Selected Model: Incremental Model

## Justification

StudyBuddy has a moderately well-defined core feature set (authentication, deck/card CRUD, spaced repetition, analytics), but parts of it — especially the OpenAI API integration and PDF text extraction with Apache PDFBox — use technologies the team hasn't worked with before, so requirements there may evolve as we learn more.

The Incremental Model fits well because:

- It lets us deliver the system as a series of working increments (core auth/CRUD first, then AI flashcard generation, then analytics/dashboards), each a usable subset of the final product.
- Familiar, low-risk features can be built first, while riskier components (OpenAI API, PDF parsing) are isolated into later increments, giving time to prototype without blocking the rest of the system.
- Each increment can be tested and demoed independently, which fits the lab's weekly progress structure.
- Unlike Waterfall, it tolerates the fact that AI-generated content quality may need refinement after initial testing.

## Overheads/Drawbacks and Management Strategy

- **Integration overhead** — new increments must be regression-tested against earlier ones. Managed via GitHub branches per feature, merged into `main` only after basic testing.
- **Upfront architecture cost** — the database schema and servlet structure need reasonable planning up front. Managed by finalizing the core schema before starting increments.
- **Documentation overhead** — each increment ideally needs short notes. Managed by keeping lightweight markdown notes rather than heavyweight docs.
- **Scope creep between increments** — new feature ideas can creep in mid-increment. Managed by freezing scope per increment and deferring new ideas to the Out-of-Scope list or a future increment.

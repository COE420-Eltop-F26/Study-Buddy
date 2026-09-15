# Project Risk Register

| Risk ID | Risk Description | Possible Cause | Probability | Impact | Mitigation/Response Strategy |
|---|---|---|---|---|---|
| R1 | OpenAI API may fail due to downtime, rate limits, or unexpected cost | Reliance on a third-party external service | Medium | High | Error handling/retry logic, usage alerts, caching, manual fallback creation |
| R2 | AI-generated flashcards may be inaccurate or poorly formatted | PDFBox extraction limits, AI output variability | Medium | Medium | Allow manual review/editing of cards, test varied PDFs early, refine prompts |
| R3 | Team members may have limited availability | Overlapping coursework/exams | Medium | Medium | GitHub Issues for task tracking, weekly check-ins, schedule buffer |
| R4 | Database concurrency/data inconsistency under simultaneous use | Lack of proper transaction handling | Low | High | Use DB transactions and locking; test under simulated concurrent load |
| R5 | Security/privacy issues with credentials or uploaded files | Improper auth/file-upload handling | Medium | High | Hash/salt passwords, secure sessions, env-var API keys, input sanitization |
| R6 | Schedule delay from unfamiliar tech (OpenAI API, PDFBox) | New technology stack components | Medium | Medium | Early technical spike/prototype, extra learning time allocated |

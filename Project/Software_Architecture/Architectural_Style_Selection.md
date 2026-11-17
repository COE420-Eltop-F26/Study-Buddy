# Architectural Style Selection (Lab 8 – Exercise 2)

## Selected architectural style

**Modular layered Java web architecture** (servlet/presentation → service → DAO/data access), with the service layer separated into five functional components (CO1–CO5).

## Main characteristics

- Three layers with one-way dependencies: the presentation layer (Java Servlets / JSP) calls only service-layer interfaces, and the service layer calls only the data access layer (DAO / JDBC) and the external OpenAI API.
- The service layer is divided into five functional components (CO1–CO5). Each component owns its classes, offers provided interfaces, and uses other components only through required interfaces.
- Persistent data (D1–D4 in the MySQL database) is read and written only through the data access layer.

## Why it is appropriate for StudyBuddy

The system has clearly separated account, deck, AI generation, study and monitoring responsibilities, and NFR-09 explicitly calls for a servlet/service/DAO design. The planned implementation technologies (Java Servlets, JSP, JDBC and MySQL) map directly onto these three layers, and the modular boundaries support maintainability, security and testing.

## How the style supports the design goals

| Goal | How the selected style supports it |
|---|---|
| G01 Maintainability | Layers and component interfaces isolate change: a feature is changed inside one component without modifying the others, as NFR-09 requires. |
| G02 Security | Every request passes through the service layer, where CO1 validates sessions and ownership (ISessionValidation) before any data access; CO1 coordinates account deletion as one transaction across D1–D3 (NFR-04). |
| G03 Reliability | Generation jobs are stored in D4 and handled only by CO3, so a failed OpenAI call keeps the job and PDF for retry (NFR-14); CO4 records every rating and next due date through the data access layer (NFR-18). |
| G04 Performance | Deck-list and dashboard queries are optimized in the data access layer without changing the UI or services (NFR-06, NFR-16); slow AI calls are confined to CO3 and do not block other components (NFR-11). |
| G05 Scalability | The resource-intensive components (CO3 AI generation, CO4 leaderboard) sit behind interfaces, so they can be scaled or optimized independently (NFR-12, NFR-17). |

## Advantages and potential limitations

| Advantages | Potential limitations / mitigation |
|---|---|
| Clear ownership and testable class groups | More interface coordination; keep contracts short and verify integration. |
| Protects ownership and business rules | Account deletion spans D1–D3; execute all deletion operations inside one transaction with rollback on failure. |
| Isolates AI and monitoring behavior | External API may fail or slow down; preserve retryable jobs and return clear errors. |

# Architectural Design Goals (Lab 8 – Exercise 1)

The design goals were defined before the architectural style was selected. Related requirements refer to the Lab 3 non-functional requirements (`Project/Requirements/Non_Functional_Requirements.md`).

| Goal ID | Design Goal | Description | Related Requirement | Priority | Justification |
|---|---|---|---|---|---|
| G01 | Maintainability | Keep account, deck, generation, study and monitoring logic separate, with clear service interfaces. | NFR-09 | High | Separating responsibilities makes feature changes easier and reduces accidental changes to other modules. |
| G02 | Security | Protect credentials and sessions; validate ownership; delete all user data atomically. | NFR-01, NFR-02, NFR-04, NFR-10 | High | The app holds personal accounts and study history, so unauthorized access and partial deletion must be prevented. |
| G03 | Reliability | Keep failed generation jobs retryable and reliably record each review and next due date. | NFR-14, NFR-18 | High | Failed API calls or ratings must not lose student progress. |
| G04 | Performance | Keep deck lists and dashboards responsive and provide fast normal-case PDF generation. | NFR-06, NFR-11, NFR-16 | High | Students use StudyBuddy frequently, including shortly before exams. |
| G05 | Scalability | Support concurrent generation requests and a growing leaderboard through well-defined modules. | NFR-12, NFR-17 | Medium | AI generation and ranking are more resource-intensive and must be isolated from basic account actions. |

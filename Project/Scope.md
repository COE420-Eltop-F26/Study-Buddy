# Project Scope

## 1. Project Objective

StudyBuddy is a full-stack, AI-assisted flashcard web application that helps students prepare for exams using active recall and spaced repetition. It addresses the problem that manually creating flashcards from lecture notes and PDFs is time-consuming and discourages consistent study habits, by automating flashcard creation from uploaded PDFs using AI and providing structured study tools to encourage regular studying.

## 2. Target Users

- University/college students preparing for exams who want an efficient way to turn study material into flashcards.
- Students who use active-recall methods and want a tool to track their progress and consistency.
- Learners studying independently from PDF-based material.

## 3. In-Scope Features

- User registration and session-based authentication.
- Full CRUD for users, decks, and cards.
- Manual flashcard/deck creation and editing.
- AI-assisted flashcard generation from uploaded PDFs (Apache PDFBox for text extraction, OpenAI API for card generation).
- Spaced repetition scheduling.
- Study analytics: progress tracking, streaks, personal dashboards.
- Leaderboards.
- MySQL database with foreign-key constraints.
- Performance target: deck loading under 500ms.

## 4. Out-of-Scope Features

- Native mobile apps.
- Real-time multiplayer study modes / live quizzes.
- Payment or subscription features.
- Offline mode.
- OCR for scanned/handwritten PDFs.
- Integration with third-party LMS platforms.
- Public deck-sharing marketplace.

## 5. Major Deliverables

- Functional web application (Java Servlets, JDBC, MySQL, JSP, HTML/CSS/JS, Bootstrap).
- Relational database schema with documented relationships.
- AI flashcard generation module.
- Study analytics module (spaced repetition, streaks, dashboards, leaderboards).
- Planning and design documentation.
- Working prototype/demo.
- Basic user manual / README.

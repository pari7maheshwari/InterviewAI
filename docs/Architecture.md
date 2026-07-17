# High-Level Architecture

InterviewAI follows a client-server architecture.

Frontend (React):
- Displays the UI.
- Collects user input.
- Sends requests to the backend.
- Never communicates directly with an LLM.

Backend (FastAPI):
- Handles authentication.
- Stores and retrieves user data.
- Coordinates interview generation.
- Applies business rules.
- Communicates with AI providers.

Database (PostgreSQL):
- Stores users, profiles, interview history, feedback, and progress.

AI Service:
- Generates interview questions.
- Creates follow-up questions.
- Evaluates answers.
- Produces structured feedback.

## Backend Architecture

InterviewAI Version 1 will use a **modular monolith** architecture.

The backend will be a single FastAPI application divided into feature-based modules such as:

- Authentication
- Profiles
- Interviews
- Feedback
- Roadmap
- AI

This approach keeps development, testing, and deployment simple while maintaining clear separation of responsibilities.

If InterviewAI grows significantly in users or engineering team size, individual modules can later be extracted into independent microservices without requiring a complete rewrite.

## AI Context Retrieval (Version 1)

InterviewAI Version 1 will use structured context retrieval instead of a full Retrieval-Augmented Generation (RAG) pipeline.

Before calling the LLM, the backend will retrieve only the information relevant to the current interview, including:

- Candidate profile
- Resume summary
- Target role
- Target company
- Previous interview history
- Weak topics
- Job description (if available)

This context will be assembled into a prompt for the LLM.

A vector database and embedding-based retrieval may be introduced in a future version when InterviewAI needs to search large collections of unstructured documents.

## Interview Flow Engine (Version 1)

InterviewAI Version 1 will use an application-managed interview state machine.

The backend is responsible for controlling interview progression, including:

- Selecting the next question
- Determining whether a follow-up question is needed
- Adjusting interview difficulty
- Ending the interview
- Persisting interview state

The LLM generates content, but the backend controls the interview flow.
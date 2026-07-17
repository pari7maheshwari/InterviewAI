# Product Decisions

## Decision 001 — Support Users Without a Resume

### Decision
Users can either upload a resume or manually create an interview profile.

### Why?
Many students and early-year college learners don't yet have a professional resume.

### Trade-off
Manual profile creation increases onboarding time slightly but makes the platform accessible to more users.

---

## Decision 002 — Authentication Happens After Demonstrating Value

### Decision
Users should be able to explore InterviewAI and see a personalized preview before creating an account.

### Why?
People are more willing to sign up after understanding the value they'll receive.

### Trade-off
Some onboarding state must be temporarily stored before account creation.

---

## Decision 003 — Goal-Based Personalization

### Decision

The onboarding flow will first identify the user's goal before collecting profile details.

### Why?

A user's objective (e.g., internship, placement, job switch) has a greater impact on interview preparation than demographic information alone.

### Trade-off

The system must support multiple preparation paths, increasing personalization logic but resulting in a more relevant experience.

---

## Decision 004 — Graceful Handling of Edge Cases

### Decision

The platform should recover gracefully from incomplete profiles, invalid resumes, unrealistic goals, and missing information.

### Why?

Users should never reach a dead end during onboarding or interview preparation.

### Examples

- Invalid resume → Offer manual profile creation.
- Advanced role for beginner → Recommend a progressive roadmap.
- Skill mismatch → Ask clarifying questions before generating interviews.

---

## Decision 005 — Modular Monolith for Version 1

### Decision

Use a single FastAPI backend organized into feature-based modules instead of microservices.

### Why?

- Faster development
- Easier debugging
- Simpler deployment
- Lower operational complexity
- Ideal for a solo developer and MVP

### Future

If scaling requirements increase, modules with clear boundaries can be extracted into separate microservices.

## Decision 006 — Delay Full RAG

### Decision

Version 1 will not use a vector database or full RAG architecture.

### Why?

The MVP primarily retrieves structured data owned by the application, making traditional database queries sufficient.

### Future

Introduce embeddings and vector search when supporting large collections of interview experiences, company documents, or learning resources.

## Decision 007 — Use a State Machine Instead of LangGraph

### Decision

Version 1 will implement interview flow using a custom state machine rather than LangGraph.

### Why?

- The interview flow is relatively small and predictable.
- A custom implementation is easier to understand, debug, and maintain.
- It avoids introducing unnecessary framework complexity.

### Future

If InterviewAI evolves into a multi-agent platform with specialized AI components, LangGraph can be introduced to orchestrate those interactions.
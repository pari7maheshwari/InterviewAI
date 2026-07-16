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
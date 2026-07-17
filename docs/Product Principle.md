# Product Principles

## Principle 1 — Depth over Breadth
Build a few features exceptionally well instead of many features poorly.

---

## Principle 2 — Every Feature Must Solve a User Problem
If a feature doesn't solve a clear user problem, it doesn't belong in the MVP.

---

## Principle 3 — AI Assists, Users Decide
AI should assist users, but users should always remain in control of important decisions.

---

## Principle 4 — Show Value Before Asking for Commitment
Users should understand the value of InterviewAI before being asked to create an account.

---

## Principle 5 — Ask for Information Only When It Creates Immediate Value
Every question asked during onboarding should immediately improve the user's experience.

---

## Principle 6 — Design Around User Goals

Personalization should be driven by what the user wants to achieve rather than who they are.

The user's goal should influence every stage of the experience, including onboarding, interview generation, roadmap creation, and feedback.

---

## Principle 7 — Guide, Don't Block

When users provide incomplete, inconsistent, or unrealistic information, InterviewAI should guide them toward a better preparation path instead of preventing them from using the platform.

---

## Principle 8 — The Frontend Should Never Know the AI Provider

The frontend communicates only with the backend. The backend abstracts the AI provider, allowing the application to switch between OpenAI, Gemini, Claude, or local models without changing the frontend.

---

## Principle 9 — Optimize for Today's Complexity

Choose the simplest architecture that solves the current problem while allowing future growth. Avoid introducing unnecessary complexity before it is needed.

---

## Principle 10 — Retrieve Only Relevant Context

The AI should receive only the information needed for the current task. Smaller, focused context improves response quality, reduces token usage, and lowers inference costs.

---

## Principle 11 — Understand Before You Abstract

Build and understand the core logic before introducing frameworks that hide implementation details.
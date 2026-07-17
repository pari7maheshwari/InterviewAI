# Database Design

## Core Entities

### Users
Represents authenticated users of InterviewAI.

### Candidate Profile
Stores long-term information about the candidate, including:

- Personal details
- Skills
- Projects
- Experience
- Education

### Interview Configuration
Stores interview-specific settings, including:

- Target role
- Target company
- Difficulty level
- Job description (optional)

The Candidate Profile represents who the user is, while the Interview Configuration represents what the user is preparing for.

## Database Design Principle

When a user can have multiple instances of the same type of information (such as skills, projects, education, or interviews), that information should be stored in a separate table rather than as comma-separated values or fixed columns.

Examples:

- One user → Many skills
- One user → Many projects
- One user → Many interviews

This design keeps the database scalable, easier to query, and easier to maintain.
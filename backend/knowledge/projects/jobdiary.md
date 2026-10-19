# Job Diary — AI-Powered Job Application Tracker

## 1. Project Overview

**Job Diary** is an AI-powered job application tracking application designed to help job seekers organize their applications, maintain company and role research, prepare for interviews, and manage follow-ups.

During a job search, applicants may submit dozens of applications and find it difficult to track application status, interview opportunities, company research, and follow-up dates. Job Diary brings this information together in one place and provides AI-generated research summaries to make reviewing information more convenient.

The application combines backend API development, asynchronous Python, database persistence, AI integration, authentication, scheduled reminders, and PDF generation.

**Repository:** https://github.com/Aswin123445/job-diary

## 2. Problem Statement

Job seekers often need to manage information across multiple applications, including:

- Company details and research notes
- Job descriptions and role requirements
- Application status and submission history
- Interview preparation notes
- Follow-up dates and pending applications

Managing these details manually can make it difficult to stay organized and prepare efficiently for interviews.

Job Diary aims to centralize this information and reduce repetitive work through AI-assisted summaries and automated follow-up reminders.

## 3. Key Features

### 3.1 Job Application Management

- Create and manage job application records.
- Keep application-related information organized in one place.
- Maintain company and job-role research alongside applications.
- Track applications and identify those requiring follow-up.

### 3.2 Company and Job Research

- Store detailed research notes about companies and job roles.
- Keep relevant information available for interview preparation.
- Generate concise summaries from stored research.

### 3.3 AI-Powered Research Summaries

The application integrates the Groq API to generate professional summaries from job and company research.

The intended workflow is:

1. The user stores research notes.
2. The user requests an AI-generated summary.
3. The application sends the relevant information to the configured language model API.
4. The generated summary is returned for review.

The summaries help users review key information before interviews or follow-ups. Their accuracy depends on the quality of the supplied research and the model's output.

### 3.4 Automated Email Reminders

The application is designed to send email reminders for job applications that have been pending for more than 10 days.

This feature helps users identify applications that may require follow-up.

The scheduling mechanism, delivery guarantees, and retry behavior should be documented separately if verified in the implementation.

### 3.5 PDF Summary Export

Users can export AI-generated research summaries as formatted PDF reports, making it easier to review or retain interview preparation material.

### 3.6 Authentication

The application provides email-based registration and sign-in using Authlib.

Authentication protects access to application-related information. The exact authentication flow, session or token handling, and authorization rules should be described according to the implemented code.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| SQLModel | Database models and database interaction |
| PostgreSQL | Relational data storage |
| Async Python | Asynchronous backend operations |
| Groq API | AI-generated research summaries |
| Authlib | Authentication integration |
| PDF generation library | Exporting summaries as PDF reports |
| Email service | Application follow-up reminders |

The specific PDF generation library, email provider, and reminder scheduling technology should be confirmed from the repository before being documented as implementation details.

## 5. High-Level Architecture

The application's conceptual workflow is:

1. **Client request:** The user creates an application record or requests a research summary.
2. **FastAPI backend:** The API validates the request and runs the relevant application logic.
3. **Database layer:** SQLModel interacts with PostgreSQL to store or retrieve application and research data.
4. **AI integration:** When requested, the backend sends research content to the Groq API and processes the generated summary.
5. **PDF export:** The summary can be formatted and exported as a PDF report.
6. **Reminder workflow:** Applications meeting the pending-duration condition are identified for email reminders.

This is a high-level description of the intended workflow, not a verified diagram of every component in the repository.

## 6. Engineering Concepts Demonstrated

### Backend API Development
Using FastAPI to organize application operations behind API endpoints.

### Database Modeling
Representing job applications and associated research using SQLModel and PostgreSQL.

### Asynchronous Programming
Using Python's asynchronous capabilities where appropriate for API operations and external service integration.

### External AI API Integration
Connecting a backend application to a hosted language model API and incorporating its output into a user-facing workflow.

### Authentication
Integrating email-based authentication through Authlib.

### Automation
Identifying applications that have remained pending beyond a defined threshold and initiating reminders.

### Document Generation
Transforming generated research summaries into formatted PDF reports.

## 7. Potential Technical Challenges

The following are useful areas to document if they were encountered during development:

- Handling AI API errors, timeouts, and rate limits
- Managing asynchronous database and external API operations
- Validating and formatting AI-generated summaries
- Preventing duplicate or unnecessary reminder emails
- Managing authentication securely
- Generating readable PDF documents from dynamic content
- Handling missing, outdated, or incomplete application research
- Keeping configuration and API credentials in environment variables

These are potential engineering concerns, not claims that every issue occurred in this project.

## 8. Project Status and Evidence

Use the source code and repository history to establish which features are implemented, tested, and deployed.

For each major feature, record:

- Implementation status
- Relevant API endpoint or module
- Tests or verification evidence
- Known limitations
- Deployment status, where applicable

Avoid describing a feature as production-ready or proven to scale unless there is supporting evidence.

## 9. Related Knowledge

- `knowledge/skills/backend.md` — Python, FastAPI, API development, and backend architecture
- `knowledge/skills/database.md` — PostgreSQL and database modeling
- `knowledge/skills/devops.md` — deployment and operational concerns
- `knowledge/profile/current-focus.md` — AI application and agent engineering learning goals
- `knowledge/profile/knowledge-boundaries.md` — rules for grounding portfolio answers in verified information

## 10. Portfolio Summary

Job Diary is a job application tracking application that combines FastAPI, SQLModel, PostgreSQL, asynchronous Python, authentication, and AI-generated research summaries. It is designed to help job seekers organize application information, prepare for interviews, export summaries as PDFs, and follow up on pending applications through email reminders.
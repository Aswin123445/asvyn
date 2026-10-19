# Are We Dating? — AI-Powered Relationship Assistant

## 1. Project Overview

**Are We Dating?** is an AI-powered conversational relationship assistant designed to help users think through dating and relationship situations through natural conversation.

The application focuses on thoughtful, conversational guidance rather than predicting relationship outcomes or making definitive claims about another person's feelings.

It uses a React frontend and a FastAPI backend, with a modular service architecture for advisor logic, prompt construction, and language model integration. The backend streams generated responses to the frontend to provide a more responsive chat experience.

**Project status:** Under active development.

## 2. Problem Statement

People navigating dating and relationship situations may want a space to explain a situation, explore different perspectives, and think through possible responses.

Are We Dating? aims to provide a conversational interface that helps users reflect on these situations without presenting uncertain interpretations as facts.

The application prioritizes useful conversation, clear limitations, and a simple architecture that can evolve as requirements become clearer.

## 3. Key Features

### 3.1 Conversational Relationship Advice

Accepts relationship-related messages and generates AI-powered conversational responses.

The intended experience is reflective and supportive, helping users consider situations and perspectives rather than claiming to know another person's intentions.

### 3.2 AI-Powered Response Generation

Integrates a language model through a dedicated LLM service.

Separating model integration from the advisor's business logic makes it easier to maintain the application and adapt the integration as requirements change.

### 3.3 Streaming AI Responses

Uses FastAPI's `StreamingResponse` to progressively send generated response content to the client.

The basic flow is:

1. The frontend submits a message.
2. The advisor API receives the request.
3. The advisor service coordinates prompt preparation and LLM interaction.
4. Generated content is yielded progressively.
5. FastAPI streams the content to the frontend.
6. The frontend displays the response as it arrives.

Streaming can improve perceived responsiveness because the user does not need to wait for the entire response before seeing the first content.

### 3.4 Modular Backend Architecture

Separates responsibilities across API routers, services, schemas, prompt construction, and LLM integration.

This structure helps keep HTTP handling, application logic, and model-specific code independently maintainable.

### 3.5 React Frontend

Provides the user-facing interface for sending relationship-related messages and displaying generated responses.

The frontend consumes the backend API and supports the intended streaming interaction.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | API development |
| Uvicorn | ASGI development server |
| React | Frontend development |
| `StreamingResponse` | Progressive response delivery |
| LLM API | AI-generated conversational responses |
| Pydantic schemas | Request and response validation, where defined |

The specific LLM provider, model, and streaming protocol should be documented after verifying the implementation.

## 5. Architecture

The application follows a layered request-processing design:

```text
React Frontend
      |
      | HTTP request
      v
FastAPI Application
      |
      v
Advisor Router
      |
      v
Advisor Service
      |
      +------> Prompt Service
      |
      +------> LLM Service
                    |
                    v
              Language Model
                    |
                    v
             Generated Chunks
                    |
                    v
          FastAPI StreamingResponse
                    |
                    v
              React Frontend
```

The diagram represents the documented high-level design. The exact execution order, streaming format, and error-handling behavior should be verified against the source code.

## 6. Project Structure

The reported backend structure is:

```text
are_we_dating/
├── backend/
│   └── app/
│       ├── main.py
│       ├── routers/
│       │   └── advisor.py
│       ├── services/
│       │   ├── advisor_service.py
│       │   ├── prompt_service.py
│       │   └── llm_service.py
│       └── schemas/
│           └── advisor.py
├── frontend/
│   └── ...
├── venv/
└── README.md
```

### Backend components

- `main.py` — FastAPI application entry point and application configuration.
- `routers/advisor.py` — Defines the advisor API endpoint.
- `services/advisor_service.py` — Coordinates the advisor's application logic.
- `services/prompt_service.py` — Handles prompt construction and related prompt logic.
- `services/llm_service.py` — Encapsulates language model interaction.
- `schemas/advisor.py` — Defines the request and response data structures, as applicable.

### Frontend

The React frontend handles message submission and presentation of the streamed response. Its exact component and state-management structure can be documented after reviewing the frontend code.

## 7. API Design

### Advisor endpoint

| Property | Value |
|---|---|
| Method | `POST` |
| Path | `/api/advisor` |
| Purpose | Submit a relationship-related message and receive an AI-generated response |
| Response behavior | Streamed response |

The endpoint accepts a user's message and returns generated content progressively.

The exact request schema, content type, stream format, and error responses should be confirmed from the API implementation.

### Local development

The documented development server command is:

```bash
uvicorn app.main:app --reload
```

This command assumes the working directory and Python import path are configured so that `app.main` can be imported.

When running the backend, the local API address is:

`http://127.0.0.1:8000`

Interactive API documentation is available at:

`http://127.0.0.1:8000/docs`

## 8. Design Philosophy and Boundaries

The project intentionally begins with a simple conversational assistant rather than a complex agent architecture.

The current design does not aim to:

- Predict whether two people will become a couple.
- Predict the future of a relationship.
- Assign relationship compatibility scores.
- Make definitive claims about another person's private feelings.
- Introduce complex agent or multi-agent workflows without a demonstrated need.

These boundaries help keep the application focused on conversational assistance rather than unsupported predictions.

## 9. Engineering Concepts Demonstrated

### Layered Backend Design
Separating API routes, application services, prompt construction, and LLM integration.

### LLM Integration
Connecting a backend service to a language model and incorporating generated content into an application workflow.

### Response Streaming
Using FastAPI's `StreamingResponse` to deliver content progressively instead of returning only a completed response.

### Request Validation
Using structured schemas to define and validate incoming API data.

### Frontend–Backend Communication
Connecting a React client to a FastAPI endpoint and rendering generated output.

### Separation of Concerns
Keeping HTTP concerns, advisor logic, prompt management, and model communication in distinct modules.

### Incremental Architecture Development
Starting with a small, understandable architecture and introducing additional components when requirements justify them.

## 10. Technical Considerations and Future Improvements

The following items are potential improvements rather than confirmed implemented features.

- **Conversation history:** Preserve relevant previous messages across turns.
- **Authentication:** Introduce user accounts if personalized or persistent conversations require them.
- **Database persistence:** Store conversations and preferences where needed.
- **Prompt management:** Version prompts and test changes systematically.
- **LLM reliability:** Handle provider errors, timeouts, rate limits, and interrupted streams.
- **Streaming robustness:** Ensure disconnects and partial responses are handled correctly.
- **Observability:** Add structured logging and useful operational metrics without unnecessarily logging sensitive conversations.
- **Testing:** Cover request validation, service behavior, streaming, and failure cases.
- **Production deployment:** Configure appropriate server settings, secrets, monitoring, and request limits.
- **Responsible responses:** Avoid presenting guesses about another person's feelings as established facts.

## 11. Project Status and Evidence

The project is currently under active development, so its architecture and capabilities may change.

When documenting implementation progress, distinguish between:

- Implemented and tested features
- Implemented but not fully tested features
- Planned improvements
- Architectural ideas that have not yet been implemented

Do not claim that authentication, persistence, production deployment, or advanced agent workflows exist unless supported by the codebase.

## 12. Portfolio Summary

Are We Dating? is an AI-powered relationship assistant built with React and FastAPI. It uses a modular backend architecture to separate advisor logic, prompt construction, and LLM integration, and uses streamed responses to support a responsive conversational experience. The project emphasizes a focused initial scope, maintainable architecture, and clear boundaries around relationship predictions.
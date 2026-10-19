# Project Learning and Experiments

## Purpose

This document records the technical concepts, tools, approaches, and architectural patterns I have explored while building projects.

Each entry describes the project context, the experiment or implementation, what I learned, and any limitations or future improvements.

The goal is to maintain a record of practical learning rather than simply list technologies or reproduce theoretical explanations.

## 1. CivicEdge — Background Task Processing

**Technologies:** Django, Celery, Redis

### Context
CivicEdge includes background operations such as certificate generation and email notifications. These operations can be handled outside the main request-response cycle.

### Experiment and Implementation
Explored using Celery for background task execution and Redis as the message broker.

### Learning
- Why background jobs are useful for operations that do not need to finish before an HTTP response is returned.
- How a message broker connects the application to background workers.
- How task registration, imports, worker availability, and configuration affect task execution.
- Why retries, idempotency, and task failure handling matter.

### Further Exploration
- Task retry policies and failure handling.
- Monitoring and inspecting task execution.
- Preventing duplicate side effects.
- Measuring the effect of background processing on request latency.

## 2. CivicEdge — Event Conflict Prevention

**Technologies:** Django, database queries, date-time validation

### Context
Event participation requires checking whether a user has already joined another event scheduled during an overlapping time interval.

### Experiment and Implementation
Worked on backend validation to prevent users from registering for conflicting upcoming events.

### Learning
- How to translate a real-world scheduling rule into a backend validation condition.
- How start and end times determine interval overlap.
- Why business rules should be enforced by the backend.
- Why boundary conditions and concurrent requests require careful consideration.

### Further Exploration
- Test overlapping and non-overlapping time intervals.
- Handle cancelled events and time-zone differences.
- Evaluate concurrency safeguards where required.

## 3. JobDiary — LLM-Powered Job Application Insights

**Technologies:** FastAPI, SQLModel, PostgreSQL, Groq API

### Context
JobDiary tracks job applications and related company or job information. It also uses an LLM API to generate summaries.

### Experiment and Implementation
Explored integrating an LLM into a backend application to transform job-related information into concise summaries.

### Learning
- How an external LLM API can be integrated into an application service.
- Why request validation and response handling matter when working with external APIs.
- Why API failures, latency, and rate limits must be considered.
- Why generated summaries should be distinguished from verified source information.

### Further Exploration
- Validate structured model outputs.
- Add tests for failed or malformed LLM responses.
- Evaluate summary quality against source information.
- Measure latency and token usage.

## 4. RailConnect — External API Integration

**Technologies:** Python, Django, external API

### Context
RailConnect is a mini project designed to fetch railway PNR status through an external API.

### Experiment and Implementation
Explored connecting a Django application to an external service and presenting the returned information through a user interface.

### Learning
- How an application communicates with an external API.
- How request parameters and API responses move through a backend application.
- Why external-service failures and unexpected responses need handling.
- Why credentials and API configuration should be managed securely.

### Further Exploration
- Test timeout and connection-failure behavior.
- Validate external API response structures.
- Improve user-facing error messages.
- Add tests using mocked external responses.

## 5. Purushu — Personal Voice Assistant

**Technologies:** Python, OpenAI API, SpeechRecognition, PyAudio, pyttsx3

### Context
Purushu explores a voice-driven assistant that combines speech input, language-model responses, speech output, and desktop automation.

### Experiment and Implementation
Explored combining separate Python libraries and modules to support voice interaction, information retrieval, and selected computer-control actions.

### Learning
- How speech recognition and text-to-speech fit into an application workflow.
- How an LLM API can support conversational interaction.
- Why modular design helps separate input, reasoning, and action handling.
- Why desktop automation requires careful control over which actions may execute.

### Further Exploration
- Improve error handling for microphone and speech-recognition failures.
- Add safeguards around sensitive desktop actions.
- Separate model responses from executable commands.
- Test individual modules independently.

## 6. Are We Dating? — Streaming LLM Responses

**Technologies:** React, FastAPI, StreamingResponse, LLM integration

### Context
Are We Dating? is a conversational relationship-advice application that explores generating responses through an LLM-backed API.

### Experiment and Implementation
Explored separating API routing, advisor logic, prompt construction, and LLM communication into dedicated backend modules. The backend uses FastAPI's `StreamingResponse` for streaming responses.

### Learning
- How separation of concerns improves backend organization.
- How streaming differs from returning a completed response.
- Why prompt design influences response style and scope.
- Why the application should avoid presenting generated advice as certainty about another person's feelings or future.

### Further Exploration
- Handle interrupted streams and provider errors.
- Add conversation persistence if needed.
- Test streaming behavior and client disconnects.
- Evaluate response quality and consistency.

## 7. Portfolio AssistNet — Retrieval-Augmented Generation

**Technologies:** Python, FastAPI, embeddings, vector databases, RAG

### Context
Portfolio AssistNet is intended to answer questions about my profile, skills, projects, technical decisions, and problem-solving experiences using a structured knowledge base.

### Experiment and Implementation
Explored organizing portfolio information into Markdown documents so that relevant content can be retrieved and supplied to an LLM when answering questions.

### Learning
- Why knowledge should be organized into focused, topic-specific documents.
- How document loading and chunking affect retrieval.
- How embeddings represent text for semantic similarity search.
- Why relevant retrieval does not automatically guarantee a correct answer.
- Why grounding, source attribution, and handling missing information are important.

### Further Exploration
- Compare chunking strategies.
- Evaluate retrieval quality with representative questions.
- Explore metadata filtering and hybrid search.
- Test whether answers remain grounded in retrieved documents.
- Measure retrieval and answer quality using a repeatable evaluation set.

## 8. Cross-Project Learnings

### Backend Architecture
Separating routes, business logic, external integrations, and data access makes applications easier to maintain and test.

### Asynchronous Processing
Background tasks can separate long-running work from HTTP requests, but require reliable task registration, failure handling, and monitoring.

### External Services
API integrations introduce dependencies on network availability, response formats, credentials, rate limits, and service latency.

### LLM Applications
LLM integration requires more than calling a model API. Reliable applications need clear prompts, validation, failure handling, evaluation, and safeguards against unsupported claims.

### Testing and Verification
A feature working once is not sufficient evidence of correctness. Repeatable tests and observable outcomes provide stronger evidence.

## Documentation Rules

For every new experiment, record:

1. **Project:** Where the experiment took place.
2. **Question:** What I wanted to understand or test.
3. **Approach:** What I implemented or compared.
4. **Observation:** What actually happened.
5. **Learning:** What I understood from the result.
6. **Limitations:** What remains unresolved.
7. **Next experiment:** What I plan to investigate next.

Clearly distinguish completed experiments from planned work. Record measured results only when they have actually been observed.
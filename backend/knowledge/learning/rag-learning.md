# AI, LLM, and RAG Learning Journey

## Purpose

This document records my learning and practical exploration of Generative AI, Large Language Models (LLMs), embeddings, semantic search, vector databases, Retrieval-Augmented Generation (RAG), and AI agent systems.

It connects the concepts I study with the tools, experiments, and projects through which I explore them.

The goal is to understand how AI applications work internally and how to build reliable, grounded, maintainable systems using backend engineering.

## 1. Large Language Models (LLMs)

### Concepts Learned

- What Large Language Models are and how they generate text.
- Tokens and tokenization.
- Context windows and token limits.
- Prompt engineering and system instructions.
- Structured outputs and response validation.
- Model limitations, hallucinations, and grounding.
- API-based model integration.

### Tools Explored

- Groq API
- OpenAI API
- Python SDKs for interacting with model providers

### Practical Applications

- JobDiary: generating job-related summaries.
- Are We Dating?: generating conversational advice.
- Purushu: conversational interaction through a language model.

### Further Learning

- Model selection and trade-offs.
- Temperature and generation parameters.
- Streaming responses.
- Token usage and cost management.
- Evaluation of generated responses.

## 2. Embeddings

### Concepts Learned

Embeddings represent text as numerical vectors that can capture semantic relationships.

Related concepts include:

- Text embeddings.
- Semantic similarity.
- Vector dimensions.
- Cosine similarity.
- Document and query embeddings.
- Semantic search versus keyword search.

### Tools and Models Explored

- Sentence Transformers
- `all-MiniLM-L6-v2`
- OpenAI embedding models

### Practical Applications

Embeddings can be used to represent documents, job descriptions, resumes, and user queries so that semantically related content can be retrieved.

### Further Learning

- Compare embedding models.
- Understand how chunk size affects representations.
- Evaluate retrieval relevance.
- Explore multilingual and domain-specific embeddings.

## 3. Semantic Search

### Concepts Learned

Semantic search retrieves content based on meaning rather than requiring exact keyword matches.

A typical workflow is:

1. Collect documents.
2. Split documents into suitable chunks.
3. Generate an embedding for each chunk.
4. Store embeddings with their text and metadata.
5. Embed a user's query.
6. Retrieve the most relevant chunks.
7. Return the matching content or provide it to an LLM.

### Tools Explored

- Sentence Transformers
- Qdrant
- Python

### Practical Applications

- Searching technical documentation.
- Matching resumes with job descriptions.
- Retrieving relevant portfolio information.

### Related Project

**Semantic Engine:** A planned semantic job-matching system that represents job descriptions and resumes as embeddings and retrieves semantically relevant matches.

### Further Learning

- Top-K retrieval.
- Similarity thresholds.
- Metadata filtering.
- Hybrid keyword and vector search.
- Retrieval evaluation and reranking.

## 4. Vector Databases — Qdrant

### Concepts Learned

A vector database stores vectors and supports similarity-based retrieval, often alongside document payloads and metadata.

### Qdrant Operations Explored

- Creating collections with `create_collection()`.
- Adding and updating points with `upsert()`.
- Retrieving points with `retrieve()`.
- Deleting points with `delete()`.
- Counting points with `count()`.
- Running Qdrant locally, in memory, or through Docker.
- Interacting with Qdrant through its API and dashboard.

### Practical Learning Goals

Build a small semantic search system that stores documents and retrieves the most relevant results for a query.

### Further Learning

- Collection configuration and vector dimensions.
- Payload filtering.
- Distance metrics.
- Persistence and deployment.
- Indexing and retrieval performance.
- Updating and deleting document chunks consistently.

## 5. Retrieval-Augmented Generation (RAG)

### Concepts Learned

RAG combines retrieval from an external knowledge source with LLM generation. Retrieved information provides context for answering a user's question.

### Basic RAG Pipeline

Document ingestion → Parsing → Chunking → Embedding → Vector storage → Retrieval → Context construction → LLM generation → Answer

### Core Concepts

- Document loaders.
- Chunking strategies.
- Embedding generation.
- Vector databases.
- Retrievers.
- Top-K retrieval.
- Metadata filtering.
- Context construction.
- Source attribution.
- Grounded answers.
- Hallucination reduction.
- Retrieval and answer evaluation.

### Practical Applications

**Portfolio AssistNet:** A portfolio assistant intended to answer questions about my profile, projects, skills, technical decisions, and documented problem-solving experiences using a Markdown-based knowledge base.

The knowledge base is organized into focused documents so that the system can retrieve relevant information instead of relying entirely on information embedded in a prompt.

### Further Learning

- Overlapping chunks versus non-overlapping chunks.
- Semantic and hierarchical chunking.
- Hybrid search.
- Reranking.
- Query rewriting.
- Context-window management.
- Retrieval precision and recall.
- Faithfulness and answer relevance evaluation.
- Handling questions with insufficient evidence.

## 6. Advanced RAG Techniques

### Topics to Explore

- **Hybrid search:** Combining keyword-based retrieval with vector similarity.
- **Reranking:** Reordering retrieved passages using a relevance model.
- **Metadata filtering:** Restricting retrieval by project, document type, or topic.
- **Hierarchical retrieval:** Connecting small, searchable chunks to larger contextual sections.
- **Query transformation:** Improving retrieval by rewriting or expanding a query.
- **Context compression:** Reducing irrelevant information before passing it to the LLM.
- **Retrieval evaluation:** Measuring whether the correct information is retrieved.
- **Grounded generation:** Ensuring responses are supported by retrieved evidence.

These are learning topics, not claims that every technique has already been implemented.

## 7. AI Agents and Tool Calling

### Concepts to Understand

An AI agent system can use an LLM to select actions, call tools, observe results, and continue toward a goal.

Topics include:

- Tool and function calling.
- Structured tool inputs and outputs.
- State management.
- Short-term and long-term memory.
- Planning and execution loops.
- Workflow orchestration.
- Human approval for sensitive actions.
- Error recovery and retry policies.
- Agent evaluation and observability.

### Current Learning Direction

Understand the difference between a conventional LLM application, a RAG application, a tool-using workflow, and an agent that selects and executes actions.

The aim is to introduce agentic behavior only when it provides a clear benefit over a simpler and more predictable workflow.

## 8. AI Application Architecture

### Backend Integration

Explore how AI capabilities fit into maintainable backend systems using Python and FastAPI.

Key areas:

- API routes and service-layer separation.
- Provider abstraction.
- Request and response schemas.
- Asynchronous API calls.
- Streaming responses.
- Authentication and authorization.
- Error handling and timeouts.
- Logging and observability.
- Configuration and secret management.
- Testing with mocked model providers.

### Reliability and Evaluation

AI systems require evaluation beyond whether an endpoint returns HTTP 200.

Areas to explore include:

- Output correctness.
- Retrieval relevance.
- Faithfulness to source documents.
- Latency and token consumption.
- Failure behavior.
- Regression tests.
- Reproducible evaluation datasets.

## 9. Learning Roadmap

### Phase 1 — LLM Fundamentals
Understand tokens, context windows, prompting, model APIs, and structured responses.

### Phase 2 — Embeddings and Semantic Search
Generate embeddings, calculate similarity, and build a small retrieval system.

### Phase 3 — Vector Databases
Store vectors and metadata in Qdrant and implement Top-K retrieval.

### Phase 4 — Basic RAG
Connect document ingestion, chunking, embeddings, retrieval, and answer generation.

### Phase 5 — RAG Quality
Explore hybrid search, reranking, metadata filtering, chunking improvements, and evaluation.

### Phase 6 — AI Agents
Learn tool calling, state, workflow orchestration, and controlled action execution.

### Phase 7 — Production AI Applications
Focus on security, observability, testing, latency, cost, reliability, and deployment.

## 10. Learning Documentation Rules

For each new concept or tool, record:

- **Concept:** What it is.
- **Purpose:** Why it is useful.
- **Mechanism:** How it works.
- **Tool:** Which library, model, or service was explored.
- **Project:** Where it was applied or tested.
- **Observation:** What the experiment demonstrated.
- **Limitations:** What remains unclear or unresolved.
- **Next step:** What to investigate next.

Clearly distinguish concepts studied, tools experimented with, features implemented, and capabilities validated in a working application.

## Overall Objective

Build a strong understanding of how to design, implement, evaluate, and deploy AI applications that combine backend engineering with LLMs, retrieval systems, and, when appropriate, agentic workflows.
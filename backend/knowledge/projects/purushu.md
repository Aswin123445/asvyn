# Purushu — AI-Powered Personal Assistant

## 1. Project Overview

**Purushu** is a Python-based personal AI assistant designed to interact with users through voice commands and automate selected everyday tasks.

The application combines speech recognition, text-to-speech, OpenAI API integration, desktop automation, and utility modules. It also includes a Flask-based local web interface for interaction.

The project explores how AI-powered conversational capabilities can be combined with Python libraries and system automation to build an interactive personal assistant.

**Repository:** https://github.com/Aswin123445/purushu

## 2. Problem Statement

Performing routine tasks can require switching between applications, searching for information, and manually interacting with desktop tools.

Purushu aims to provide a conversational interface for selected tasks, allowing users to issue voice commands and receive spoken responses or trigger supported actions.

## 3. Key Features

### 3.1 Voice Input

Uses `SpeechRecognition` and `PyAudio` to capture and process spoken commands through a microphone.

This provides a hands-free input mechanism for interacting with the assistant.

### 3.2 Text-to-Speech Responses

Uses `pyttsx3` to convert text responses into speech, allowing the assistant to respond audibly.

### 3.3 AI-Powered Conversation

Integrates the OpenAI API to generate conversational responses to supported user requests.

The AI integration provides the language-processing component, while individual Python modules handle specific tasks.

### 3.4 Desktop Automation

Uses `PyAutoGUI` and related utilities to automate selected mouse, keyboard, and screen interactions.

Examples described in the project include taking screenshots and automating repetitive desktop actions.

Desktop automation should be treated carefully because actions may affect the active application or interact with sensitive information.

### 3.5 Wikipedia Search

Uses the `wikipedia` library to retrieve summaries about requested topics.

### 3.6 WhatsApp Messaging

Uses `pywhatkit` to support WhatsApp messaging workflows.

Actual delivery may depend on the environment, account access, and the automation flow.

### 3.7 Joke Generation

Uses `pyjokes` to provide jokes in response to supported commands.

### 3.8 Flask Web Interface

Uses Flask to provide a local web interface for interacting with the assistant.

The exact relationship between the web interface and the voice assistant should be confirmed from the implementation.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application programming |
| OpenAI API | AI-powered conversational responses |
| SpeechRecognition | Speech recognition |
| PyAudio | Microphone audio input |
| pyttsx3 | Text-to-speech |
| PyAutoGUI | Desktop automation |
| pyperclip | Clipboard operations |
| pywhatkit | WhatsApp-related automation |
| wikipedia | Topic summaries |
| pyjokes | Joke generation |
| Flask | Local web interface |
| Pillow | Image processing utilities |
| BeautifulSoup4 | HTML parsing |
| Requests | HTTP requests |
| python-dotenv | Environment variable configuration |

## 5. Project Structure

The reported repository structure is:

```text
purushu/
├── assistant/
│   └── main.py
├── modules/
│   ├── wikipedia functionality
│   ├── WhatsApp functionality
│   ├── joke functionality
│   └── desktop automation
├── config/
├── assets/
├── requirements.txt
└── README.md
```

The module names above describe the documented responsibilities; they are not necessarily the exact filenames in the repository.

- `assistant/` — Core assistant logic and AI integration.
- `modules/` — Individual capabilities such as search, messaging, jokes, and automation.
- `config/` — Configuration and environment settings.
- `assets/` — Supporting files such as images and audio assets.
- `requirements.txt` — Python dependency list.

## 6. High-Level Architecture

The conceptual interaction flow is:

1. **Input:** The assistant receives a voice command or another supported interaction.
2. **Speech recognition:** Spoken input is converted into text.
3. **Command processing:** The application determines which capability should handle the request.
4. **AI integration:** Requests requiring conversational responses can use the OpenAI API.
5. **Task execution:** Supported utility or automation modules perform the requested action.
6. **Response generation:** The application prepares a result or response.
7. **Speech output:** Text responses can be converted into speech using `pyttsx3`.

The Flask interface provides an additional interaction layer. The exact routing and execution flow should be verified against the source code before being documented as the implemented architecture.

## 7. Configuration and Environment

The project uses `python-dotenv` to load configuration from environment variables.

The documented configuration includes an OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Credentials should remain outside version control. The repository documentation also indicates that `.env` is excluded through `.gitignore`.

Microphone functionality may require suitable audio hardware and operating-system permissions. PyAudio may also require PortAudio system dependencies on some Linux environments.

## 8. Engineering Concepts Demonstrated

### LLM API Integration
Connecting a Python application to a hosted language model API and incorporating generated responses into a user interaction flow.

### Speech Processing
Integrating speech recognition and text-to-speech to support voice-based interaction.

### Modular Application Design
Separating individual assistant capabilities into modules instead of placing all functionality in one large file.

### Desktop Automation
Using Python libraries to interact with desktop applications and system interfaces.

### Web Application Development
Using Flask to expose a local web-based interaction interface.

### Configuration Management
Using environment variables to separate secrets and configuration from application code.

### External Library Integration
Combining libraries and services that each provide a specific capability.

## 9. Technical Considerations

Areas worth documenting or validating include:

- Handling speech recognition failures and background noise.
- Managing OpenAI API errors, rate limits, and timeouts.
- Distinguishing direct utility commands from requests requiring an LLM.
- Handling failures in desktop automation and external integrations.
- Preventing unintended mouse or keyboard actions.
- Managing API credentials securely.
- Keeping voice interaction responsive when external requests are slow.
- Defining how Flask requests interact with the assistant's execution flow.

These are engineering considerations, not claims that all have been implemented or encountered.

## 10. Project Status and Evidence

When reviewing the repository, record:

- The exact OpenAI API workflow and model configuration.
- How voice commands are interpreted and routed.
- Which automation tasks are implemented and tested.
- How Flask communicates with the core assistant.
- The error-handling behavior of each external integration.
- Which features have been verified on the intended operating system.

Do not describe the assistant as fully autonomous or production-ready without evidence of the relevant capabilities and safeguards.

## 11. Portfolio Summary

Purushu is a Python-based personal assistant that explores voice-enabled interaction, LLM integration, desktop automation, and modular application design. It combines the OpenAI API with speech recognition, text-to-speech, utility integrations, and a Flask interface to support conversational access to selected everyday tasks.
# EduAgent-OS: Containerized Multi-Agent Educational Orchestrator

An isolated, production-grade asynchronous multi-agent pipeline designed to autonomously ingest remote or local lecture media, extract high-fidelity acoustic streams, compute localized text transcriptions, and execute concurrent semantic synthesis and type-safe verification loops using the official Google GenAI SDK.

## 🏗️ System Architecture

The runtime execution environment is decoupled into four isolated, deterministic layers to maintain strict containment and host-machine neutrality:

1. **Ingestion Layer (`media_fetcher.py`):** Intercepts input targets (URLs/local files), applies performance filters using `yt-dlp`, isolates raw audio frequencies, and outputs normalized `.mp3` media footprints.
2. **Acoustic Layer (`transcriber.py`):** Initializes an on-disk instance of `faster-whisper` inside the container boundary to execute local, hardware-native ML diarization and token translation into time-stamped text arrays.
3. **Orchestration Layer (`main.py`):** Utilizes `asyncio` to concurrently dispatch specialized prompt weights to Gemini sub-agents:
   * **Academic Synthesis Specialist:** Generates hierarchical markdown study materials.
   * **Educational Taxonomist:** Extracts mathematical entities, formulas, and critical terminology into Anki-compliant matrix blocks.
4. **Validation Layer (`schema.py`):** Acts as a programmatic quality gate. It marshals the final synthesis through a strict Pydantic model (`LectureEvaluation`), forcing Gemini to emit structural JSON validating the consistency score and detecting semantic hallucinations.

## 🚀 Quickstart & Deployment Guide

### Prerequisites
* Docker & Docker Compose v2.0+ (Configured for native ARM64 or AMD64 virtualization)
* Active Google AI Studio API Token Credentials

### 1. Environment Configuration
Clone the repository and instantiate your private environment variables. The configuration layers are secured using `.gitignore` to prevent secret leaks to public upstreams:

```text
GEMINI_API_KEY=AQ.Ab...YourActualStudioTokenHere
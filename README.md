# Quinn AI — Conversational AI Assistant

An LLM-powered conversational AI system built for production deployment at JMedia Corp. Quinn handles multi-turn customer queries using the Google Gemini API, responds via voice, and tracks conversation context through a persistent SQL backend.

## Results
- **25% improvement** in customer query resolution efficiency
- **40% reduction** in user interaction effort via voice response integration
- Deployed across a live user base with cloud infrastructure on GCP

## Architecture
User Input (Text / Voice)
↓
Speech Recognition Engine
↓
Google Gemini API (LLM)
↓
SQL Backend (context + logging)
↓
Text + Voice Response


## Features
- Multi-turn conversation with session-aware context tracking
- Google Gemini API for natural language understanding and generation
- Text-to-speech engine for voice responses
- SQL database integration for persistent conversation logging
- Responsible AI compliance built into response pipeline

## Tech Stack
Python · Google Gemini API · Speech Engine (pyttsx3) · SQL · GCP · VMware

## Installation

```bash
git clone https://github.com/akashabbigeri/QUINNAI.git
cd QUINNAI
pip install -r requirements.txt
```

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY=your_key_here
```

Run the app:

```bash
python app.py
```

## Context
Built during an AI engineering internship at JMedia Corp (Oct 2023 – Feb 2024). Part of a broader suite of AI tools deployed to improve customer support operations.

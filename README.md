# Quinn AI

A production-grade conversational AI assistant built with the Google Gemini API and Flask. Multi-turn conversation with per-user session isolation and server-side session storage.

## Architecture

```
User (Browser)
      ↓ HTTP POST /chat
Flask REST API (app.py)
      ↓
Per-session history (Flask-Session / filesystem)
      ↓
Google Gemini 1.5 Flash
      ↓
JSON response → UI
```

## Features

- **Multi-turn memory** — conversation history persists across messages per user session
- **Per-user isolation** — each visitor gets their own independent chat session via server-side storage
- **Session reset** — one-click conversation reset without page reload
- **Safety filters** — Gemini safety settings block harmful content categories
- **XSS-safe rendering** — all model output rendered via `textContent`, never `innerHTML`

## Tech Stack

Python · Flask · Flask-Session · Google Gemini API (`gemini-1.5-flash`) · python-dotenv

## Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/akashabbigeri/QUINNAI.git
cd QUINNAI
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` and fill in:

```
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_secret_key_here
```

Generate a secure `SECRET_KEY` with:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Get a Gemini API key at [aistudio.google.com](https://aistudio.google.com).

**4. Run**
```bash
python app.py
```

Open `http://localhost:5000`.

## API

| Endpoint | Method | Body | Description |
|---|---|---|---|
| `/` | GET | — | Serves the chat UI |
| `/chat` | POST | `{"message": "..."}` | Send a message, returns `{"reply": "..."}` |
| `/reset` | POST | — | Clears current session history |

## Project Background

Built during an AI engineering internship at JMedia Corp (Oct 2023 – Feb 2024) as part of a customer support automation suite. The system improved query resolution efficiency by 25% and reduced user interaction effort by 40% through voice response integration.

## Notes

- Session files accumulate in `.flask_sessions/` — not tracked by git
- For multi-worker or cloud deployment, switch `SESSION_TYPE` to `redis`
- The app will not start without both `GEMINI_API_KEY` and `SECRET_KEY` in `.env`

# Voice & Text Chat with Llama 3

> Chat with Llama 3 by voice or text: speech-to-text, LLM reply, text-to-speech and translation.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)


## Features

- Speech-to-text input.
- Llama 3 replies through Groq.
- Text-to-speech output.
- Optional translation between languages.

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Llama 3 via Groq |
| Speech | speech-to-text and text-to-speech libraries |
| UI | Python desktop / web |

## Quick Start

```bash
git clone https://github.com/dastonbek8747/voice-chat-llama3.git
cd voice-chat-llama3
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # add GROQ_API_KEY
python main.py
```

## Environment variables

| Variable | Meaning |
|---|---|
| `GROQ_API_KEY` | Groq API key for Llama 3. |

## Note

The virtual environment that was once committed here has been removed from version control. Recreate it locally with the commands above.

## License

MIT © 2026 Doston Sultonov.

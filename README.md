# Python Intro Live Class

## Setup

1. Create virtual environment:
```bash
python3 -m venv .chatbot_env
source .chatbot_env/bin/activate
```

2. Install dependencies:
```bash
pip install litellm python-dotenv
```

3. Set up environment variables:
```bash
cp .env.example .env
```
Then edit `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

## Running the Chatbot

Run the interactive chatbot CLI:
```bash
python cli.py
```

Type 'exit' or 'quit' to end the conversation.
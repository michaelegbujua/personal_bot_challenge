# Personal Bot Challenge

Three command-line chatbots powered by the Groq API. They share the same API key and model, but each one behaves differently because of the persona it loads from a single `persona.txt` file.

## The Bots

| Bot | File | Persona |
|-----|------|---------|
| Strict Teacher | `strict_teacher_bot.py` | A strict secondary-school maths tutor who never gives the answer directly, only hints |
| Naija Chef | `naija_chef_bot.py` | A friendly Naija chef who explains recipes with local ingredients and pidgin flavour |
| Customer Support | `customer_support_bot.py` | A customer support rep for a fictional fintech called PayPoint |

## How It Works

- All personas live in `persona.txt`, one per line, each with a label (`teacher:`, `chef:`, `support:`).
- `persona_loader.py` reads the file and returns only the persona a bot asks for.
- Each bot sends its persona as a `system` message, then keeps the conversation history so it remembers earlier turns.
- Requests go to Groq's OpenAI-compatible chat completions endpoint.

## Setup

1. Clone the repo and enter the folder:
```bash
   git clone https://github.com/michaelegbujua/personal_bot_challenge.git
   cd personal_bot_challenge
```
2. Create and activate a virtual environment, then install dependencies:
```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
```
3. Create a `.env` file in the project root:
```
   GROQ_API_KEY=your_key_here
```
   Get a key from the [Groq console](https://console.groq.com).

## Usage

Run any one of the bots:

```bash
python strict_teacher_bot.py
python naija_chef_bot.py
python customer_support_bot.py
```

Type your message and press Enter. Type `exit` to quit.

## Tech Stack

Python, `requests`, `python-dotenv`, Groq API

## What I Learned

- Managing multiple personas from one config file
- Keeping conversation memory across turns
- Keeping secrets out of version control with `.env` and `.gitignore`

## Author

Michael Egbujua
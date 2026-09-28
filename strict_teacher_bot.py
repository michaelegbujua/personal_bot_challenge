import os
import requests
from dotenv import load_dotenv




load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")    

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

#the persona.txt file should contain the persona of the bot
MODEL = "qwen/qwen3.8-27b"  # confirm this exact ID in your Groq console

#add a load_persona function to load the individual persona from persona.txt file
path ="persona.txt"
def load_persona(name, path=path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.lower().startswith(name.lower() + ":"):
                return line.split(":", 1)[1].strip()
    raise ValueError(f"Persona '{name}' not found in {path}")

persona = load_persona("teacher")   # "chef" or "support" in the other files
memory = [{"role": "system", "content": persona}]

while True:
    user_input = input("You (type 'exit' to quit): ").strip()
    if user_input.lower() in ["exit", "quit", "n", "no", "nope", "nah"]:
        break

    memory.append({"role": "user", "content": user_input})
    response = requests.post(url, headers=headers,
                             json={"model": MODEL, "messages": memory})

    if response.status_code != 200:
        print("Error:", response.status_code, response.json())
        memory.pop()  # drop the failed message so history stays clean
        continue

    reply = response.json()["choices"][0]["message"]["content"]
    print("AI:", reply)
    memory.append({"role": "assistant", "content": reply})
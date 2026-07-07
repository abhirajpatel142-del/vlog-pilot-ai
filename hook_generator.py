import requests

API_KEY = "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"
URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_hooks(topic):
    prompt = f"""
Generate 10 viral YouTube Shorts hooks in Hindi.

Topic:
{topic}

Rules:
- 1-2 lines only
- Curiosity based
- Emotional
- Scroll stopping
- Human sounding

Only return hooks.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 200:
        hooks = response.json()["choices"][0]["message"]["content"]

        with open("outputs/hooks.txt", "w", encoding="utf-8") as f:
            f.write(hooks)

        print("✅ Hooks Generated!")
    else:
        print("Error:", response.text)

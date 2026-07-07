import requests

API_KEY = "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"
URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_titles(topic):
    prompt = f"""
Generate 10 viral YouTube Shorts titles in Hindi for this topic:

{topic}

Rules:
- Maximum 60 characters
- High CTR
- Curiosity based
- Emotional
- Viral style

Only return the titles.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 200:
        titles = response.json()["choices"][0]["message"]["content"]

        with open("outputs/titles.txt", "w", encoding="utf-8") as f:
            f.write(titles)

        print("✅ Viral Titles Generated!")
    else:
        print("Error:", response.text)

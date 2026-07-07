import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY ="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"


URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_script(topic):
    prompt = f"""
Tum India ke No.1 YouTube Shorts aur Mini Vlog Script Writer ho.

User ka topic:
{topic}

Tum khud decide karo ki is topic ke liye kaunsa style best rahega:
1. Daily Mini Vlog
2. Story Based Vlog
3. Cinematic Lifestyle Vlog

Agar zarurat ho to teeno styles ko mix karke sabse engaging script banao.

Requirements:
- 30-45 seconds
- Hindi (natural, human-like)
- Strong 2-second hook
- Curiosity maintain karo
- Emotional ya satisfying ending
- Voiceover-friendly lines
- Viral YouTube Shorts style

Output format:

TITLE:
HOOK:
VOICEOVER:
SHOT LIST:
CAPTION:
THUMBNAIL TEXT:
10 HASHTAGS:
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
        script = response.json()["choices"][0]["message"]["content"]

        print(script)

        with open("outputs/output_script.txt", "w", encoding="utf-8") as f:
            f.write(script)

        print("✅ Script saved to output_script.txt")

    else:
        print("Error:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    topic = input("Enter topic: ")
    generate_script(topic)

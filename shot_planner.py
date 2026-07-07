import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = "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"

URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_shot_plan(topic):
    prompt = f"""
Tum ek professional YouTube Shorts Director ho.

Topic: {topic}

Is topic ke liye:
1. 8 cinematic shots.
2. Har shot ka camera angle.
3. Har shot kitne seconds ka ho.
4. B-roll ideas.
5. Editing tips.
6. Background music mood.

Output sirf Hindi me do.
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
        plan = response.json()["choices"][0]["message"]["content"]
        print(plan)

        with open("outputs/shot_plan.txt", "w", encoding="utf-8") as f:
            f.write(plan)

        print("✅ Shot plan saved!")
    else:
        print(response.text)

if __name__ == "__main__":
    topic = input("Enter topic: ")
    generate_shot_plan(topic)

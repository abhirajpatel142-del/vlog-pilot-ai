import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = "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"

URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_editing_guide(topic):
    prompt = f"""
Tum ek professional CapCut editor ho.

Topic: {topic}

Hindi me ye batao:

1. Hook ke baad kis second par cut lagana hai.
2. Kis shot par zoom use karna hai.
3. Kis transition ka use karna hai.
4. Kahan text dikhana hai.
5. Kahan sound effect lagana hai.
6. Kis type ka background music use karna hai.

Output short aur clear hona chahiye.
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
        result = response.json()["choices"][0]["message"]["content"]

        print(result)

        with open("outputs/editing_guide.txt", "w", encoding="utf-8") as f:
            f.write(result)

        print("✅ Editing Guide Saved!")

    else:
        print(response.text)

if __name__ == "__main__":
    topic = input("Enter topic: ")
    generate_editing_guide(topic)

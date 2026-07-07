import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = "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"

URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_youtube_pack(topic):
    prompt = f"""
Tum YouTube SEO Expert ho.

Topic:
{topic}

Hindi me ye generate karo:

1. Viral SEO Title
2. YouTube Description
3. Thumbnail Text
4. Pinned Comment
5. Call To Action
6. 20 Trending Hashtags

Output professional aur YouTube Shorts ke hisaab se hona chahiye.
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

        with open("outputs/youtube_pack.txt", "w", encoding="utf-8") as f:
            f.write(result)

        print("✅ YouTube Pack Saved!")

    else:
        print(response.text)

if __name__ == "__main__":
    topic = input("Enter topic: ")
    generate_youtube_pack(topic)

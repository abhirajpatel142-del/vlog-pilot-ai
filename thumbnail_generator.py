from script_generator import generate_script

def generate_thumbnail_prompt(topic):
    prompt = f"""
🎨 AI THUMBNAIL PROMPT

Topic: {topic}

Create a YouTube Shorts thumbnail with:

- Cinematic lighting
- High contrast
- Bright colors
- Emotional expression
- Ultra realistic
- Viral YouTube style
- Big bold text
- 9:16 composition

Main Subject:
{topic}
"""

    with open("outputs/thumbnail_prompt.txt", "w", encoding="utf-8") as f:
        f.write(prompt)

    print("🖼️ Thumbnail Prompt Generated!")

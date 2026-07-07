import asyncio
import edge_tts

VOICE = "hi-IN-SwaraNeural"

async def generate_voice():
    with open("outputs/output_script.txt", "r", encoding="utf-8") as f:
        text = f.read()

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("outputs/voice.mp3")

    print("✅ Voice Generated!")

if __name__ == "__main__":
    asyncio.run(generate_voice())

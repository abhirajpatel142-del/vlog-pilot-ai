from hook_generator import generate_hooks
from title_generator import generate_titles
from script_generator import generate_script
from shot_planner import generate_shot_plan
from voice_generator import generate_voice
from youtube_pack import generate_youtube_pack
from editing_guide import generate_editing_guide
from thumbnail_generator import generate_thumbnail_prompt
import asyncio

def main():
    topic = input("Enter topic: ")

    print("\n🧠 Generating Script...")
    generate_script(topic)

    print("\n🎬 Generating Shot Plan...")
    generate_shot_plan(topic)

    print("\n🎤 Generating Voice...")
    asyncio.run(generate_voice())

    print("\n📺 Generating YouTube Pack...")
    generate_youtube_pack(topic)

    print("\n✂️ Generating Editing Guide...")
    generate_editing_guide(topic)

    generate_thumbnail_prompt(topic)

    generate_titles(topic)
    
    generate_hooks(topic)

    print("\n🎉 Vlog Pilot Finished Successfully!")

if __name__ == "__main__":
    main()

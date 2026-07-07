def generate_shorts(topic):

    return {
        "status": "success",
        "topic": topic,

        "title": f"{topic} | Viral Shorts Story 🔥",

        "hook": f"Ek chhoti si {topic}… jo aapki soch badal degi 😳",

        "voiceover": (
            f"Aaj ka topic hai {topic}. "
            "Shuru me sab normal lag raha tha, "
            "lekin dheere dheere sab kuch change ho gaya. "
            "Aur us din mujhe ek bada life lesson mila."
        ),

        "scenes": [
            f"Scene 1: Introduction of {topic}",
            "Scene 2: Normal life moment",
            "Scene 3: Conflict or twist",
            "Scene 4: Emotional peak",
            "Scene 5: Ending lesson"
        ],

        "on_screen_text": [
            "Don’t ignore small moments ❤️",
            "Life is unpredictable 😳",
            "Every moment matters"
        ],

        "caption": f"{topic} | Real Life Viral Story ❤️",

        "hashtags": f"#{topic.replace(' ','')} #shorts #viral #minivlog #story"
    }

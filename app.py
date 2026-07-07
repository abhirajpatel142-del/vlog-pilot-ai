from thumbnail_generator import generate_thumbnail
from flask import Flask, render_template, request, send_file
import os
import asyncio
import zipfile

from script_generator import generate_script
from shot_planner import generate_shot_plan
from youtube_pack import generate_youtube_pack
from editing_guide import generate_editing_guide
from voice_generator import generate_voice

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        topic = request.form["topic"]

        os.makedirs("uploads", exist_ok=True)
        os.makedirs("outputs", exist_ok=True)

        files = request.files.getlist("clips")

        for file in files:
            if file.filename:
                file.save(os.path.join("uploads", file.filename))

        generate_script(topic)
        generate_shot_plan(topic)
        generate_youtube_pack(topic)
        generate_editing_guide(topic)
        asyncio.run(generate_voice())
        thumbnail = generate_thumbnail(topic)

        script = open("outputs/output_script.txt", encoding="utf-8").read()
        titles = open("outputs/titles.txt", encoding="utf-8").read()
        hooks = open("outputs/hooks.txt", encoding="utf-8").read()
        thumbnail = open("outputs/thumbnail_prompt.txt", encoding="utf-8").read()

        return render_template(
            "result.html",
            script=script,
            titles=titles,
            hooks=hooks,
            thumbnail=thumbnail
        )

    return render_template("index.html")


@app.route("/download")
def download():

    zip_path = "outputs/vlog_package.zip"

    with zipfile.ZipFile(zip_path, "w") as zipf:

        files = [
            "outputs/output_script.txt",
            "outputs/titles.txt",
            "outputs/hooks.txt",
            "outputs/thumbnail_prompt.txt",
            "outputs/shot_plan.txt",
            "outputs/editing_guide.txt",
            "outputs/voice.mp3"
        ]

        for file in files:
            if os.path.exists(file):
                zipf.write(file, os.path.basename(file))

    return send_file(zip_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

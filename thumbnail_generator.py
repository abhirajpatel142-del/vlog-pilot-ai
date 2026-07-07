from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_FOLDER = "static/thumbnails"

def generate_thumbnail(title):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    width = 1280
    height = 720

    image = Image.new("RGB", (width, height), (25, 25, 45))

    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 80)
    except:
        font = ImageFont.load_default()

    draw.text(
        (80, 250),
        title.upper(),
        fill=(255, 255, 0),
        font=font
    )

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "thumbnail.png"
    )

    image.save(output_path)

    return output_path

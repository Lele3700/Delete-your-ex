from PIL import Image, ImageDraw, ImageFont
import face_recognition
from pathlib import Path

def draw_red_boxes(image_path, output_path):
    """
    Draw red boxes around faces in an image and save the output.
    :param image_path: Path to the input image file.
    :param output_path: Path to save the processed image.
    """
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.load_default()

    for (top, right, bottom, left) in face_locations:
        for offset in range(5):  # Thickness of the rectangle
            draw.rectangle(
                [(left - offset, top - offset), (right + offset, bottom + offset)],
                outline=(255, 0, 0),
            )
        text = "Face"
        draw.text((left, bottom + 5), text, fill=(255, 0, 0), font=font)

    pil_image.save(output_path)

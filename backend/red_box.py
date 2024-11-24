from PIL import Image, ImageDraw, ImageFont
import face_recognition
from pathlib import Path

# Path to the image file
ex_path = Path(__file__).resolve().parent
image_path = ex_path / "ex_picture" / "lara.jpeg"

# Load the image
unknown_image = face_recognition.load_image_file(image_path)

# Find all the faces in the image
face_locations = face_recognition.face_locations(unknown_image)

# Convert the image to a PIL image for drawing
pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

# Font for the text (optional: specify a TTF font file for custom font)
font = ImageFont.load_default()

# Loop through each face found in the image
for (top, right, bottom, left) in face_locations:
    # Draw a red rectangle around the face with a thicker width
    for offset in range(5):  # Adjust the width by drawing multiple rectangles
        draw.rectangle(
            [(left - offset, top - offset), (right + offset, bottom + offset)],
            outline=(255, 0, 0),
        )

    # Add the name "ex" below the red rectangle
    text = "ex"
    text_bbox = draw.textbbox((0, 0), text, font=font)  # Calculate text bounding box
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_position = (left, bottom + 5)  # Position the text below the rectangle
    draw.text(text_position, text, fill=(255, 0, 0), font=font)

# Clean up the drawing object
del draw

# Save the image with rectangles and text
output_path = ex_path / "ex_picture" / "ex_.jpg"
pil_image.save(output_path)

print(f"Processed image saved at {output_path}")

from PIL import Image, ImageDraw, ImageFont

def add_emoji_to_image(photo_path, emoji_path, coordinates, output_path, emoji_size=(100,100)):
    """
    Adds an emoji at the specified coordinates on the photo.
    
    :param photo_path: Path to the photo (JPEG).
    :param emoji_path: Path to the emoji (transparent PNG).
    :param coordinates: Tuple (x, y) for the location of the emoji.
    :param output_path: Path to save the resulting image.
    """
    # Load the photo
    photo = Image.open(photo_path).convert("RGBA")
    
    # Load the emoji
    emoji = Image.open(emoji_path).convert("RGBA")
    
    emoji = emoji.resize(emoji_size)
    
    # Overlay the emoji onto the photo
    photo.paste(emoji, coordinates, emoji)  # Use emoji as its own mask for transparency

    # Convert back to RGB to save as JPG
    photo = photo.convert("RGB")
    photo.save(output_path, "JPEG")

if "__main__" == __name__:
    photo_path = r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_input\lara_victoria.jpeg"  # Input photo path
    emoji_path = r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\emojis\goblin.png"  # Input emoji path
    coordinates = (400, 150)  # Example coordinates
    output_path = r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_output\lara_victoria_goblin.jpeg"  # Output photo path
    add_emoji_to_image(photo_path, emoji_path, coordinates, output_path)
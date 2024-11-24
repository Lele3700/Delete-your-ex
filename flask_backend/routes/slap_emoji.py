from PIL import Image

def add_emoji_to_image(photo_path, emoji_path, coordinates, output_path, size=(100, 100)):
    """
    Adds an emoji to a photo at the specified coordinates.
    :param photo_path: Path to the input photo.
    :param emoji_path: Path to the emoji image (PNG).
    :param coordinates: Tuple (x, y) for the emoji placement.
    :param output_path: Path to save the resulting image.
    :param size: Size of the emoji as (width, height).
    """
    photo = Image.open(photo_path).convert("RGBA")
    emoji = Image.open(emoji_path).convert("RGBA")
    emoji = emoji.resize(size)
    photo.paste(emoji, coordinates, emoji)
    photo.convert("RGB").save(output_path, "JPEG")

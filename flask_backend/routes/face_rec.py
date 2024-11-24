from PIL import Image
import face_recognition
from pathlib import Path
import os
import random
from flask import current_app

def choice_emoji(emoji):
    """
    Returns the absolute path of an emoji file.
    
    Args:
        emoji (str): The name of the emoji (without the ".png").
    
    Returns:
        Path: The full path to the emoji file.
    """
    emoji = emoji + ".png"
    # Use the current_app.root_path to ensure a path relative to the Flask app's root
    path_emoji_lib = Path(current_app.root_path) / "emojis"
    return path_emoji_lib / emoji

def get_random_emoji():
    """
    Retrieves a random emoji file from the 'emojis' folder.
    
    Returns:
        str: A random file path from the folder, or None if no files are found.
    """
    # Use the current_app.root_path to ensure the correct path to the folder
    folder_path = Path(current_app.root_path) / "emojis"
    
    # Ensure the folder exists
    if not folder_path.exists():
        print(f"Folder does not exist: {folder_path}")
        return None
    
    # Get all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        print(f"No files found in folder: {folder_path}")
        return None
    
    # Choose a random file from the list
    random_file = random.choice(files)
    return folder_path / random_file

def create_folder(folder_path):
    """
    Creates a folder if it doesn't exist.

    Args:
        folder_path (str): The path to the folder.
    
    Returns:
        bool: True if the folder was created, False if it already existed.
    """
    # Use the Flask app's root path as the base directory
    absolute_folder_path = os.path.join(current_app.root_path, folder_path)
    
    # Check if the folder exists, and create it if not
    if not os.path.exists(absolute_folder_path):
        os.makedirs(absolute_folder_path)  # Create the folder and intermediate directories if necessary
        print(f"Folder created: {absolute_folder_path}")
        return True
    else:
        print(f"Folder already exists: {absolute_folder_path}")
        return False

def get_face_code(image_path):
    """
    Get the face encoding from an image.
    :param image_path: Path to the image file.
    :return: Face encoding.
    """
    try:
        image = face_recognition.load_image_file(image_path)
        face_code = face_recognition.face_encodings(image)[0]
        return face_code
    except Exception as e:
        raise ValueError(f"Error processing image: {str(e)}")

def get_coordinates(image_path, i):
    """
    Get facial landmark coordinates for a specific face in the image.
    :param image_path: Path to the image file.
    :param i: Index of the face in the image.
    :return: Facial landmarks as a dictionary.
    """
    image = face_recognition.load_image_file(image_path)
    face_landmarks_list = face_recognition.face_landmarks(image)
    return face_landmarks_list[i]

def find_faces(image_path):
    """
    Find face encodings in an image.
    :param image_path: Path to the image file.
    :return: List of face encodings.
    """
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings

def match_encodings(encoding1, encoding2):
    """
    Compare two face encodings to check if they match.
    :param encoding1: First face encoding.
    :param encoding2: Second face encoding.
    :return: Boolean indicating match.
    """
    results = face_recognition.compare_faces([encoding1], encoding2)
    return results[0]

def add_emoji_to_image(photo_path, emoji_path, coordinates, output_path, size=(100, 100)):
    """
    Add an emoji to the specified location on a photo.
    :param photo_path: Path to the photo.
    :param emoji_path: Path to the emoji image.
    :param coordinates: Tuple (x, y) for the emoji position.
    :param output_path: Path to save the modified image.
    :param size: Tuple indicating the size of the emoji.
    """
    photo = Image.open(photo_path).convert("RGBA")
    emoji = Image.open(emoji_path).convert("RGBA")
    emoji = emoji.resize(size)

    photo.paste(emoji, coordinates, emoji)  # Use transparency mask
    photo.convert("RGB").save(output_path, "JPEG")


def remove_ex(path_to_img, ex_image, list_of_images, emoji, output_path):
    """
    Overlay an emoji on the face matching the excluded image.
    :param path_to_img: Path to the directory with images.
    :param ex_image: Image of the face to exclude.
    :param list_of_images: List of image file names to process.
    :param emoji: Path to the emoji image.
    :param output_path: Directory to save processed images.
    """

    try:
        ex = face_recognition.load_image_file(Path(path_to_img) / ex_image)
        face_code_ex = face_recognition.face_encodings(ex)[0]
    except Exception as e:
        raise ValueError(f"Error loading excluded image: {str(e)}")

    for image in list_of_images:
        faces = find_faces(Path(path_to_img) / image)
        index = -1
        for face in range(len(faces)):
            if match_encodings(face_code_ex, faces[face]):
                index = face

        if index == -1:
            raise ValueError(f"No matching face found in {image}")

        landmarks = get_coordinates(Path(path_to_img) / image, index)

        mini = min(y for _, y in landmarks["left_eyebrow"])
        maximum = max(y for _, y in landmarks["chin"])

        chin_to_brow = int(1.8 * (maximum - mini))
        size = (chin_to_brow, chin_to_brow)
        dist = int(0.5 * chin_to_brow)

        coords_0 = landmarks['nose_tip'][2][0] - dist
        coords_1 = landmarks['nose_tip'][2][1] - dist
        coords = (coords_0, coords_1)

        output_file = Path(output_path) / (Path(image).stem + "_edited.jpeg")
        add_emoji_to_image(Path(path_to_img) / image, emoji, coords, output_file, size)
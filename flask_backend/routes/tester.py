from PIL import Image
import face_recognition
import os
from pathlib import Path
import random
from flask import Flask, current_app

def test_choice_emoji():
    emoji_name = "smile"
    emoji_path = choice_emoji(emoji_name)
    print(f"Path to emoji: {emoji_path}")

def test_get_random_emoji():
    random_emoji = get_random_emoji()
    print(f"Random emoji file: {random_emoji}")

def test_create_folder():
    folder_path = "test_folder"
    success = create_folder(folder_path)
    print(f"Folder creation status: {success}")

def test_get_face_code():
    image_path = "test_image.jpg"
    try:
        face_code = get_face_code(image_path)
        print(f"Face encoding: {face_code}")
    except Exception as e:
        print(f"Error: {e}")

def test_match_encodings():
    image_path1 = "test_image1.jpg"
    image_path2 = "test_image2.jpg"
    try:
        encoding1 = get_face_code(image_path1)
        encoding2 = get_face_code(image_path2)
        match = match_encodings(encoding1, encoding2)
        print(f"Do the faces match? {match}")
    except Exception as e:
        print(f"Error: {e}")

def test_add_emoji_to_image():
    photo_path = "photo.jpg"
    emoji_path = "emoji.png"
    coordinates = (100, 100)
    output_path = "output_image.jpg"
    add_emoji_to_image(photo_path, emoji_path, coordinates, output_path)
    print(f"Emoji added to image: {output_path}")

# Run tests
test_choice_emoji()
test_get_random_emoji()
test_create_folder()
test_get_face_code()
test_match_encodings()
test_add_emoji_to_image()

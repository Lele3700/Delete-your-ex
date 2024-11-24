from flask import Flask, jsonify, current_app
import os

app = Flask(__name__)

# Ensure you have a folder like "emojis" under the root path of your Flask app
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'emojis')

@app.route('/test_choice_emoji/<emoji>')
def test_choice_emoji_route(emoji):
    emoji_path = choice_emoji(emoji)
    return jsonify({"emoji_path": str(emoji_path)})

@app.route('/test_get_random_emoji')
def test_get_random_emoji_route():
    random_emoji = get_random_emoji()
    if random_emoji:
        return jsonify({"random_emoji": str(random_emoji)})
    else:
        return jsonify({"error": "No emoji found"}), 404

@app.route('/test_create_folder')
def test_create_folder_route():
    folder_path = "test_folder"
    success = create_folder(folder_path)
    return jsonify({"folder_created": success})

@app.route('/test_get_face_code/<image_path>')
def test_get_face_code_route(image_path):
    try:
        face_code = get_face_code(image_path)
        return jsonify({"face_encoding": str(face_code)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/test_match_encodings/<image_path1>/<image_path2>')
def test_match_encodings_route(image_path1, image_path2):
    try:
        encoding1 = get_face_code(image_path1)
        encoding2 = get_face_code(image_path2)
        match = match_encodings(encoding1, encoding2)
        return jsonify({"faces_match": match})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/test_add_emoji_to_image')
def test_add_emoji_to_image_route():
    photo_path = "photo.jpg"
    emoji_path = "emoji.png"
    coordinates = (100, 100)
    output_path = "output_image.jpg"
    add_emoji_to_image(photo_path, emoji_path, coordinates, output_path)
    return jsonify({"message": f"Emoji added to image: {output_path}"})


if __name__ == "__main__":
    app.run(debug=True)

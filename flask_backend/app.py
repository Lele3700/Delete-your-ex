from flask import Flask, request, jsonify
from routes.face_rec import get_face_code, remove_ex
from routes.red_box import draw_red_boxes

app = Flask(__name__)
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for communication with the React frontend

# Your current routes
@app.route('/api/face-code', methods=['POST'])
def face_code():
    data = request.json
    image_path = data['image_path']
    try:
        face_code = get_face_code(image_path)
        return jsonify({'face_code': face_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/remove-face', methods=['POST'])
def remove_face():
    files = request.files.getlist("images")  # Multiple files
    emoji_path = request.form["emoji_path"]  # Emoji file or name
    output_dir = os.path.join(os.getcwd(), "output")

    try:
        os.makedirs(output_dir, exist_ok=True)
        output_files = []

        for file in files:
            input_path = os.path.join(output_dir, file.filename)
            output_path = os.path.join(output_dir, f"modified_{file.filename}")
            file.save(input_path)

            # Apply emoji to each image
            remove_ex(input_path, emoji_path, None, output_path)
            output_files.append(output_path)

        # Zip the results
        zip_filename = os.path.join(output_dir, "results.zip")
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            for file in output_files:
                zipf.write(file, os.path.basename(file))

        return jsonify({"message": "Processing complete", "zip_path": zip_filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/red-box', methods=['POST'])
def red_box():
    data = request.json
    image_path = data['image_path']
    output_path = data['output_path']
    try:
        draw_red_boxes(image_path, output_path)
        return jsonify({'message': 'Red box added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/add-emoji', methods=['POST'])
def add_emoji():
    """
    API route to call the add_emoji_to_image function.
    """
    data = request.json
    photo_path = data['photo_path']
    emoji_path = data['emoji_path']
    coordinates = tuple(data['coordinates'])  # Ensure this is a tuple
    output_path = data['output_path']
    size = tuple(data.get('size', (100, 100)))  # Default size if not provided

    try:
        # Call the function
        add_emoji_to_image(photo_path, emoji_path, coordinates, output_path, size=size)
        return jsonify({'message': 'Emoji added successfully', 'output_path': output_path})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# New routes for image handling
@app.route('/images/<filename>', methods=['GET'])
def serve_image(filename):
    """Serve an image from the static folder."""
    static_folder = os.path.join(os.getcwd(), "static")
    return send_from_directory(static_folder, filename)

@app.route('/api/images', methods=['GET'])
def get_images():
    """Return a list of image paths available in the static folder."""
    static_folder = os.path.join(os.getcwd(), "static")
    images = [f"/images/{img}" for img in os.listdir(static_folder) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return jsonify(images)

@app.route('/api/upload', methods=['POST'])
def upload_image():
    """Handle image upload from the React frontend."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    static_folder = os.path.join(os.getcwd(), "static")
    filepath = os.path.join(static_folder, file.filename)
    file.save(filepath)

    return jsonify({'message': 'File uploaded successfully', 'path': f"/images/{file.filename}"})

if __name__ == '__main__':
    app.run(debug=True)

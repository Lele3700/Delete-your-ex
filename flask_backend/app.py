from routes.face_rec import get_face_code, remove_ex
from routes.red_box import draw_red_boxes
from routes.face_rec import add_emoji_to_image
from flask_cors import CORS
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def index():
    return "Welcome to the Flask API! Available endpoints: /api/face-code, /api/remove-face, /api/red-box, /api/add-emoji"

@app.route('/api/upload_image', methods=['POST'])
def upload_image():
    # Log request details
    app.logger.info("Received request to /api/upload-image")

    if 'image' not in request.files:
        app.logger.error("No image part in the request")
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']

    if image.filename == '':
        app.logger.error("No file selected")
        return jsonify({'error': 'No selected file'}), 400

    try:
        upload_dir = "./uploads"
        os.makedirs(upload_dir, exist_ok=True)

        # Save the uploaded file
        file_path = os.path.join(upload_dir, image.filename)
        image.save(file_path)
        return jsonify({'message': f"File {image.filename} uploaded successfully"})
    except Exception as e:
        app.logger.error(f"Error saving file: {str(e)}")
        return jsonify({'error': str(e)}), 500
        
# Route for getting face code
@app.route('/api/face-code', methods=['POST'])
def face_code(image_file):
    # If the function expects a file path, save the file first
    temp_path = "./uploads/temp_image.jpg"
    image_file.save(temp_path)
    # Process the saved image
    face_code = get_face_code(temp_path)
    return face_code

# Route for removing face
@app.route('/api/remove-face', methods=['POST'])
def remove_face():
    data = request.json
    path_to_img = data['path_to_img']
    ex_image = data['ex_image']
    list_of_images = data['list_of_images']
    emoji = data['emoji']
    output_path = data['output_path']
    try:
        remove_ex(path_to_img, ex_image, list_of_images, emoji, output_path)
        return jsonify({'message': 'Faces removed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for red box
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

# Route for adding emoji
@app.route('/api/add-emoji', methods=['POST'])
def add_emoji():
    data = request.json
    photo_path = data['photo_path']
    emoji_path = data['emoji_path']
    coordinates = tuple(data['coordinates'])
    output_path = data['output_path']
    try:
        add_emoji_to_image(photo_path, emoji_path, coordinates, output_path)
        return jsonify({'message': 'Emoji added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

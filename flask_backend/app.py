from flask import Flask, request, jsonify
from routes.face_rec import get_face_code, remove_ex
from routes.red_box import draw_red_boxes
from routes.slap_emoji import add_emoji_to_image

app = Flask(__name__)

# Route for getting face code
@app.route('/api/face-code', methods=['POST'])
def face_code():
    data = request.json
    image_path = data['image_path']
    try:
        face_code = get_face_code(image_path)
        return jsonify({'face_code': face_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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

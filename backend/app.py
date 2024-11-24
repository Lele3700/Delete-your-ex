from flask import Flask, request, jsonify
from pathlib import Path
import face_recognition
import slap_emoji as sp
from PIL import Image

app = Flask(__name__)

# Set input/output paths
IMAGE_IN = Path(__file__).resolve().parent / "pictures_input"
IMAGE_OUT = Path(__file__).resolve().parent / "pictures_output"
EMOJI = Path(__file__).resolve().parent / "emojis" / "pile-of-poo.png"

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        data = request.json
        ex_image = data['ex_image']
        images = data['images']
        emoji = EMOJI
        output_path = IMAGE_OUT

        # Find face in the example image
        ex_path = IMAGE_IN / ex_image
        ex = face_recognition.load_image_file(ex_path)
        face_cod_ex = face_recognition.face_encodings(ex)[0]

        results = []
        for image in images:
            image_path = IMAGE_IN / image
            faces = face_recognition.face_encodings(face_recognition.load_image_file(image_path))
            match_found = False
            for i, face in enumerate(faces):
                if face_recognition.compare_faces([face_cod_ex], face)[0]:
                    match_found = True
                    landmarks = face_recognition.face_landmarks(face_recognition.load_image_file(image_path))[i]
                    
                    # Calculate chin-to-brow distance
                    mini = min(y for x, y in landmarks["left_eyebrow"])
                    maximum = max(y for x, y in landmarks["chin"])
                    chin_to_brow = int(1.8 * (maximum - mini))
                    size = (chin_to_brow, chin_to_brow)
                    
                    # Calculate coordinates
                    dist = int(0.5 * chin_to_brow)
                    coords_0 = landmarks['nose_tip'][2][0] - dist
                    coords_1 = landmarks['nose_tip'][2][1] - dist
                    coords = (coords_0, coords_1)

                    # Create output image
                    out_image = image[:-4] + "_edited.jpeg"
                    out_path = output_path / out_image
                    sp.add_emoji_to_image(image_path, emoji, coords, out_path, size)
                    results.append({"image": image, "output": str(out_path)})
                    break
            
            if not match_found:
                results.append({"image": image, "output": None, "error": "No matching face found"})

        return jsonify({"status": "success", "results": results}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

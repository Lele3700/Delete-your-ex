import slap_emoji as sp
from PIL import Image, ImageDraw
import face_recognition 
from pathlib import Path

image_path = Path(__file__).resolve().parent
def get_face_code(image):

    try: 
        image = face_recognition.load_image_file(image)
        face_cod  = face_recognition.face_encodings(image)[0]
    except:
        print("Face not found")
    
    return face_cod

def get_coordinates(image,i):
    image = face_recognition.load_image_file(image)
    face_landmarks_list = face_recognition.face_landmarks(image)
    return face_landmarks_list[i]

def find_faces(image):
    image = face_recognition.load_image_file(image)
    Face_encodings = face_recognition.face_encodings(image)
    return Face_encodings

def match_encodings(encodin1,encodin2):
    results = face_recognition.compare_faces([encodin1], encodin2)
    return results[0]


def remove_ex(path_to_img,ex_image,list_of_images,emoji,output_path):

    try: 
        ex = face_recognition.load_image_file(path_to_img / ex_image)
        face_cod_ex  = face_recognition.face_encodings(ex)[0]
    except:
        print("Face not found")

    for image in list_of_images:
        faces = find_faces(path_to_img / image)
        
        for face in range(len(faces)):
            if match_encodings(face_cod_ex,faces[face]):
                index = face

        landmarks = get_coordinates(image_in / image ,index)

        mini = 10000
        for x,y in landmarks["left_eyebrow"]:
            mini = min(y,mini)
        maximum = 0
        for x,y in landmarks["chin"]:
            maximum = max(y,maximum)

        chin_to_brow = int(1.8*(maximum-mini))
        size = (chin_to_brow, chin_to_brow)

        dist=int(0.5*chin_to_brow)

        coords_0=landmarks['nose_tip'][2][0]-dist
        coords_1=landmarks['nose_tip'][2][1]-dist

        coords=(coords_0, coords_1)

        out_image = image[:-4] + "_edited.jpeg"
        out_path=output_path / out_image

        print(path_to_img/image, emoji, coords, out_path, size)
        sp.add_emoji_to_image(path_to_img/image, emoji, coords, out_path, size)


image_in = Path(__file__).resolve().parent / "pictures_input"
image_out = Path(__file__).resolve().parent / "pictures_output"
emoji = Path(__file__).resolve().parent / "emojis" / "pile-of-poo.png"

remove_ex(image_in,"lara.jpeg",["lara_lean2.jpeg","lara_victoria.jpeg"],emoji,image_out)
        
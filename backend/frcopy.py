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

ex = get_face_code(image_path / "pictures_input" / "lara.jpeg")
faces = find_faces(image_path / "pictures_input" / "lara_lean.jpeg")

for face in range(len(faces)):
    if match_encodings(ex,faces[face]):
        index = face

landmarks = get_coordinates(image_path / "pictures_input" / "lara_lean.jpeg",index)

nose_tip = landmarks['nose_tip'][2][1]
chin = landmarks['chin'][8][1]
#length = 2*(chin-nose_tip)
#size = (length, length)
#eye_dist = abs(landmarks['right_eye'][2][0]-landmarks['left_eye'][2][0])
#coords_0 = landmarks['right_eyebrow'][2][0]-eye_dist
#coords_1 = landmarks['right_eyebrow'][2][1]+(nose_tip-chin)
#coords = (coords_0, coords_1)


#TESTS START:
#goblin
#coords_0 = landmarks['left_eyebrow'][2][0]-eye_dist
#coords_1 = landmarks['left_eyebrow'][2][1]+chin_to_nose

# goblin2:
#coords_0 = landmarks['left_eyebrow'][2][0]+chin_to_nose
#coords_1 = landmarks['left_eyebrow'][2][1]-eye_dist
#coords = (coords_0, coords_1)

# CONCLUSION: 
# RIGHTWARDS = SUBTRACT TO 2ND COORDINATE
# DOWNWARDS = ADD TO FIRST COORDINATE

# UP MEANS MINUS SECOND COORDINATE
# DOWN MEANS PLUS SECOND COORDINATE
# RIGHT MEANS PLUS FIRST COORINATE
# LEFT MEANS LESS FIRST COORDINATE
# SO UP AND DOWN ARE INVERTED, LEFT AND RIGHT ARE OK
# 0 IS UP IN VERTICAL
# 0 IS LEFT IN HORIZONTAL

# LEFT EYEBROW IS THE ONE TO MY LEFT!!
# TESTS END

#print(chin)
#print(length)
#print(landmarks)

#print(landmarks['chin'])
#pic_path=image_path / "pictures_input" / "lara_victoria.jpeg"
#pic_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_input\nico_kike.jpeg"
#emoji_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\emojis\goblin.png"
#coords=(landmarks['left_eyebrow'][2])
#coords=landmarks['left_eye'][2]
#size=(30,30)
#out_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_output\nico_kike_goblin3.jpeg"
#sp.add_emoji_to_image(pic_path, emoji_path, coords, out_path)

#sp.add_emoji_to_image()

#print("what we got")
#print(landmarks[1][1]['nose_tip'][2])

#image=face_recognition.load_image_file(image_path / "pictures_input" / "lara_victoria.jpeg")
#face_landmarks_list = face_recognition.face_landmarks(image)
#print("person 1:")
#print(face_landmarks_list[0])
#print("person 2:")
#print(face_landmarks_list[1])

#def Get_coords(ex_pic, pic_list):
   #ex_encoding  = face_recognition.face_encodings(ex_pic)
#    for pic in pic_list:
#        facesfind_faces(pic)

# TEST 1: small on left brow
#print(landmarks)
#pic_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_input\nico_kike.jpeg"
#emoji_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\emojis\goblin.png"
#coords=(landmarks['left_eyebrow'][2])
#coords=landmarks['left_eye'][2]
#size=(30,30)
#out_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_output\nico_kike_goblin_snall_left_brow.jpeg"
#sp.add_emoji_to_image(pic_path, emoji_path, coords, out_path, size)


# TEST 2: large on left brow
#print(landmarks)
#pic_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_input\nico_kike.jpeg"
#emoji_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\emojis\goblin.png"
#coords=(landmarks['left_eyebrow'][2])
#coords=landmarks['left_eye'][2]
#size=(300,300)
#out_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_output\nico_kike_goblin_test2.jpeg"
#sp.add_emoji_to_image(pic_path, emoji_path, coords, out_path, size)

#test 3: size 1.5 min brow to max chin
#print(landmarks)
#mini = 10000
#for x,y in landmarks["left_eyebrow"]:
#    mini = min(y,mini)
#maximum = 0
#for x,y in landmarks["chin"]:
#    maximum = max(y,maximum)
#chin_to_brow = int(1.5*(maximum-mini))
#size = (chin_to_brow, chin_to_brow)
#pic_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_input\nico_kike.jpeg"
#emoji_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\emojis\goblin.png"
#coords=(landmarks['left_eyebrow'][2])
#out_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_output\nico_kike_goblin_test3.jpeg"
#sp.add_emoji_to_image(pic_path, emoji_path, coords, out_path, size)

#test 3: size 1.5 min brow to max chin

print(landmarks)

mini = 10000
for x,y in landmarks["left_eyebrow"]:
    mini = min(y,mini)
maximum = 0
for x,y in landmarks["chin"]:
    maximum = max(y,maximum)

chin_to_brow = int(1.8*(maximum-mini))
size = (chin_to_brow, chin_to_brow)
distancey = int(0.7*(maximum-mini))

mini = 10000
for x,y in landmarks["left_eyebrow"]:
    mini = min(y,mini)
maximum = 0
for x,y in landmarks["right_eye"]:
    maximum = max(y,maximum)

distancex = int((maximum - mini)*2.75)

pic_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_input\lara_lean.jpeg"
emoji_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\emojis\goblin.png"

coords_0=landmarks['left_eyebrow'][2][0]-distancex
coords_1=landmarks['left_eyebrow'][2][1]-distancey

coords=(coords_0, coords_1)

out_path=r"C:\Users\enpon\OneDrive - McGill University\Desktop\FS2024\codejam\delete-your-ex\backend\pictures_output\test5.jpeg"
sp.add_emoji_to_image(pic_path, emoji_path, coords, out_path, size)

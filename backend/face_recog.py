from PIL import Image, ImageDraw
import face_recognition 
from pathlib import Path

image_folder = Path(__file__).resolve().parent / "pictures"

image = face_recognition.load_image_file(image_folder / "lara_victoria.jpeg")
face_landmarks_list = face_recognition.face_landmarks(image)

face1 = face_landmarks_list[0]
face2 = face_landmarks_list[1]

print(face1)
print(face2)

################################################################

picture_of_me = face_recognition.load_image_file(image_folder / "nico.jpeg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file(image_folder / "enrique.jpeg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of nico!")

################################################################################################

picture_of_me = face_recognition.load_image_file(image_folder / "nico.jpeg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file(image_folder / "nico2.jpeg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of nico!")

#########################################################

picture_of_lara = face_recognition.load_image_file(image_folder / "enrique.jpeg")
lara_face_encoding = face_recognition.face_encodings(picture_of_lara)[0]

picture_of_paloma = face_recognition.load_image_file(image_folder / "paloma_con_nino.jpeg")
paloma_face_encoding = face_recognition.face_encodings(picture_of_paloma)[0]

results = face_recognition.compare_faces([lara_face_encoding],paloma_face_encoding)

if results[0] == True:
    print("It's a picture of lara!")
else:
    print("It's not a picture of lara!")
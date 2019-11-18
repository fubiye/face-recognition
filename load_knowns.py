import os
import face_recognition

def load():
    known_face_encodings= []
    known_face_names = []

    knowns_path = os.listdir("knowns/")
    for img_file in knowns_path:
        img_file_path = os.path.join('%s%s' % ("knowns/", img_file))
        print("Loading known imgs: " + img_file_path)
        face_name = os.path.splitext(img_file)[0]
        known_face_names.append(face_name)
        image = face_recognition.load_image_file(img_file_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        print("Encoded face:" + face_name)

    return known_face_encodings, known_face_names
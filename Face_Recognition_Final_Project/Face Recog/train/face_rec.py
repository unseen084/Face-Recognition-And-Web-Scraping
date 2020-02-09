import os
import threading

import face_recognition
import cv2
import datetime
import ui.ui as ui

only_detect = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")


def count_total_image_files():
    cnt = 0
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                cnt += 1

    return cnt


def load_and_encode_images():
    print(threading.currentThread())
    msg = ui.get_msg_setter()
    msg.set("Loading")
    known_face_encodings = []
    known_face_names = []

    total_image = str(count_total_image_files())
    msg.set(total_image + ' Images Found')
    cnt = 0
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                # label = os.path.basename(root)
                # print(label, path)
                msg.set(str(cnt) + " out of " + total_image + ' images Trained.\nNow Training image: ' + file)
                image = face_recognition.load_image_file(path)
                a = datetime.datetime.now()
                face_encoding = face_recognition.face_encodings(image)[0]
                print(datetime.datetime.now() - a)
                known_face_encodings.append(face_encoding)
                known_face_names.append(file.split(".")[0])
                cnt += 1
    msg.set(str(cnt) + " out of " + total_image + ' images Trained.')
    return known_face_encodings, known_face_names


def recognize(known_face_encodings, known_face_names, frame):
    if known_face_names is None:
        return None, None
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    name = ""

    small_frame = cv2.resize(frame, (0, 0), fx=0.20, fy=0.20)
    rgb_small_frame = small_frame[:, :, ::-1]



    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 5
        right *= 5
        bottom *= 5
        left *= 5

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    return frame, name

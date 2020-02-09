import threading

import train.face_rec as train
import cv2
import PIL.Image, PIL.ImageTk
import ui.ui as ui
import upload.upload as upload
import scrap.webScrap as scrap

info_string='Uploading and Fetching data from Web.. Please wait'
known_face_encodings = None
known_face_names = None

class ThreadHelper(threading.Thread):
    def run(self):
        global info_string
        uploaded_file_url = upload.upload_file()
        info = scrap.imageLookup(uploaded_file_url)
        print(info)
        info_string=info


def train_model():
    global known_face_encodings, known_face_names
    known_face_encodings, known_face_names = train.load_and_encode_images()


def save_still_image():
    frame = video_capture.read()[1]
    cv2.imwrite("tmp_image.png", frame)
    b, g, r = cv2.split(frame)
    frame = cv2.merge((r, g, b))
    ui.set_image(PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)))
    ui.set_msg("Uploading and Fetching data from Web.. Please wait")
    ui.hide_buttons()
    ThreadHelper().start()
    while ui.for_online_search:
        ui.update()
        ui.set_name(info_string, 'info')
    ui.show_buttons()


ui.load_ui(train_model, save_still_image)

video_capture = cv2.VideoCapture(0)


while True:
    ret, frame = video_capture.read()

    recognized_frame, name = train.recognize(known_face_encodings, known_face_names, frame)
    if recognized_frame is None:
        recognized_frame = frame
        ui.set_msg("Please Train the Model First")

    b, g, r = cv2.split(recognized_frame)
    recognized_frame = cv2.merge((r, g, b))
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(recognized_frame))

    ui.set_image(photo)
    if name is not None:
        ui.set_name(name, None)
    ui.update()

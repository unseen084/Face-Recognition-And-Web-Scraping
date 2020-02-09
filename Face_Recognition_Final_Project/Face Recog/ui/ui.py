import threading
from tkinter import *
canvas = None
root = None
name = None
msg = None
v = None
popup_canvas = None
save_still_image = None
recognize_button = None
local_button = None
train_button = None
for_online_search=False

def dismiss():
    global for_online_search
    for_online_search=False

def recognize_from_web():
    global for_online_search
    for_online_search = True
    save_still_image()

def load_ui(train_callback, save_still_image_callback):
    print(threading.currentThread())
    global name, root, msg, canvas, v, save_still_image, recognize_button, train_button, local_button
    save_still_image = save_still_image_callback
    root = Tk()
    v = StringVar()

    view_frame = Frame(root, width=500, height=500)
    view_frame.grid(row=0, column=0)

    canvas = Canvas(view_frame, width=600, height=500)
    canvas.grid(row=0, column=0, padx=10, pady=10)

    recognize_button = Button(view_frame, text="Recognize Face Online", width=25, height=3, command=recognize_from_web)
    recognize_button.grid(row=1, column=0)

    local_button = Button(view_frame, text="Back", width=25, height=3, command=dismiss)


    info_frame = Frame(root, width=500, height=500)
    info_frame.grid(row=0, column=1)

    train_button = Button(info_frame, text="Train Model", command=train_callback
                         , width=25, height=3)
    train_button.grid(row=0, column=0, padx=10, pady=10)

    name = Text(info_frame, width=50, height=10)
    name.grid(row=1, column=0, padx=10, pady=10)

    msg = Label(info_frame, width=50, height=10, textvariable=v)
    msg.grid(row=2, column=0, padx=10, pady=10)


def set_image(photo):
    global canvas
    canvas.create_image(0, 0, image=photo, anchor=NW)


def update():
    global root
    root.update_idletasks()
    root.update()


def set_name(n, info):
    global name
    name.delete(1.0, END)
    if info and info=='info':
        name.insert(INSERT, "Info: " + n)
    else:
        name.insert(INSERT, "Name: " + n)


def set_msg(text):
    global msg, v
    v.set(text)


def get_msg_setter():
    global v
    return v

def set_popup_image(photo):
    global popup_canvas
    popup_canvas.create_image(0, 0, image=photo, anchor=NW)

def hide_buttons():
    global recognize_button, train_button, local_button
    recognize_button.grid_forget()
    train_button.grid_forget()
    local_button.grid(row=1, column=0)

def show_buttons():
    global recognize_button, train_button, local_button
    local_button.grid_forget()
    recognize_button.grid(row=1, column=0)
    train_button.grid(row=0, column=0, padx=10, pady=10)


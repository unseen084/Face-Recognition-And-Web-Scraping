
import pyimgur

CLIENT_ID = 'b8de73761d59053'

def upload_file():
    import os

    PATH = os.path.abspath("tmp_image.png")

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="tmp")
    print(uploaded_image.title)
    print(uploaded_image.link)
    print(uploaded_image.size)
    print(uploaded_image.type)
    return uploaded_image.link

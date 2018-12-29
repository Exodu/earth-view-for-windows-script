from urllib import request
import random
# import ctypes
import os


def change_background():
    with open('images.txt', 'r') as images:
        links = images.readlines()
        url = random.choice(links)
        image = request.urlopen(url)

    with open('background.jpg', 'wb') as background:
        background.write(image.read())

    path = os.getcwd() + '/background.jpg'
    # ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)


change_background()

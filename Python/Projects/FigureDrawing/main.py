import time

import dearpygui.dearpygui as dpg
from PIL import Image
from time import *
import random
import glob
import threading
import os

dpg.create_context()
#dpg.enable_docking(dock_space=True)

NUM_IMAGES = 30
POSE_LENGTH = 180
MAIN_DIR = "C:\\Users\\jason\\Desktop\\Art\\Art Ref"
SUB_DIR = ["\\Female Fantasy pack\\", "\\sample pack new\\", "\\Veronica_Large\\"]
my_timer = POSE_LENGTH
viewed_images = 0
IMG_WIN = "Primary Window"
STOP_LOOP = False

def start():
    global my_timer
    while my_timer > 0 and not STOP_LOOP:
        my_timer -= 1
        time.sleep(1)

def stop():
    STOP_LOOP = True

def start_thread():
    t = threading.Thread(target=start)
    t.start()

def get_new_img():
    file_path = MAIN_DIR + SUB_DIR[random.randint(0, len(SUB_DIR) - 1)] + "*.jpg"
    images = glob.glob(file_path)
    random_image = random.choice(images)

    img = random_image

    new_img = Image.open(img)

    if new_img.width > new_img.height:
        out = new_img.rotate(90, expand=True)
        new_height = 1000
        new_width = new_height / out.height * out.width
        resized_img = out.resize((int(new_width), int(new_height)))
        resized_img.save(f'images/image.jpg')
    else:
        new_height = 1000
        new_width = new_height / new_img.height * new_img.width
        resized_img = new_img.resize((int(new_width), int(new_height)))
        resized_img.save(f'images/image.jpg')


get_new_img()
start_thread()

width, height, channels, data = dpg.load_image('images/image.jpg')

with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

with dpg.window(tag=IMG_WIN):
    dpg.add_image("texture_tag")

dpg.create_viewport(title='PyrPose - Figure Drawing Tool')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
dpg.set_primary_window(IMG_WIN, True)
dpg.start_dearpygui()
dpg.destroy_context()

import time

import dearpygui.dearpygui as dpg
from PIL import Image
from time import *
import random
import glob
import threading
import os

dpg.create_context()

NUM_IMAGES = 30
POSE_LENGTH = 10
MAIN_DIR = "C:\\Users\\jason\\Desktop\\Art\\Art Ref"
SUB_DIR = ["\\Female Fantasy pack\\", "\\sample pack new\\", "\\Veronica_Large\\"]
viewed_images = 0
IMG_WIN = "Primary Window"
STOP_LOOP = False
NEW_IMAGE = True


def draw_image():
    if dpg.does_item_exist("curr_image"):
        dpg.delete_item("curr_image")
    if dpg.does_item_exist(IMG_WIN):
        dpg.delete_item(IMG_WIN)

    get_new_img()

    width, height, channels, data = dpg.load_image('images/image.jpg')

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="curr_image")

    with dpg.window(tag=IMG_WIN):
        dpg.add_image("curr_image")


def timer():
    global my_timer
    my_timer = POSE_LENGTH
    while my_timer >= 0:
        if STOP_LOOP:
            break
        my_timer -= 1
        sleep(1)


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


draw_image()
t = threading.Thread(target=timer)
t.start()


dpg.create_viewport(title="PyrPose")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    if my_timer <= 0 and viewed_images <= NUM_IMAGES:
        my_timer = POSE_LENGTH
        viewed_images += 1
        print(viewed_images)
        draw_image()

    dpg.render_dearpygui_frame()

dpg.destroy_context()
STOP_LOOP = True

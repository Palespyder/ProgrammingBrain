import time

import dearpygui.dearpygui as dpg
from PIL import Image, ImageOps, ExifTags
from time import *
import random
import glob
import threading
import os

dpg.create_context()

# add a font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("Cinzel-Regular.ttf", 120)

NUM_IMAGES = 30
POSE_LENGTH = 180
MAIN_DIR = "C:\\Users\\jason\\Desktop\\Art\\Art Ref"
SUB_DIR = ["\\Female Fantasy pack\\", "\\Poses\\", "\\Sword fight\\", "\\Veronica_Large\\"]
viewed_images = 0
IMG_WIN = "Primary Window"
STOP_LOOP = False
NEW_IMAGE = True
images_used = []
image_width = None
image_height = None


def draw_image():
    if dpg.does_item_exist("curr_image"):
        dpg.delete_item("curr_image")
    if dpg.does_item_exist(IMG_WIN):
        dpg.delete_item(IMG_WIN)

    get_new_img()

    width, height, channels, data = dpg.load_image('images/image.jpg')

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="curr_image")

    with dpg.window(tag=IMG_WIN, width=width, height=height):
        dpg.add_image("curr_image")
        dpg.bind_font(default_font)


def timer():
    global my_timer
    my_timer = POSE_LENGTH
    while my_timer >= 0:
        if STOP_LOOP:
            break
        my_timer -= 1
        sleep(1)


def get_new_img():
    global image_width, image_height
    file_path = MAIN_DIR + SUB_DIR[random.randint(0, len(SUB_DIR) - 1)] + "*.jpg"
    images = glob.glob(file_path)
    random_image = random.choice(images)
    if random_image in images_used:
        get_new_img()
    else:
        images_used.append(random_image)
        print(random_image)

    new_img = Image.open(random_image)

    ImageOps.exif_transpose(new_img)

    if ExifTags.TAGS.keys() is not None:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = new_img._getexif()

        if exif[orientation] == 3:
            new_img = new_img.rotate(180, expand=True)
        elif exif[orientation] == 4:
            new_img = new_img.rotate(180, expand=True)
        elif exif[orientation] == 5:
            new_img = new_img.rotate(270, expand=True)
        elif exif[orientation] == 6:
            new_img = new_img.rotate(270, expand=True)
        elif exif[orientation] == 7:
            new_img = new_img.rotate(270, expand=True)
        elif exif[orientation] == 8:
            new_img = new_img.rotate(90, expand=True)

    new_height = 1000
    new_width = new_height / new_img.height * new_img.width
    resized_img = new_img.resize((int(new_width), int(new_height)))
    resized_img.save(f'images/image.jpg')

    image_width = resized_img.width
    image_height = resized_img.height


draw_image()
t = threading.Thread(target=timer)
t.start()

dpg.create_viewport(title="PyrPose")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
dpg.set_primary_window(IMG_WIN, True)
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    if my_timer <= 0 and viewed_images <= NUM_IMAGES:
        my_timer = POSE_LENGTH
        viewed_images += 1
        draw_image()
        dpg.set_primary_window("Primary Window", True)

    dpg.set_viewport_title(title="PyrPose - A Figure Drawing Tool for Me")

    if dpg.does_item_exist("counter"):
        dpg.delete_item("counter")
        dpg.draw_text((image_width + 200, 0), "Time Remaining: " + str(round(my_timer / 60, 2)), parent=IMG_WIN, size=120, tag="counter")
    else:
        dpg.draw_text((image_width + 200, 0), "Time Remaining: " + str(round(my_timer / 60, 2)), parent=IMG_WIN, size=120, tag="counter")

    dpg.render_dearpygui_frame()

dpg.destroy_context()
STOP_LOOP = True

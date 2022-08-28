import dearpygui.dearpygui as dpg
from PIL import Image
from time import *
import random
import threading
import os

dpg.create_context()
dpg.enable_docking(dock_space=True)

NUM_IMAGES = 30
POSE_LENGTH = 180
MAIN_DIR = "C:\\Users\\jason\\Desktop\\Art\\Art Ref"
SUB_DIR = ["\\Female Fantasy pack\\","\\Poses\\", "\\sample pack new\\", "\\Sword fight\\", "\\Veronica_Large\\"]

def img_timer():
    global my_timer
    global viewed_images
    my_timer = POSE_LENGTH

    for x in range(POSE_LENGTH):
        my_timer -= 1
        sleep(1)
    viewed_images += 1
    if viewed_images <= NUM_IMAGES:
        get_new_img()


def get_new_img()




img = "C:\\Users\\jason\\Desktop\\Art\\Art Ref\\Poses\\IMG_0065.JPG"


new_img = Image.open(img)

if new_img.width > new_img.height:
    out = new_img.rotate(90, expand=True)
    new_height = 1000
    new_width = new_height / out.height * out.width
    resized_img = out.resize((int(new_width), int(new_height)))
    resized_img.save(f'images/image.jpg')
    width, height, channels, data = dpg.load_image('images/image.jpg')
else:
    new_height = 1000
    new_width = new_height / new_img.height * new_img.width
    resized_img = new_img.resize((int(new_width), int(new_height)))
    resized_img.save(f'images/image.jpg')
    width, height, channels, data = dpg.load_image('images/image.jpg')


with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

with dpg.window(tag="Primary Window"):
    dpg.add_image("texture_tag")

dpg.create_viewport(title='PyrPose - Figure Drawing Tool', width=int(new_width), height=int(new_height))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
#dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

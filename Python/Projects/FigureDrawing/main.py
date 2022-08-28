import dearpygui.dearpygui as dpg
from PIL import Image
import os

dpg.create_context()
#dpg.enable_docking(dock_space=True)


img = "C:\\Users\\jason\\Desktop\\Art\\Art Ref\\sample pack new\\0A2A1731.JPG"


new_img = Image.open(img)
new_height = 1000
new_width = new_height / new_img.height * new_img.width
resized_img = new_img.resize((int(new_width), int(new_height)))

if new_width > new_height:
    out = resized_img.rotate(90, expand=True)
    out.save('images/image.jpg')
    width, height, channels, data = dpg.load_image('images/image.jpg')
else:
    out.save('images/image.jpg')
    width, height, channels, data = dpg.load_image('images/image.jpg')


with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

with dpg.window(tag="Primary Window"):
    dpg.add_image("texture_tag")

dpg.create_viewport(title='PyrPose - Figure Drawing Tool', width=int(new_width), height=int(new_height))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

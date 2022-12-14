import dearpygui.dearpygui as dpg
from PIL import Image, ImageOps, ExifTags
from time import *
import random
import glob
import threading
import os

dpg.create_context()

from theme_settings import *

class App:
    def __init__(self):
        self.interval = 30
        self.pose_length = 180
        self.time = 0
        self.stop_loop = False
        self.main_dir = "C:\\Users\\jason\\Desktop\\Art\\Art Ref"
        self.sub_dir = ["\\Female Fantasy pack\\", "\\Poses\\", "\\Sword fight\\", "\\Veronica_Large\\"]
        self.images_used = []

    def timer(self):
        self.time = self.pose_length
        while self.time >= 0:
            if self.stop_loop:
                break
            self.time -= 1
            sleep(1)

    def get_new_img(self):
        file_path = self.main_dir + self.sub_dir[random.randint(0, len(self.sub_dir) - 1)] + "*.jpg"
        images = glob.glob(file_path)
        random_image = random.choice(images)
        if random_image in self.images_used:
            self.get_new_img()
        else:
            self.images_used.append(random_image)

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

        new_height = 900
        new_width = new_height / new_img.height * new_img.width
        resized_img = new_img.resize((int(new_width), int(new_height)))
        resized_img.save(f'images/image.jpg')

        image_width = resized_img.width
        image_height = resized_img.height

    def main_window_setup(self):
        dpg.create_viewport(title="PyPose Figure Drawing Tool", x_pos=0, y_pos=0, width=1920, height=1080)
        dpg.set_viewport_max_height(1080)
        dpg.set_viewport_max_width(1920)

        with dpg.window(pos=[0, 0], autosize=True, no_collapse=True, no_resize=True, no_close=True, no_move=True,
                        no_title_bar=True) as main_window:
            with dpg.child_window(height=90, autosize_x=True):
                with dpg.group(horizontal=True):
                    score_text = dpg.add_text(default_value=" Time Remaining : ")
                    score = dpg.add_text(default_value=self.time)

                dpg.bind_item_font(item=score_text, font=timer_font)
                dpg.bind_item_font(item=score, font=timer_font)

                with dpg.group(horizontal=True):
                    highest_score_text = dpg.add_text(default_value=" Image Number : ")
                    highest_score = dpg.add_text(default_value="0")

                dpg.bind_item_font(item=highest_score_text, font=regular_font)
                dpg.bind_item_font(item=highest_score, font=regular_font)

            with dpg.group(horizontal=True):
                with dpg.group():
                    with dpg.plot(no_menus=False, no_title=True, no_box_select=True, no_mouse_pos=True, width=1200,
                                  height=900, equal_aspects=True) as snake_burrow:
                        default_x = dpg.add_plot_axis(axis=0, no_gridlines=True, no_tick_marks=True,
                                                      no_tick_labels=True,
                                                      label="", lock_min=True)
                        dpg.set_axis_limits(axis=default_x, ymin=0, ymax=50)
                        default_y = dpg.add_plot_axis(axis=1, no_gridlines=True, no_tick_marks=True,
                                                      no_tick_labels=True,
                                                      label="", lock_min=True)
                        dpg.set_axis_limits(axis=default_y, ymin=0, ymax=50)

                with dpg.child_window(autosize_x=True, autosize_y=True):
                    with dpg.group():
                        with dpg.child_window(height=640):
                            dpg.add_spacer(height=5)
                            settings_text = dpg.add_text(default_value=" Settings")
                            dpg.bind_item_font(item=settings_text, font=bold_font)
                            dpg.add_spacer(height=5)
                            dpg.add_separator()
                            dpg.add_spacer(height=5)

                            clothing_text = dpg.add_text(default_value=" Cover and Clothing:")
                            dpg.bind_item_font(item=clothing_text, font=bold_font)
                            dpg.add_spacer(height=5)
                            clothing =dpg.add_radio_button(items=("All Models", "Only Nude Models", "Only Clothed Models"),
                                                           label="Cover and Clothing",
                                                           horizontal=True)


                            dpg.add_spacer(height=15)

                            gender_text = dpg.add_text(default_value=" Gender:")
                            dpg.bind_item_font(item=gender_text, font=bold_font)
                            dpg.add_spacer(height=5)

                            gender = dpg.add_radio_button(
                                items=("Both", "Only Female Models", "Only Male Models"),
                                label="Gender",
                                horizontal=True)

                            dpg.add_spacer(height=15)
                            interval_text = dpg.add_text(default_value=" Time Interval:")
                            dpg.bind_item_font(item=interval_text, font=bold_font)
                            dpg.add_spacer(height=5)

                            interval = dpg.add_radio_button(
                                    items=("30 Seconds", "60 Seconds", "2 Minutes", "5 Minutes", "10 Minutes", "20 Minutes"),
                                    label="Time Interval",
                                    horizontal=False,
                                    callback=self.set_interval)


                        dpg.add_separator()
                        dpg.add_spacer()
                        dpg.add_button(label="Start", width=-1, height=30)
                        dpg.add_button(label="Pause", width=-1, height=30)
                        with dpg.group(horizontal=True, width=350):
                            dpg.add_button(label="Previous Image", height=30)
                            dpg.add_button(label="Next Image", height=30)
                        dpg.add_spacer()
                        dpg.add_separator()
                        dpg.add_spacer()
                        dpg.add_button(label="Help", width=-1, height=30)

        key_release_handler_parent = dpg.add_handler_registry()
        dpg.add_key_release_handler(parent=key_release_handler_parent)

        dpg.bind_theme(global_theme)
        dpg.bind_font(regular_font)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.maximize_viewport()
        dpg.set_primary_window(window=main_window, value=True)
        dpg.start_dearpygui()
        dpg.destroy_context()

    def set_interval(self, sender, app_data):
        if app_data == "30 Secondss":
            self.interval = 30
        elif app_data == "60 Seconds":
            self.interval = 60
        elif app_data == "2 Minutes":
            self.interval = 2 * 60
        elif app_data == "5 Minutes":
            self.interval = 5 * 60
        elif app_data == "10 Minutes":
            self.interval = 10 * 60
        elif app_data == "20 Minutes":
            self.interval = 20 * 60

    # Function to update Image.


    def run(self):
        self.main_window_setup()


if __name__ == '__main__':
    app = App()
    app.run()
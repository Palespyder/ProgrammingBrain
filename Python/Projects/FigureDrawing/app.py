import dearpygui.dearpygui as dpg

dpg.create_context()

from theme_settings import *

class App:
    def __init__(self):
        pass

    def main_window_setup(self):
        dpg.create_viewport(title="PyPose Figure Drawing Tool", x_pos=0, y_pos=0, width=1920, height=1080)
        dpg.set_viewport_max_height(1080)
        dpg.set_viewport_max_width(1920)

        with dpg.window(pos=[0, 0], autosize=True, no_collapse=True, no_resize=True, no_close=True, no_move=True,
                        no_title_bar=True) as main_window:
            with dpg.child_window(height=90, autosize_x=True):
                with dpg.group(horizontal=True):
                    score_text = dpg.add_text(default_value=" Time Remaining : ")
                    score = dpg.add_text(default_value="0")

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

                            age_text = dpg.add_text(default_value=" Ages:")
                            dpg.bind_item_font(item=age_text, font=bold_font)
                            dpg.add_spacer(height=5)

                            with dpg.group(horizontal=True):
                                dpg.add_spacer(height=15)
                                add_baby = dpg.add_checkbox(label="Baby", default_value=False)
                                add_child = dpg.add_checkbox(label="Child", default_value=False)
                                add_teen = dpg.add_checkbox(label="Teen", default_value=False)
                                add_adult = dpg.add_checkbox(label="Adult", default_value=True)

                            dpg.add_spacer(height=15)

                            class_type_text = dpg.add_text(default_value=" Session Type:")
                            dpg.bind_item_font(item=class_type_text, font=bold_font)
                            dpg.add_spacer(height=5)
                            item_list = ["All the same length", "Class Mode"]
                            session_type = dpg.add_radio_button(
                                items=item_list,
                                label="Session Type",
                                horizontal=True)

                            dpg.add_spacer(height=15)
                            interval_text = dpg.add_text(default_value=" Time Interval:")
                            dpg.bind_item_font(item=interval_text, font=bold_font)
                            dpg.add_spacer(height=5)

                            interval = dpg.add_radio_button(
                                items=("30 Seconds", "60 Seconds", "2 Minutes", "5 Minutes", "10 Minutes"),
                                label="Time Interval",
                                horizontal=False)


                            dpg.add_spacer(height=15)
                            dpg.add_button(label="Reset Settings", width=-1, height=30)

                        dpg.add_separator()
                        dpg.add_spacer()
                        dpg.add_button(label="Start", width=-1, height=30)
                        dpg.add_button(label="Restart", width=-1, height=30)
                        dpg.add_button(label="Reset Stats", width=-1, height=30)
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


    def run(self):
        self.main_window_setup()


if __name__ == '__main__':
    app = App()
    app.run()
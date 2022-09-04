import dearpygui.dearpygui as dpg

dpg.create_context()

from theme_settings import *


def main_window_setup():

    dpg.create_viewport(title="Implementation Toolkit", x_pos=0, y_pos=0, width=1920, height=1080)
    dpg.set_viewport_max_height(1080)
    dpg.set_viewport_max_width(1920)

    with dpg.window(pos=[0, 0], autosize=True, no_collapse=True, no_resize=True, no_close=True, no_move=True,
                    no_title_bar=True) as main_window:
        with dpg.child_window(height=90, autosize_x=True):
            with dpg.group(horizontal=True):
                score_text = dpg.add_text(default_value=" Score : ")
                score = dpg.add_text(default_value="0")

            dpg.bind_item_font(item=score_text, font=regular_font)
            dpg.bind_item_font(item=score, font=regular_font)

            with dpg.group(horizontal=True):
                highest_score_text = dpg.add_text(default_value=" Highest score : ")
                highest_score = dpg.add_text(default_value="0")

            dpg.bind_item_font(item=highest_score_text, font=regular_font)
            dpg.bind_item_font(item=highest_score, font=regular_font)

        with dpg.group(horizontal=True):
            with dpg.group():
                with dpg.plot(no_menus=False, no_title=True, no_box_select=True, no_mouse_pos=True, width=1500,
                              height=900, equal_aspects=True) as snake_burrow:
                    default_x = dpg.add_plot_axis(axis=0, no_gridlines=True, no_tick_marks=True, no_tick_labels=True,
                                                  label="", lock_min=True)
                    dpg.set_axis_limits(axis=default_x, ymin=0, ymax=50)
                    default_y = dpg.add_plot_axis(axis=1, no_gridlines=True, no_tick_marks=True, no_tick_labels=True,
                                                  label="", lock_min=True)
                    dpg.set_axis_limits(axis=default_y, ymin=0, ymax=50)



            with dpg.child_window(autosize_x=True, autosize_y=True):
                with dpg.group():
                    with dpg.child_window(height=340):
                        dpg.add_spacer(height=5)
                        settings_text = dpg.add_text(default_value=" Settings")
                        dpg.bind_item_font(item=settings_text, font=bold_font)
                        dpg.add_spacer(height=5)
                        dpg.add_separator()
                        dpg.add_spacer(height=5)
                        snake_speed = dpg.add_drag_int(label="Snake speed", width=130, clamped=True, min_value=1,
                                                       max_value=10, default_value=5)
                        dpg.add_spacer(height=15)
                        snake_color = dpg.add_color_edit(label="Snake color", default_value=[0, 255, 0], no_alpha=True,
                                                         width=130)
                        dpg.add_spacer(height=5)
                        apple_color = dpg.add_color_edit(label="Apple color", default_value=[255, 0, 0], no_alpha=True,
                                                         width=130)
                        dpg.add_spacer(height=5)
                        burrow_color = dpg.add_color_edit(label="Burrow color", default_value=[33, 33, 33],
                                                          no_alpha=True, width=130)
                        dpg.add_spacer(height=15)
                        fix_snake_length = dpg.add_checkbox(label="Fix snake length", default_value=False
                                                            )
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
    dpg.add_key_release_handler( parent=key_release_handler_parent)

    dpg.bind_theme(global_theme)
    dpg.bind_font(regular_font)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.set_primary_window(window=main_window, value=True)
    dpg.start_dearpygui()
    dpg.destroy_context()


main_window_setup()
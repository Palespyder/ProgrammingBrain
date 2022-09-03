import dearpygui.dearpygui as dpg

with dpg.font_registry() as main_font_registry:
    regular_font = dpg.add_font('fonts/Cinzel/Cinzel-Regular.ttf', 16)
    bold_font = dpg.add_font('fonts/Cinzel/Cinzel-Medium.ttf', 21)
from dearpygui.core import *
from dearpygui.simple import *
from Stores import Stores
import products_db
display_button = False

def add_item_url():
    print(get_value("Input"))
    with window("Py_Bot"):
        add_button("Run Bot", callback=run_bot)

def run_bot():
    for i in products_db.gpu_list:
        if i.store == 'Amazon':
            with window("Py_Bot"):
                add_text(Stores.amazon_buy(i))

# window object
set_main_window_size(540,720)
set_global_font_scale(1.25)
set_theme("Dark")

with window("Py_Bot", width=520, height=677):
    set_window_pos("Py_Bot", 0,0)
    add_text("Paste in URLs for item you are looking for")
    add_input_text("Input", width=415, default_value="add url")
    add_button("Add",callback=add_item_url)
        

start_dearpygui()
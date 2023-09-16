from src.bot import DSBot
#from src.commands import set_commands

import discord

import os

from PIL import ImageGrab

def try_mkdir(path_: str):
    if not os.path.exists(path_):
        os.mkdir(path_)
try_mkdir("data_cartas")


def take_screenshot(
        path_save: str,
        x_l: int,
        y_l: int,
        x_r: int,
        y_r: int):
    screenshot = ImageGrab.grab(bbox = (x_l, y_l, x_r, y_r))
    screenshot.save(path_save)

#if __name__ == "__main__":
intents = discord.Intents.default()
intents.message_content = True
bot = DSBot(command_prefix = '!', intents = intents)

import threading
from pynput import keyboard
from datetime import datetime

def on_press(key):
    try:
        if key == keyboard.Key.print_screen:
            id_canal = 1128816226089570355
            p_1_1 = (3265, 150)
            p_1_2 = (3800, 1000)
            p_2_1 = (120, 165)
            p_2_2 = (800, 890)

            t = str(datetime.now().timestamp()).replace(".","_")
            path_out = os.path.join("data_cartas", t)
            try_mkdir(path_out)

            path_out_1 = os.path.join(path_out, f"{t}_carta.png")
            path_out_2 = os.path.join(path_out, f"{t}_ruleta.png")
            take_screenshot(path_out_1, *p_1_1, *p_1_2)
            take_screenshot(path_out_2, *p_2_1, *p_2_2)

            print("antes de tocar")
            file_1 = discord.File(path_out_1)
            file_2 = discord.File(path_out_2)
            bot.loop.create_task(bot.get_channel(id_canal).send(files=[file_1, file_2]))
            print("despues de tocar")
    except AttributeError:
        print("error")

def listen_for_key_press():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Crear un hilo aparte para ejecutar el proceso
key_press_thread = threading.Thread(target=listen_for_key_press)
key_press_thread.start()

print("llega aca")
#set_commands(bot)
bot.run(os.getenv("TOKEN_DS"))
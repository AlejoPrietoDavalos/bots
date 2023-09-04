import pyautogui as p
from pynput import keyboard as kb
from PIL import ImageGrab

import time


class Bot():
    def __init__(self):
        self.n_points = 0
        self.points = []
        self.point_button = ()
        self.start = False

    def get_mouse_position(self) -> tuple:
        return p.position()

    def move(self, pos:tuple):
        p.moveTo(pos[0], pos[1])

    def click(self):
        p.click()
    
    def add_point(self, point:tuple):
        if self.n_points == 1 and self.points[0][0]>point[0]:
            self.points.insert(0, point)
        else:
            self.points.append(point)
        self.n_points += 1
    
    def add_point_button(self, point:tuple):
        self.point_button = point

bot = Bot()



def when_key_pressed(_key):
    if _key == kb.KeyCode.from_char('p') and bot.n_points<2:
        bot.add_point(bot.get_mouse_position())

    if _key == kb.KeyCode.from_char('s') and not bot.start and bot.n_points==2:
        bot.start = True
        bot.add_point_button(bot.get_mouse_position())

        
        for i in range(200):
            bot.move(bot.point_button)
            bot.click()
            time.sleep(0.3)

            screenshot = ImageGrab.grab(
            bbox=(
                bot.points[0][0],
                bot.points[0][1],
                bot.points[1][0],
                bot.points[1][1]
            ))
            screenshot.save(f"{i+1}.png")

        
        
        bot.start = False
        bot.n_points = 0
        bot.points = []
        bot.point_button = ()
        


with kb.Listener(when_key_pressed) as escuchador:
    escuchador.join()


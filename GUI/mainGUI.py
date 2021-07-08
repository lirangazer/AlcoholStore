"""
this is the GUI impalement gui
"""
import sys
import tkinter
from tkinter import *
from common.root_logger import *
import os
import subprocess
from GUI.login_window import *
from picture import *

try:
    from pillow import *
    from PIL import Image
    from PIL import ImageTk
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    # from pillow import *
    from PIL import Image
    from PIL import ImageTk

PROJECT = ""


def add_to_basket():
    print('success')


class AlcoholStore():
    def __init__(self, main_window, title, window_geo, icon=None):
        setup_logger(title, print_to_screen=False)
        self.main_window = main_window
        self.main_window.title(title)
        self.main_window.geometry(window_geo)

        global PROJECT
        PROJECT = title
        self.frame = []
        self.buttons = []
        self.products_name = []
        self.products_pic = []
        self.init_frame()
        self.init_buttons()
        self.init_pic()

    def init_frame(self):
        for i in range(3):
            self.frame.append(Frame(self.main_window, height=70, width=400, pady=15, padx=15))
        self.frame[0].grid(row=0, column=0)
        self.frame[1].grid(row=0, column=1)
        self.frame[2].grid(row=1, column=0, columnspan=3)

    def init_buttons(self):
        buttons_name = ['Purchase', 'Cancel', 'Edit', 'Exit']
        for i in range(len(buttons_name)):
            self.buttons.append(Button(self.frame[2], text=buttons_name[i], padx=20, pady=15,
                                       command=lambda i=i: self.buttons_action(i)))
        self.buttons[0].grid(row=0, column=0, padx=20, pady=15)
        self.buttons[1].grid(row=0, column=1)
        self.buttons[2].grid(row=0, column=2)
        self.buttons[3].grid(row=0, column=3)

    def init_pic(self):
        picture_path = {'Red Label': r"picture\redlabel.png", 'Glenfiddich': r"picture/glenfiddich.png", 'Grey Goose': 'picture/grey goose.png'}
        i = 0
        for (k, v) in picture_path.items():
            tmp = Image.open(v)
            tmp1 = tmp.resize((100, 100), Image.ANTIALIAS)
            tmp2 = ImageTk.PhotoImage(tmp1)
            self.products_pic.append(Button(self.frame[0], image=tmp2, padx=20, pady=15, command=add_to_basket))
            self.products_name.append(Label(self.frame[0], text=k))
            self.products_pic[i].image = tmp2
            i += 1
        for j in range(len(self.products_pic)):
            self.products_pic[j].grid(row=0, column=j, padx=5)
            self.products_name[j].grid(row=1, column=j)

    def button_action(self, index):
        """
        :param index: Index of the pressed button.
        """
        #file_parser = filesParse()
        if index == 0:
          pass
        if index == 4:
            self.main_window.destory()





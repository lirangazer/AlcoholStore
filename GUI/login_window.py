"""
this is gui  login page to the system
"""
import time
from tkinter import *
from functools import partial
from GUI.mainGUI import *
from common.root_logger import *


class login_window():
    def __init__(self, root, title, window_geo, icon=None):
        self.logger = get_logger()
        self.root = root
        self.root.title(title)
        self.root.geometry(window_geo)
        self.username_verify = StringVar()
        self.password_verify = StringVar()
        # Label(self.root, text='User Name').grid(row=0, column=0)
        # username = StringVar()
        # Entry(self.root, textvariable=username).grid(row=0, column=1)
        # Label(self.root, text='Password').grid(row=1, column=0)
        # password = StringVar()
        # Entry(self.root, textvariable=password, show='*').grid(row=1, column=1)
        self.init_login()

    def init_login(self):
        user_label = Label(self.root, text='User Name').grid(row=0, column=0)
        username_verify = self.username_verify
        usr_entry = Entry(self.root, textvariable=username_verify).grid(row=0, column=1)
        password_label = Label(self.root, text='Password').grid(row=1, column=0)
        password_verify = self.password_verify
        password_entry = Entry(self.root, textvariable=password_verify, show='*').grid(row=1, column=1)
        bnt = Button(self.root, text='Login', width=10, height=1, command = self.login_verify).grid(row=2, column=1)


    def login_verify(self):
        username = self.username_verify.get().lower()
        password = self.password_verify.get()
        authentication = {'liran': '123', 'whibe': '123'}
        for key, value in authentication.items():
            if key == username:
                if value == password:
                    newroot=Toplevel()
                    AlcoholStore(newroot, 'Alcohol Store', '1000x1000')
                    Label(self.root, text='success', fg='green', font=("calibri", 12)).grid(row=3, column=1)
                    self.root.withdraw()
                    newroot.mainloop()
                    self.root.destroy()
            else:
                Label(self.root, text='login failed ', fg='red', font=("calibri", 12)).grid(row=3, column=1)






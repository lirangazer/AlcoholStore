"""
this is gui  login page to the system
"""
import time
from tkinter import *
from functools import partial
from GUI.mainGUI import *
from common.root_logger import *


class login_window():
    """
    this class define the login window
    """
    def __init__(self, root, title, window_geo, icon=None):
        self.logger = get_logger()
        self.root = root
        self.root.title(title)
        self.root.geometry(window_geo)
        self.username_verify = StringVar()
        self.password_verify = StringVar()
        self.items = []
        self.label_message = None
        self.authentication = {'liran': '123', 'whibe': '123'}
        self.init_login()

    def init_login(self):
        """
        initialize the login screen with the widget
        :return:
        """
        self.items.append(Label(self.root, text='User Name').grid(row=0, column=0))
        username_verify = self.username_verify
        self.items.append(Entry(self.root, textvariable=username_verify).grid(row=0, column=1))
        self.items.append(Label(self.root, text='Password').grid(row=1, column=0))
        password_verify = self.password_verify
        self.label_message = Label(self.root).grid(row=3, column=0)
        self.items.append(Entry(self.root, textvariable=password_verify, show='*').grid(row=1, column=1))
        self.items.append(Entry(self.root, textvariable=password_verify, show='*').grid(row=1, column=1))
        bnt = Button(self.root, text='Login', width=10, height=1, command = self.login_verify).grid(row=2, column=0 ,padx=15)
        bnt = Button(self.root, text='Register', width=10, height=1, command = self.register).grid(row=2, column=1)


    def login_verify(self):
        """
        this function verify the login user
        :return:
        """
        username = self.username_verify.get().lower()
        password = self.password_verify.get()
        
        for key, value in self.authentication.items():
            if key == username:
                if value == password:
                    # Label(self.root, text='success', fg='green', font=("calibri", 12)).grid(row=3, column=1)
                    mainStore(self.root)

            else:
                Label(self.root, text='login failed ', fg='red', font=("calibri", 12)).grid(row=3, column=1)

    def register(self):
        """
        this function used for register new user
        :return:
        """
        username = self.username_verify.get()
        password = self.password_verify.get()
        flag = 0
        for(k,v) in self.authentication.items():
            if k is not username:

                flag = 1

            else:
                continue
        if flag == 0:
            messagebox.showerror('Error', 'user is already exits please check again')

        elif flag == 1:
            self.authentication[username] = password
            messagebox.showinfo('Thanks', 'Thanks for register')









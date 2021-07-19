from tkinter import *
from tkinter import messagebox
from store.supplier import *


class NewSupplierWindow():
    def __init__(self, root, title, window_geo, parent, icon=None):
        self.root = root
        self.root.title(title)
        self.root.geometry(window_geo)
        self.parent = parent
        self.frame = []
        self.init_frame()
        self.init_window()

    def init_frame(self):
        for i in range(3):
            self.frame.append(Frame(self.root, height=100, width=300))
        self.frame[0].grid(row=0, column=0)
        self.frame[1].grid(row=1, column=0)
        self.frame[2].grid(row=2, column=0)

    def init_window(self):
        Label(self.frame[0], text="Please insert the new amount you want to buy:",bg='cyan',font=("calibri", 12)).grid(row=0, column=0)
        Label(self.frame[1], text='amount').grid(row=0, column=0)
        amount = StringVar()
        name_entry = Entry(self.frame[1], textvariable=amount).grid(row=0, column=1)
        Button(self.frame[1], text='Save', command=lambda i=0: self.return_amount(amount)).grid(row=2, column=1)
        Button(self.frame[1], text='Cancel', height=1, width=7, command=lambda i=1: self.cancel()).grid(row=2, column=2,
                                                                                                        pady=5)

    def return_amount(self, amount):
        pass

    def cancel(self):
        pass

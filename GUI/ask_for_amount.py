from tkinter import *
from tkinter import messagebox
from store.supplier import *


class AskForAmount():
    def __init__(self, root, title, window_geo, parent,amount, icon=None):
        self.root = root
        self.root.title(title)
        self.root.geometry(window_geo)
        self.parent = parent
        self.amount=amount
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
        amount_entry = StringVar()
        name_entry = Entry(self.frame[1], textvariable=amount_entry).grid(row=0, column=1)
        amount_text = 'Total amount: ' + self.amount
        Label(self.frame[1], text=amount_text).grid(row=0, column=2)
        Button(self.frame[2], text='Save', command=lambda i=0: self.return_amount(amount_entry)).grid(row=2, column=1)
        Button(self.frame[2], text='Cancel', height=1, width=7, command=lambda i=1: self.cancel()).grid(row=2, column=2,
                                                                                                        pady=5)

    def return_amount(self, amount_entry):
        self.parent.amount = amount_entry.get()
        self.root.destroy()
        # if amount_entry.get() <= self.amount:
        #     self.parent.amount = amount_entry.get()
        #     self.root.destroy()
        # else:
        #     Label(self.frame[2], text='This amount is invalid please enter lower amount.', fg='red').grid(row=3, column=1)


    def cancel(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

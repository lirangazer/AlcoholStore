from tkinter import *
from tkinter import messagebox
from store.buyer import *


class NewBuyerWindow():
    """
    this class define new user that add from GUI
    """
    def __init__(self, root, title, window_geo, parent):
        self.root = root
        self.root.title(title)
        self.root.geometry(window_geo)
        self.parent = parent
        self.frame = []
        self.init_frame()
        self.init_window()


    def init_frame(self):
        """
        this function initialized the window Frames
        :return:
        """
        for i in range(3):
            self.frame.append(Frame(self.root, height=100, width=300))
        self.frame[0].grid(row=0, column=0)
        self.frame[1].grid(row=1, column=0)
        self.frame[2].grid(row=2, column=0)

    def init_window(self):
        """
               this function initialized the window Widget
               :return:
               """
        Label(self.frame[0], text="Please insert the new Buyer details", bg='cyan', font=("calibri", 12)).grid(row=0,
                                                                                                               column=0,
                                                                                                               pady=10)
        Label(self.frame[1], text='Name').grid(row=0, column=0)
        name = StringVar()
        name_entry = Entry(self.frame[1], textvariable=name).grid(row=0, column=1)
        Label(self.frame[1], text='ID').grid(row=1, column=0)
        id_buyer = StringVar()
        id_entry = Entry(self.frame[1], textvariable=id_buyer).grid(row=1, column=1)
        Label(self.frame[1], text='Phone').grid(row=2, column=0)
        phone = StringVar()
        phone_entry = Entry(self.frame[1], textvariable=phone).grid(row=2, column=1)
        Label(self.frame[1], text='Age').grid(row=3, column=0)
        age = StringVar()
        age_entry = Entry(self.frame[1], textvariable=age).grid(row=3, column=1)

        Button(self.frame[1], text='Save', height=1, width=7,
               command=lambda i=0: self.return_buyer(name, id_buyer, phone, age)).grid(row=5, column=1)
        Button(self.frame[1], text='Cancel', height=1, width=7, command=lambda i=1: self.cancel()).grid(row=5, column=2,
                                                                                                        pady=5)


    def return_buyer(self, name_entry, id_entry, phone_entry, age_entry):
        """
        this function return the new buyer to main window
        :param name_entry: user name that enter from gui
        :param id_entry: id that enter from GUI
        :param phone_entry: phone that enter from GUI
        :param age_entry: age that enter from GUI
        :return:
        """
        try:
            new_buyer = Buyer(name_entry.get(), id_entry.get(), phone_entry.get(), age_entry.get())
            for i in range(len(self.parent.buyers_names)):
                if new_buyer not in self.parent.buyers:
                    self.parent.buyers.append(new_buyer)
                    self.parent.init_buyer_frame(new_buyer)

            self.root.destroy()
        except TclError:
            Label(self.frame[2], text="Wrong ID ,Phone or Age please enter a number", fg='red',
                  font=("calibri", 12)).grid(row=1, column=0)
            phone_entry.set(0)
            name_entry.set('')
            age_entry.set(0)
            id_entry.set(0)

        # print(new_buyer.name)

    #
    def cancel(self):
        """
        this function use for the cancel button and destroy the window
        :return:
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()




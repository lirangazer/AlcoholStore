from tkinter import *
from store.buyer import *


class NewBuyerWindow():
    def __init__(self, root, title, window_geo, parent, icon=None):
        self.root = root
        self.root.title(title)
        self.root.geometry(window_geo)
        self.parent = parent
        self.init_window()

    def init_window(self):
        Label(self.root, text="Please insert the new Buyer details").grid(row=0, column=0)
        Label(self.root, text='Name').grid(row=1, column=0)
        name = StringVar()
        name_entry = Entry(self.root, textvariable=name).grid(row=1, column=1)
        Label(self.root, text='ID').grid(row=2, column=0)
        id_buyer = IntVar()
        id_entry = Entry(self.root, textvariable=id_buyer).grid(row=2, column=1)
        Label(self.root, text='Phone').grid(row=3, column=0)
        phone = IntVar()
        phone_entry = Entry(self.root, textvariable=phone).grid(row=3, column=1)
        Label(self.root, text='Age').grid(row=4, column=0)
        age = IntVar()
        age_entry = Entry(self.root, textvariable=IntVar()).grid(row=4, column=1)
        Button(self.root, text='Save', command=lambda i=0: self.return_buyer(name.get(), id_buyer.get(), phone.get(), age.get())).grid(row=5, column=0)
        #Button(self.root, text='Save', command=return_buyer(name.get(), id_buyer.get(), phone.get(), age.get(),self.parent)).grid(row=5, column=0)

    def return_buyer(self, name_entry, id_entry, phone_entry, age_entry):
        new_buyer = Buyer(name_entry, id_entry, phone_entry, age_entry)
        #print(new_buyer.name)
        self.parent.append(new_buyer)
        #print(self.parent)
        self.root.destroy()
        #self.root.update()
# def return_buyer(name_entry, id_entry, phone_entry, age_entry,parent):
#         new_buyer = Buyer(name_entry, id_entry, phone_entry, age_entry)
#         print(name_entry)
#         parent.append(new_buyer)





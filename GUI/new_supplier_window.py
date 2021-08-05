from tkinter import *
from tkinter import messagebox
from store.supplier import *


class NewSupplierWindow():
    """
    this class use for implement of adding new supplier
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
        this function initialized the frames
        :return:
        """
        for i in range(3):
            self.frame.append(Frame(self.root, height=100, width=300))
        self.frame[0].grid(row=0, column=0)
        self.frame[1].grid(row=1, column=0)
        self.frame[2].grid(row=2, column=0)

    def init_window(self):
        """
        this function initialized the window widget
        :return:
        """
        Label(self.frame[0], text="Please insert the new Supplier details", bg='cyan', font=("calibri", 12)).grid(row=0, column=0)
        Label(self.frame[1], text='Name').grid(row=0, column=0)
        name = StringVar()
        name_entry = Entry(self.frame[1], textvariable=name).grid(row=0, column=1)
        Label(self.frame[1], text='ID').grid(row=1, column=0)
        id_buyer = StringVar()
        id_entry = Entry(self.frame[1], textvariable=id_buyer).grid(row=1, column=1)
        Label(self.frame[1], text='Phone').grid(row=2, column=0)
        phone = StringVar()
        phone_entry = Entry(self.frame[1], textvariable=phone).grid(row=2, column=1)
        Label(self.frame[1], text='Address').grid(row=3, column=0)
        address = StringVar()
        address_entry = Entry(self.frame[1], textvariable=address).grid(row=3, column=1)
        Button(self.frame[1], text='Save', command=lambda i=0: self.return_supplier(name, id_buyer, phone, address)).grid(row=5, column=1)
        Button(self.frame[1], text='Cancel', height=1, width=7, command=lambda i=1: self.cancel()).grid(row=5, column=2,
                                                                                                        pady=5)

    def return_supplier(self, name_entry, id_entry, phone_entry, address_entry):
        """
        this function return the new supplier details
        :param name_entry:
        :param id_entry:
        :param phone_entry:
        :param address_entry:
        :return:
        """
        try:
            new_supplier = Supplier(name_entry.get(), address_entry.get(), id_entry.get(), phone_entry.get())
            for i in range(len(self.parent.suppliers)):
                if new_supplier not in self.parent.suppliers:
                    self.parent.suppliers.append(new_supplier)
                    self.parent.init_supplier_frame(new_supplier)

            self.root.destroy()
        except TclError:
            Label(self.frame[2], text="Wrong ID ,Phone or Age please enter a number", fg='red', font=("calibri", 12)).grid(row=1, column=0)
            phone_entry.set(0)
            name_entry.set('')
            address_entry.set('')
            id_entry.set(0)

    def cancel(self):
        """
        this function cancel the operation of adding new supplier
        :return:
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

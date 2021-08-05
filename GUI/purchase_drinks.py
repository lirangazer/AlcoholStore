from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from store.drink import *


class PurchaseDrinks():
    """
    this class implement the purchase drinks from supplier
    """
    def __init__(self, root, title, window_geo, parent, icon=None):
        self.root = root
        self.root.title(title)
        self.root.geometry(window_geo)
        self.parent = parent
        self.frame = []
        self.items = []
        self.catalog_id = {'Red Label': 1055, 'Glenfiddich' : 1056, 'Grey Goose': 2055, 'Van Gogh': 2056, 'Bakerdi':3055, 'Captain Morgans':3056,
                           'Bombay Sapphire':4055, 'Beefeater':4056}
        self.price = {'Red Label': 150, 'Glenfiddich' : 250, 'Grey Goose': 200, 'Van Gogh': 180, 'Bakerdi':100, 'Captain Morgans':250,
                           'Bombay Sapphire':120, 'Beefeater':130}
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

    def init_window(self, i=None):
        """
        this function initialized the widget
        :param i:
        :return:
        """
        Label(self.frame[0], text="Please choose the Drinks Purchase details", bg='cyan', font=("calibri", 12)).grid(row=0, column=0, pady=10)
        self.items.append(Label(self.frame[1], text='type'))
        drinks_types = ['Vodka', 'Whiskey', 'Rum', 'Gin']
        self.items.append(Combobox(self.frame[1], values=drinks_types))
        self.items.append(Label(self.frame[1], text='brand'))
        self.items.append(Combobox(self.frame[1]))
        self.items.append(Label(self.frame[1], text='Amount'))
        amount = StringVar()
        self.items.append(Entry(self.frame[1], textvariable=amount))
        self.items.append(Label(self.frame[1], text='catalog_id'))
        self.items.append(Entry(self.frame[1], state='disable'))
        self.items.append(Label(self.frame[1], text='price'))
        self.items.append(Entry(self.frame[1], state='disable'))
        self.items[0].grid(row=0, column=0)
        self.items[1].grid(row=0, column=1)
        self.items[2].grid(row=1, column=0)
        self.items[3].grid(row=1, column=1)
        self.items[4].grid(row=2, column=0)
        self.items[5].grid(row=2, column=1)
        self.items[6].grid(row=3, column=0)
        self.items[7].grid(row=3, column=1)
        self.items[8].grid(row=4, column=0)
        self.items[9].grid(row=4, column=1)
        self.items[1].bind("<<ComboboxSelected>>", lambda i=i: self.update_drinks_name(i))
        self.items[3].bind("<<ComboboxSelected>>", lambda i=i: self.update_drinks_id_price(i))
        Button(self.frame[2], text='Save', height=1, width=7,command=lambda i=0: self.return_drinks()).grid(row=0, column=1)
        Button(self.frame[2], text='Cancel', height=1, width=7, command=lambda i=1:self.cancel()).grid(row=0, column=2, pady=5)

    def update_drinks_name(self, event):
        """
        this function update the comobobox of the drinks names
        :param event: get the event from the selected
        :return:
        """
        if event.widget.get() == 'Vodka':
            vodka_brand = ['Grey Goose', 'Van Gogh']
            self.items[3]['values'] = vodka_brand
        elif event.widget.get() == 'Whiskey':
            whiskey_brand = ['Red Label', 'Glenfiddich']
            self.items[3]['values'] = whiskey_brand
        elif event.widget.get() == 'Rum':
            rum_brand = ['Bakerdi', 'Captain Morgans']
            self.items[3]['values'] = rum_brand
        elif event.widget.get() == 'Gin':
            gin_brand = ['Bombay Sapphire', 'Beefeater']
            self.items[3]['values'] = gin_brand

    def return_drinks(self):
        """
        this function return the drinks that purchase form supplier to the main window
        :return:
        """
        new_drink = Drink(self.items[1].get(),self.items[3].get(),int(self.items[7].get()),int(self.items[9].get()), int(self.items[5].get()))
        self.parent.tmp_drinks.append(new_drink)
        self.root.destroy()

    def cancel(self):
        """
        this function use to cancel the operation
        :return:
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def update_drinks_id_price(self, i):
        """
        this function update the price and catalog id for the chosen drink
        :param i:
        :return:
        """
        for (k,v) in self.catalog_id.items():
            if i.widget.get() == k:
                self.items[7].configure(state='normal')
                self.items[7].delete(0, 'end')
                self.items[7].insert(0, v)
                self.items[7].configure(state='disable')
        for (k,v) in self.price.items():
            if i.widget.get() == k:
                self.items[9].configure(state='normal')
                self.items[9].delete(0, 'end')
                self.items[9].insert(0, v)
                self.items[9].configure(state='disable')

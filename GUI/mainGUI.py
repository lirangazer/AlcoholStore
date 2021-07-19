"""
this is the GUI impalement gui
"""
import sys
import re
import traceback
import tkinter
from tkinter import *
from tkinter.ttk import *
from common.root_logger import *
import os
import subprocess
from GUI.login_window import *
from GUI.new_buyer_window import *
from GUI.new_supplier_window import *
from picture import *
from store.drink import *
from store.buyer import *
from store.product_sale import ProductSale
from store.sale import Sale
from store.supplier import *
from store.product_purchase import *
from store.store import *

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
buyer_text = ''
supplier_text = ''


#
# def add_to_basket():
#     print('success')


def add_new_buyer(main_window):
    new_buyer = Toplevel()
    new_buyer_user = NewBuyerWindow(new_buyer, "Add new Buyer", '350x350', main_window)

    new_buyer.mainloop()


def add_new_supplier(main_window):
    new_supplier = Toplevel()
    new_supplier_window = NewSupplierWindow(new_supplier, "Add New Supplier", '350x350', main_window)
    new_supplier.mainloop()


class AlcoholStore():
    def __init__(self, main_window, title, window_geo, perant, icon=None):
        setup_logger(title, print_to_screen=False)
        self.main_window = main_window
        self.main_window.title(title)
        self.main_window.geometry(window_geo)
        self.perant = perant

        global PROJECT
        PROJECT = title
        self.frame = []
        self.buttons = []
        self.products_name = []
        self.products_pic = []
        self.spinbox_pic = []
        self.buyer_list_items = []
        self.buyers = []
        self.buyers_names = []
        self.suppliers = []
        self.suppliers_names = []
        self.supplier_list_items = []
        self.basket = []
        self.init_frame()
        self.init_buttons()
        self.init_pic()
        self.init_buyer_frame()
        self.init_supplier_frame()

    def init_frame(self):
        for i in range(4):
            self.frame.append(Frame(self.main_window, height=70, width=400, pady=15, padx=15))
        self.frame[0].grid(row=0, column=0)
        self.frame[1].grid(row=1, column=0)
        self.frame[2].grid(row=1, column=1)
        self.frame[3].grid(row=2, column=0)

    def init_buttons(self):
        buttons_name = ['Purchase', 'Cancel', 'Add Buyer', 'Add Supplier', 'Exit']
        for i in range(len(buttons_name)):
            self.buttons.append(Button(self.frame[3], text=buttons_name[i], padx=20, pady=15,
                                       command=lambda i=i: self.buttons_action(i)))
        self.buttons[0].grid(row=0, column=0, padx=20, pady=15)
        self.buttons[1].grid(row=0, column=1)
        self.buttons[2].grid(row=0, column=2)
        self.buttons[3].grid(row=0, column=3)
        self.buttons[4].grid(row=0, column=4)

    def init_pic(self):
        picture_path = {'Red Label': r"picture\redlabel.png", 'Glenfiddich': r"picture/glenfiddich.png",
                        'Grey Goose': 'picture/grey goose.png'}
        i = 0
        for (k, v) in picture_path.items():
            tmp = Image.open(v)
            tmp1 = tmp.resize((100, 100), Image.ANTIALIAS)
            tmp2 = ImageTk.PhotoImage(tmp1)
            self.products_pic.append(Button(self.frame[0], image=tmp2, text=k, padx=20, pady=15))
            self.products_name.append(Label(self.frame[0], text=k))
            self.spinbox_pic.append(Spinbox(self.frame[0], from_=0, to=100, state='disable'))
            self.products_pic[i].image = tmp2
            i += 1
        for j in range(len(self.products_pic)):
            self.products_pic[j].grid(row=0, column=j, padx=5)
            print(self.products_pic[j])
            self.products_pic[j].bind('<Button-1>', lambda i=i: self.add_to_basket(i))
            self.products_pic[j].bind('<Button-3>', lambda i=i: self.edit_drink(i))
            self.products_name[j].grid(row=1, column=j)
            self.spinbox_pic[j].grid(row=2, column=j)

    def init_buyer_frame(self, buyer=None):
        self.buyer_list_items.append(Label(self.frame[1], text="Buyer"))
        self.buyer_list_items.append(Combobox(self.frame[1]))
        if buyer is not None:
            self.buyers_names.append(buyer.name)
            self.buyer_list_items[1]['values'] = self.buyers_names
            self.buyer_list_items[1].bind("<<ComboboxSelected>>", lambda buyer=buyer: self.update_buyer_detailes(buyer))
        buyer_category_text = ["ID", "Phone", "Age"]
        for i in range(len(buyer_category_text)):
            self.buyer_list_items.append(Label(self.frame[1], text=buyer_category_text[i]))
            self.buyer_list_items.append(Entry(self.frame[1], state='disable'))
        self.buyer_list_items[0].grid(row=0, column=0)
        self.buyer_list_items[1].grid(row=0, column=1)
        self.buyer_list_items[2].grid(row=1, column=0)
        self.buyer_list_items[3].grid(row=1, column=1)
        self.buyer_list_items[4].grid(row=2, column=0)
        self.buyer_list_items[5].grid(row=2, column=1)
        self.buyer_list_items[6].grid(row=3, column=0)
        self.buyer_list_items[7].grid(row=3, column=1)

    def buttons_action(self, index):
        """
        :param index: Index of the pressed button.
        """
        # file_parser = filesParse()
        if index == 0:
            pass
        elif index == 2:
            # self.add_new_buyer()
            add_new_buyer(self)
        elif index == 3:
            add_new_supplier(self)
        elif index == 4:
            self.main_window.destroy()
            self.perant.deiconify()

    def update_buyer_detailes(self, buyer):
        buyer_category_text = ["ID", "Phone", "Age"]

        global buyer_text
        for buyer1 in self.buyers:
            if buyer.widget.get() == buyer1.name:
                for i in range(len(buyer_category_text)):
                    if buyer_category_text[i] == 'ID':
                        buyer_text = str(buyer1.id)
                        self.buyer_list_items[3].configure(state='normal')
                        self.buyer_list_items[3].delete(0, 'end')
                        self.buyer_list_items[3].insert(0, buyer_text)
                        self.buyer_list_items[3].configure(state='disable')
                    elif buyer_category_text[i] == 'Phone':
                        buyer_text = str(buyer1.phone)
                        self.buyer_list_items[5].configure(state='normal')
                        self.buyer_list_items[5].delete(0, 'end')
                        self.buyer_list_items[5].insert(0, buyer_text)
                        self.buyer_list_items[5].configure(state='disable')
                    elif buyer_category_text[i] == 'Age':
                        buyer_text = str(buyer1.age)
                        self.buyer_list_items[7].configure(state='normal')
                        self.buyer_list_items[7].delete(0, 'end')
                        self.buyer_list_items[7].insert(0, buyer_text)
                        self.buyer_list_items[7].configure(state='disable')
                    else:
                        buyer_text = ''
            else:
                continue

    def init_supplier_frame(self, supplier=None):
        self.supplier_list_items.append(Label(self.frame[2], text='Supplier'))
        self.supplier_list_items.append(Combobox(self.frame[2]))
        if supplier is not None:
            self.suppliers_names.append(supplier.name)
            self.supplier_list_items[1]['values'] = self.suppliers_names
            self.supplier_list_items[1].bind("<<ComboboxSelected>>", lambda supplier=supplier: self.update_supplier_detailes(supplier))
        supplier_category_text = ['Address', 'ID', 'Phone']
        for i in range(len(supplier_category_text)):
            self.supplier_list_items.append(Label(self.frame[2], text=supplier_category_text[i]))
            self.supplier_list_items.append(Entry(self.frame[2], state='disable'))
        self.supplier_list_items[0].grid(row=0, column=0)
        self.supplier_list_items[1].grid(row=0, column=1)
        self.supplier_list_items[2].grid(row=1, column=0)
        self.supplier_list_items[3].grid(row=1, column=1)
        self.supplier_list_items[4].grid(row=2, column=0)
        self.supplier_list_items[5].grid(row=2, column=1)
        self.supplier_list_items[6].grid(row=3, column=0)
        self.supplier_list_items[7].grid(row=3, column=1)

    def update_supplier_detailes(self, supplier):
        supplier_category_text = ['Address', 'ID', 'Phone']
        global supplier_text
        for supplier1 in self.suppliers:
            if supplier.widget.get() == supplier1.name:
                for i in range(len(supplier_category_text)):

                    if supplier_category_text[i] == 'Address':
                        supplier_text = str(supplier1.address)
                        self.supplier_list_items[3].configure(state='normal')
                        self.supplier_list_items[3].delete(0, 'end')
                        self.supplier_list_items[3].insert(0, supplier_text)
                        self.supplier_list_items[3].configure(state='disable')
                    elif supplier_category_text[i] == 'Phone':
                        supplier_text = str(supplier1.phone)
                        self.supplier_list_items[5].configure(state='normal')
                        self.supplier_list_items[5].delete(0, 'end')
                        self.supplier_list_items[5].insert(0, supplier_text)
                        self.supplier_list_items[5].configure(state='disable')
                    elif supplier_category_text[i] == 'ID':
                        supplier_text = str(supplier1.id)
                        self.supplier_list_items[7].configure(state='normal')
                        self.supplier_list_items[7].delete(0, 'end')
                        self.supplier_list_items[7].insert(0, supplier_text)
                        self.supplier_list_items[7].configure(state='disable')
                    else:
                        supplier_text = ''
            else:
                continue

    def add_to_basket(self, event):
        for i in range(len(self.products_name)):
            if self.products_pic[i] is event.widget:
                # event.widget.c
                self.ask_for_amount()
                self.basket.append(self.products_name[i])

        print(self.basket)

    def ask_for_amount(self):
        pass

    def edit_drink(self, event):
        for i in range(len(self.products_name)):
            if self.products_pic[i] is event.widget:
                self.spinbox_pic[i].configure(state='normal')
                print(self.spinbox_pic[i].get())
                self.spinbox_pic[i].configure(state='disable')


setup_logger(PROJECT)
logger = get_logger()


def mainStore(root_window):
    try:
        logger.info("StoreApp Ready")

        store = Store()
        newroot = Toplevel()
        alcohol_store = AlcoholStore(newroot, 'Alcohol Store', '1000x1000', root_window)
        root_window.withdraw()

        # Under age example
        # --------------------------------------------------------------------
        drink = Drink("Wiski", "Red Label", 1055, 500, 0)
        buyer = Buyer("Wihbe", 2055, 5022, 30)
        sale = Sale(558956)
        # label_text = drink.name + "  amount: " + str(drink.amount)
        # alcohol_store.products_name[0].config(text=label_text)

        wihbe_product_sale = ProductSale(5, sale, drink, buyer)
        store.sell_product(wihbe_product_sale)

        # Not exist in the stock example.
        # --------------------------------------------------------------------

        buyer_amit = Buyer("Amit", 20365899, 504808196, 80)
        alcohol_store.buyers.append(buyer_amit)
        alcohol_store.init_buyer_frame(buyer_amit)
        amit_product_sale = ProductSale(5, sale, drink, buyer_amit)
        store.sell_product(amit_product_sale)
        # Purchase example.
        # --------------------------------------------------------------------
        supplier = Supplier("Chen", "Haifa", 11, 559842658)
        #alcohol_store.supplier_list_items[1]['values'] += supplier.name
        alcohol_store.suppliers.append(supplier)
        alcohol_store.init_supplier_frame(supplier)
        product_purchase = ProductPurchase(drink, supplier, "Buying vodka", 3)
        store.product_purchase_from_supplier(product_purchase)
        for i in range(len(alcohol_store.products_name)):
            if product_purchase.drink.name == alcohol_store.products_name[i].cget("text"):
                amount = StringVar()
                amount.set(str(product_purchase.amount))
                alcohol_store.spinbox_pic[i].configure(state='normal')
                alcohol_store.spinbox_pic[i].configure(textvariable=amount)
                alcohol_store.spinbox_pic[i].configure(state='disable')

        # Selling not enough products.
        # --------------------------------------------------------------------
        store.sell_product(amit_product_sale)

        # Another purchase
        # --------------------------------------------------------------------
        store.product_purchase_from_supplier(product_purchase)

        # Selling with the right amount.
        # --------------------------------------------------------------------
        store.sell_product(amit_product_sale)

        # Display drink in store.
        # --------------------------------------------------------------------
        store.display_drinks_in_store()

        # Display Purchase and Selling history in store.
        # --------------------------------------------------------------------
        store.display_product_purchases_from_supplier()
        newroot.mainloop()

        logger.info("Finshed running")

    except Exception as e:
        exc_traceback = sys.exc_info()[2]  # Full traceback address

        print(
            "\n=======================================================================================================================")
        logger.error("Exception 'e': {0}  -- Error started in line: {1}".format(e, exc_traceback.tb_lineno))
        print(
            "=======================================================================================================================\n")

        print(
            "=======================================================================================================================")
        full_traceback = traceback.format_tb(exc_traceback)
        logger.error("main -> Exception: printing full traceback stack")
        # full_traceback.reverse()
        for error_trace in full_traceback:
            # trace_arrange = error_trace.split(',')
            trace_arrange = re.split(', |\n', error_trace)
            logger.error("Method: {0} -- {1} -- Error: {2} -- {3}".format(trace_arrange[2], trace_arrange[1],
                                                                          trace_arrange[3].strip(), trace_arrange[0]))

        print(
            "=======================================================================================================================\n")
        logger.info(r'Log file save in: {0}\{1}.log'.format(get_working_dir(), get_project()))

    finally:
        release_logger()

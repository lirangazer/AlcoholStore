"""
this is the GUI impalement gui
"""
import sys
import re
import traceback
import tkinter
from tkinter import *
from common.root_logger import *
import os
import subprocess
from GUI.login_window import *
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


def add_to_basket():
    print('success')


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
        picture_path = {'Red Label': r"picture\redlabel.png", 'Glenfiddich': r"picture/glenfiddich.png",
                        'Grey Goose': 'picture/grey goose.png'}
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

    def buttons_action(self, index):
        """
        :param index: Index of the pressed button.
        """
        # file_parser = filesParse()
        if index == 0:
            pass
        if index == 3:
            self.main_window.destroy()
            self.perant.deiconify()


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
        amit_product_sale = ProductSale(5, sale, drink, buyer_amit)
        store.sell_product(amit_product_sale)
        # Purchase example.
        # --------------------------------------------------------------------
        supplier = Supplier("Chen", "Haifa", 11, 559842658)
        product_purchase = ProductPurchase(drink, supplier, "Buying vodka", 3)
        store.product_purchase_from_supplier(product_purchase)
        for i in range(len(alcohol_store.products_name)):
            if product_purchase.drink.name == alcohol_store.products_name[i].cget("text"):
                label_text = drink.name + "  amount: " + str(product_purchase.amount)
                alcohol_store.products_name[i].config(text=label_text)


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

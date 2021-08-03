"""
this is the GUI impalement gui
"""
import sys
import re
import traceback
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from common.root_logger import *
import os
import subprocess
import random
from GUI.login_window import *
from GUI.new_buyer_window import *
from GUI.new_supplier_window import *
from GUI.ask_for_amount import *
from GUI.purchase_drinks import *
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
button_flag = 0


def add_new_buyer(main_window):
    new_buyer = Toplevel()
    new_buyer_user = NewBuyerWindow(new_buyer, "Add new Buyer", '350x350', main_window)
    # new_buyer.protocol("WM_DELETE_WINDOW", on_closing(new_buyer))
    main_window.main_window.wait_window(new_buyer)


def add_new_supplier(main_window):
    new_supplier = Toplevel()
    new_supplier_window = NewSupplierWindow(new_supplier, "Add New Supplier", '350x350', main_window)
    new_supplier.mainloop()


def update_drinks_amount(colling_window):
    for i in range(len(colling_window.products_name)):
        if colling_window.tmp_drinks[0].name == colling_window.products_name[i].cget('text'):
            if int(colling_window.spinbox_pic[i].cget('text')) == '0':
                amount = StringVar()
                amount.set(colling_window.tmp_drinks[0].amount)
                #colling_window.spinbox_pic[i].configure(state='normal')
                colling_window.spinbox_pic[i].configure(textvariable=amount)
                #colling_window.spinbox_pic[i].configure(state='disable')
            else:
                amount_1 = StringVar()
                tmp_amount = int(colling_window.spinbox_pic[i].cget('text')) + colling_window.tmp_drinks[0].amount
                amount_1.set(tmp_amount)
                #colling_window.spinbox_pic[i].configure(state='normal')
                colling_window.spinbox_pic[i].configure(textvariable=amount_1)
                #colling_window.spinbox_pic[i].configure(state='disable')
        else:
            continue


def purchase_from_supplier(colling_window):
    prices = 0
    if colling_window.supplier_list_items[7].get() == '':
        colling_window.messages_label[0]['text'] = "Invalid Supplier!! Please choose supplier from list"
    else:
        purchase_drink = Toplevel()
        PurchaseDrinks(purchase_drink, 'purchase form supplier', '350x350', colling_window)
        colling_window.main_window.wait_window(purchase_drink)
        tmp_supplier = Supplier(colling_window.supplier_list_items[1].get(), colling_window.supplier_list_items[3].get(),
                                colling_window.supplier_list_items[7].get(), colling_window.supplier_list_items[5].get())
        for i in colling_window.tmp_drinks:
            tmp_text = "buying" + " " + i.name
            tmp_purchase = ProductPurchase(i, tmp_supplier, tmp_text, i.amount)
            colling_window.store.product_purchase_from_supplier(tmp_purchase)
            prices += (i.price * i.amount)
        messagebox.showinfo('Thanks', 'Thanks for purchase the total value is : %s' % str(prices))

        update_drinks_amount(colling_window)
        colling_window.store.display_drinks_in_store()
        colling_window.tmp_drinks.clear()


def get_total_amount(drinks_in_store, drink):
    for i in drinks_in_store:
        if i.catalog_id == drink.catalog_id:
            return i.amount
        else:
            continue


def get_total_pay(celling_winsow):
    total_pay = 0
    for i in celling_winsow.basket:
        total_pay += int(i.amount) * i.price
    return total_pay

def sale_to_buyer(celling_window):
    if celling_window.buyer_list_items[3].get() == '':

        celling_window.messages_label[0]['text'] = "Invalid Buyer!! Please choose buyer from list"
    else:
        tmp_buyer = Buyer(celling_window.buyer_list_items[1].get(), int(celling_window.buyer_list_items[3].get()), int(celling_window.buyer_list_items[5].get()),
                          int(celling_window.buyer_list_items[7].get()))
        sale = Sale(random.randrange(100000, 999999))
        for i in celling_window.basket:
            tmp_product_sale = ProductSale(i.amount, sale, i, tmp_buyer)
            return_answer = int(celling_window.store.sell_product(tmp_product_sale))
            if return_answer == 0:
                messagebox.showerror("Under Age", "The buyer {0} is under legal age 18, his age: {1}".format(tmp_product_sale.buyer.name, tmp_product_sale.buyer.age))
            elif return_answer == 1:
                messagebox.showwarning('Not enough product', "The item {0} amount is: {1}".format(tmp_product_sale.drink.name, get_total_amount(celling_window.store.drinks_in_store,
                                                                                                                                                tmp_product_sale.drink)))
            elif return_answer == 2:
                messagebox.showwarning("Item don't Exist", "The item: {0} is not exist in the stock".format(tmp_product_sale.drink.name))
            elif return_answer == 3:

                # print(''.join(e.drink.name for e in celling_window.store.product_sales))
                # print(f"Invoice Number:, {sale.invoice_number}\n {sale.date}\n ",' Sold :','\n'.join(e.drink.amount for e in celling_window.store.product_sales),'  drinks of:',
                #       '\n'.join(e.drink.name for e in celling_window.store.product_sales),'\n')
                # for drink in range(len(celling_window.products_pic)):
                #     if celling_window.products_pic[drink].cget('text') == celling_window.basket[drink].name:
                #         celling_window.spinbox_pic[drink]['text'] =str(int(celling_window.spinbox_pic[drink].cget('text')) - int(celling_window.basket[drink].drink.amount))
                for i in range(len(celling_window.basket)):
                    for drink in range(len(celling_window.products_pic)):
                        if celling_window.products_pic[drink].cget('text') == celling_window.basket[i].name:
                            amount = StringVar()
                            tmp_amount = celling_window.spinbox_pic[drink].cget('text') - int(celling_window.basket[i].amount)
                            amount.set(tmp_amount)
                            celling_window.spinbox_pic[drink].configure(textvariable=amount)

                print(f"Invoice Number:{sale.invoice_number}\n{sale.date} "+'\n' " Sold :"+''.join([e.drink.amount for e in celling_window.store.product_sales]),
                                                         '  drinks of:'+'\n'.join([e.drink.name for e in celling_window.store.product_sales]))

                messagebox.showinfo("Thanks for buying",(f"Invoice Number:{sale.invoice_number}\n{sale.date} "+'\n' " Sold :"+''.join([e.drink.amount for e in celling_window.store.product_sales]),
                                                         '  drinks of:'+'\n'.join([e.drink.name for e in celling_window.store.product_sales]+''.join('\nTotal pay: '+str(get_total_pay(celling_window))))))
                celling_window.basket.clear()


class AlcoholStore():
    def __init__(self, main_window, title, window_geo, perant, store, icon=None):
        setup_logger(title, print_to_screen=False)
        self.main_window = main_window
        self.main_window.title(title)
        self.main_window.geometry(window_geo)
        self.perant = perant
        self.store = store
        global PROJECT
        PROJECT = title
        self.amount = 0
        self.frame = []
        self.buttons = []
        self.products_name = []
        self.products_pic = []
        self.drinks = []
        self.tmp_drinks = []
        self.spinbox_pic = []
        self.label_pic = []
        self.price_pic = []
        self.messages_label = []
        self.buyer_list_items = []
        self.buyers = []
        self.buyers_names = []
        self.suppliers = []
        self.suppliers_names = []
        self.supplier_list_items = []
        self.basket = []
        self.init_frame()
        self.init_buttons()
        self.init_message_label()
        self.init_pic()
        self.init_buyer_frame()
        self.init_supplier_frame()

    def init_frame(self):
        # self.main_window.grid_rowconfigure(1, weight=1)
        # self.main_window.grid_columnconfigure(0, weight=1)
        for i in range(5):
            self.frame.append(Frame(self.main_window, height=60, width=400, pady=15, padx=15))
        self.frame[0].grid(row=0, sticky='ew', columnspan=2)
        self.frame[1].grid(row=1, column=0, sticky='ew', columnspan=2)
        self.frame[2].grid(row=2, column=0, sticky='ew',padx=180)
        self.frame[3].grid(row=2, column=1, sticky='nsew', padx=180 )
        self.frame[4].grid(row=3, column=0, sticky='nsew', columnspan=2, padx=250)

    def init_buttons(self):
        buttons_name = ['Purchase from supplier', 'Sale to buyer', 'Add Buyer', 'Add Supplier', 'Exit']
        for i in range(len(buttons_name)):
            self.buttons.append(Button(self.frame[4], text=buttons_name[i], padx=20, pady=15,
                                       command=lambda i=i: self.buttons_action(i)))
        self.buttons[0].grid(row=0, column=0, pady=15)
        self.buttons[1].grid(row=0, column=1)
        self.buttons[2].grid(row=0, column=2)
        self.buttons[3].grid(row=0, column=3)
        self.buttons[4].grid(row=0, column=4)

    def init_pic(self):
        picture_path = {'Red Label': r"picture\redlabel.png", 'Glenfiddich': r"picture/glenfiddich.png",
                        'Grey Goose': 'picture/grey goose.png', 'Van Gogh': r'picture/vangoghacaiblueberry.png', 'Captain Morgans': r'picture/Captin_Morgans.png',
                        'Bakerdi': 'picture/Bakerdi.png', 'Bombay Sapphire': r'picture/bombay Sapphire.png', 'Beefeater': 'picture/BEEFEATER.png'}
        price = {'Red Label': 150, 'Glenfiddich': 250, 'Grey Goose': 200, 'Van Gogh': 180, 'Bakerdi': 100, 'Captain Morgans': 250,
                 'Bombay Sapphire': 120, 'Beefeater': 130}
        i = 0
        for (k, v) in picture_path.items():
            tmp = Image.open(v)
            tmp1 = tmp.resize((100, 100), Image.ANTIALIAS)
            tmp2 = ImageTk.PhotoImage(tmp1)
            self.products_pic.append(Button(self.frame[0], image=tmp2, text=k, padx=20, ))
            self.products_name.append(Label(self.frame[0], text=k))

            self.label_pic.append(Label(self.frame[1], text='amount', state='disable'))
            self.spinbox_pic.append(Label(self.frame[1], text='0'))
            self.products_pic[i].image = tmp2
            i += 1
        for (k,v) in price.items():
            text = 'price: ' + str(v)
            self.price_pic.append(Label(self.frame[0], text=text))
        for j in range(len(self.products_pic)):
            self.products_pic[j].grid(row=0, column=j, padx=5, pady=5)
            self.products_pic[j].bind('<Button-1>', lambda i=i: self.add_to_basket(i))
            # self.products_pic[j].bind('<Double-Button-1>', lambda i=i: self.remove_to_basket(i))
            self.products_pic[j].bind('<Button-3>', lambda i=i: self.remove_to_basket(i))
            # self.products_pic[j].bind('<Double-Button-3>', lambda i=i: self.stop_edit_drink(i))
            self.products_name[j].grid(row=1, column=j)
            self.price_pic[j].grid(row=2, column=j)
            self.label_pic[j].grid(row=1, column=j ,padx=34)
            self.spinbox_pic[j].grid(row=2, column=j)

    def buttons_action(self, index):
        """
        :param index: Index of the pressed button.
        """
        if index == 0:
            purchase_from_supplier(self)
        elif index == 1:
            sale_to_buyer(self)
        elif index == 2:
            add_new_buyer(self)
        elif index == 3:
            add_new_supplier(self)
        elif index == 4:
            self.main_window.destroy()
            self.perant.deiconify()

    def init_buyer_frame(self, buyer=None):
        self.buyer_list_items.append(Label(self.frame[2], text="Buyer"))
        self.buyer_list_items.append(Combobox(self.frame[2]))
        if buyer is not None:
            self.buyers_names.append(buyer.name)
            self.buyer_list_items[1]['values'] = self.buyers_names
            self.buyer_list_items[1].bind("<<ComboboxSelected>>", lambda buyer=buyer: self.update_buyer_detailes(buyer))
        buyer_category_text = ["ID", "Phone", "Age"]
        for i in range(len(buyer_category_text)):
            self.buyer_list_items.append(Label(self.frame[2], text=buyer_category_text[i]))
            self.buyer_list_items.append(Entry(self.frame[2], state='disable'))
        self.buyer_list_items[0].grid(row=0, column=0)
        self.buyer_list_items[1].grid(row=0, column=1)
        self.buyer_list_items[2].grid(row=1, column=0)
        self.buyer_list_items[3].grid(row=1, column=1)
        self.buyer_list_items[4].grid(row=2, column=0)
        self.buyer_list_items[5].grid(row=2, column=1)
        self.buyer_list_items[6].grid(row=3, column=0)
        self.buyer_list_items[7].grid(row=3, column=1)

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
        self.supplier_list_items.append(Label(self.frame[3], text='Supplier'))
        self.supplier_list_items.append(Combobox(self.frame[3]))
        if supplier is not None:
            self.suppliers_names.append(supplier.name)
            self.supplier_list_items[1]['values'] = self.suppliers_names
            self.supplier_list_items[1].bind("<<ComboboxSelected>>",
                                             lambda supplier=supplier: self.update_supplier_detailes(supplier))
        supplier_category_text = ['Address', 'ID', 'Phone']
        for i in range(len(supplier_category_text)):
            self.supplier_list_items.append(Label(self.frame[3], text=supplier_category_text[i]))
            self.supplier_list_items.append(Entry(self.frame[3], state='disable'))
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
                self.products_pic[i].config(relief='sunken')
                self.products_pic[i].config(bg='blue')
                self.ask_for_amount(self.spinbox_pic[i].cget('text'), event)
                if int(self.amount) > 0:
                    for j in self.store.drinks_in_store:
                        if j.name == event.widget.cget('text'):
                            tmp_drink = Drink(j.type, j.name, j.catalog_id, j.price, j.amount)
                            tmp_drink.amount = self.amount
                            self.basket.append(tmp_drink)
                            break

        print(self.basket)

    def remove_to_basket(self, event):
        for i in range(len(self.products_name)):
            if self.products_pic[i] is event.widget:
                self.products_pic[i].config(relief='raised')
                for i in self.basket:
                    if i.name == event.widget.cget('text'):
                        self.basket.remove(i)
                    else:
                        continue
        # print(self.basket)

    def ask_for_amount(self, amount, event):
        ask_for_amount = Toplevel()
        AskForAmount(ask_for_amount, "Amount", '350x350', self, amount)
        self.main_window.wait_window(ask_for_amount)
        for i in range(len(self.products_name)):
            if self.products_pic[i] is event.widget:
                self.products_pic[i].config(bg='SystemButtonFace')
                self.products_pic[i].config(relief='raised')

    def init_message_label(self):
        self.messages_label.append(Label(self.frame[4], fg='red'))
        self.messages_label[0].grid(row=1, column=1, columnspan=3)


setup_logger(PROJECT)
logger = get_logger()


def mainStore(root_window):
    try:
        logger.info("StoreApp Ready")

        store = Store()
        newroot = Toplevel()
        alcohol_store = AlcoholStore(newroot, 'Alcohol Store', '1120x500', root_window, store)
        root_window.withdraw()

        # Under age example
        # --------------------------------------------------------------------
        drink = Drink("Wiski", "Red Label", 1055, 500, 0)
        buyer = Buyer("Wihbe", 2055, 5022, 30)
        alcohol_store.buyers.append(buyer)
        alcohol_store.init_buyer_frame(buyer)
        alcohol_store.drinks.append(drink)
        sale = Sale(558956)
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
        alcohol_store.suppliers.append(supplier)
        alcohol_store.init_supplier_frame(supplier)
        product_purchase = ProductPurchase(drink, supplier, "Buying vodka", 3)

        store.product_purchase_from_supplier(product_purchase)
        for i in range(len(alcohol_store.products_name)):
            if product_purchase.drink.name == alcohol_store.products_name[i].cget("text"):
                amount = StringVar()
                amount.set(str(product_purchase.amount))
                #alcohol_store.spinbox_pic[i].configure(state='normal')
                alcohol_store.spinbox_pic[i].configure(textvariable=amount)
                #alcohol_store.spinbox_pic[i].configure(state='disable')

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

#  -------------------------------------------------------------------------------
# Name:        alcohol_store
# Purpose:     Simulating saling and purchasing done in alcohol store
#
# Author:      Wihbe Brakat, Liran Avichzier
#
# Created:     20/5/2021
#  -------------------------------------------------------------------------------

from GUI.login_window import *
import traceback
import re
from common.root_logger import *
from store.drink import *
from store.buyer import *
from store.product_sale import ProductSale
from store.sale import Sale
from store.store import *
from tkinter import *
#
# CSV = r"common\tpu_configration.xml"
# XML = r"common\csv_file.csv"
from store.product_purchase import ProductPurchase
from store.supplier import Supplier

PROJECT = "StoreApp"

setup_logger(PROJECT)
logger = get_logger()

def main():
    """
    Main enterace of the program.
    Function responsible on the program flow.
    """
    root = Tk()
    login_window(root, "Alcohol Store", "250x150")
    root.iconbitmap('picture/Alcohol for all-logos_transparent.ico')
    root.mainloop()
    # try:
    #
    #     logger.info("StoreApp Ready")
    #
    #     store = Store()
    #     #store.display_drinks_in_store()
    #
    #
    #
    #
    #     #Under age example
    #     #--------------------------------------------------------------------
    #     drink = Drink("Wiski", "RedLabel", 1055, 500, 0)
    #     buyer = Buyer("Wihbe", 2055, 5022, 30)
    #     sale = Sale(558956)
    #
    #     wihbe_product_sale = ProductSale(5, sale, drink, buyer)
    #     store.sell_product(wihbe_product_sale)
    #
    #     #Not exist in the stock example.
    #     #--------------------------------------------------------------------
    #
    #     buyer_amit = Buyer("Amit", 20365899, 504808196, 80)
    #     amit_product_sale = ProductSale(5, sale, drink, buyer_amit)
    #     store.sell_product(amit_product_sale)
    #
    #     #Purchase example.
    #     #--------------------------------------------------------------------
    #     supplier = Supplier("Chen","Haifa", 11, 559842658)
    #     product_purchase = ProductPurchase(drink, supplier, "Buying vodka", 3)
    #     store.product_purchase_from_supplier(product_purchase)
    #
    #     #Selling not enough products.
    #     #--------------------------------------------------------------------
    #     store.sell_product(amit_product_sale)
    #
    #     #Another purchase
    #     #--------------------------------------------------------------------
    #     store.product_purchase_from_supplier(product_purchase)
    #
    #     #Selling with the right amount.
    #     #--------------------------------------------------------------------
    #     store.sell_product(amit_product_sale)
    #
    #     #Display drink in store.
    #     #--------------------------------------------------------------------
    #     store.display_drinks_in_store()
    #
    #     #Display Purchase and Selling history in store.
    #     #--------------------------------------------------------------------
    #     store.display_product_purchases_from_supplier()
    #
    #
    #     logger.info("Finshed running")
    #
    # except Exception as e:
    #     exc_traceback = sys.exc_info()[2]  # Full traceback address
    #
    #     print(
    #         "\n=======================================================================================================================")
    #     logger.error("Exception 'e': {0}  -- Error started in line: {1}".format(e, exc_traceback.tb_lineno))
    #     print(
    #         "=======================================================================================================================\n")
    #
    #     print(
    #         "=======================================================================================================================")
    #     full_traceback = traceback.format_tb(exc_traceback)
    #     logger.error("main -> Exception: printing full traceback stack")
    #     # full_traceback.reverse()
    #     for error_trace in full_traceback:
    #         # trace_arrange = error_trace.split(',')
    #         trace_arrange = re.split(', |\n', error_trace)
    #         logger.error("Method: {0} -- {1} -- Error: {2} -- {3}".format(trace_arrange[2], trace_arrange[1],
    #                                                                       trace_arrange[3].strip(), trace_arrange[0]))
    #
    #     print(
    #         "=======================================================================================================================\n")
    #     logger.info(r'Log file save in: {0}\{1}.log'.format(get_working_dir(), get_project()))
    #
    # finally:
    #     release_logger()

if __name__ == '__main__':
    main()

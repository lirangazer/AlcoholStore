#  -------------------------------------------------------------------------------
# Name:        alcohol_store
# Purpose:     Simulating saling and purchasing done in alcohol store
#
# Author:      Wihbe Brakat, Liran Avichzier
#
# Created:     20/5/2021
#  -------------------------------------------------------------------------------

# from gui.tpu_app import *
import traceback
import re
from common.root_logger import *
from store.drink import *
from store.buyer import *
# from tkinter import *
#
# CSV = r"common\tpu_configration.xml"
# XML = r"common\csv_file.csv"
from store.product_purchase import ProductPurchase

PROJECT = "StoreApp"

setup_logger(PROJECT)
logger = get_logger()

def main():
    """
    Main enterace of the program.
    Function responsible on the program flow.
    """

    try:

        logger.info("StoreApp Ready")
        drink = Drink("Wiski", "RedLabel", 223344, 25, 60)
        buyer = Buyer("Wihbe", 2055, 5022, 30)
        pp = ProductPurchase("w", "w", "w", "w")
        logger.info("{0},\n{1}".format(buyer, drink))

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

if __name__ == '__main__':
    main()

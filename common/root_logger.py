#  -------------------------------------------------------------------------------
# Name:        root logger file, can be used in multiple files.
# Purpose:     Logging for the project
#
# Author:      Wihbe Brakat, Liran Avichzier
#
# Created:     20/5/2021
#  -------------------------------------------------------------------------------

import sys
import os
import logging

WORKING_DIRECTORY = r"C:\Temp"
PROJECT = ""


def setup_logger(file, folder=WORKING_DIRECTORY, print_to_screen=True):
    """
    Setting up the logger for the program.
    File handler to save log.
    Console handler to print for the user.
    """
    try:
        global WORKING_DIRECTORY, PROJECT
        WORKING_DIRECTORY = folder
        PROJECT = file

        root_logger = logging.getLogger(PROJECT)

        if not os.path.isdir(r'{0}'.format(folder, file)):
            os.mkdir(r'{0}'.format(folder, file))

        if not os.path.isdir(r'{0}\{1}'.format(folder, file)):
            os.mkdir(r'{0}\{1}'.format(folder, file))

        file_handler = logging.FileHandler(r"{0}\{1}\{2}.log".format(folder, file, file))
        log_formatter = logging.Formatter("%(asctime)s [%(name)-12.12s] [%(levelname)-5.5s]  %(message)s")
        # log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)

        if (print_to_screen):
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(log_formatter)
            root_logger.addHandler(console_handler)

        root_logger.setLevel(logging.DEBUG)

    except Exception as setup_error:
        raise("Setup logger has been failed\nError: {0}".format(setup_error))


def get_logger():
    """
    Return active logger in the program
    Must use setup_logger(..) before
    :return:
    Logger object
    """
    if (not PROJECT):
        print("No logger defined")

    return logging.getLogger(PROJECT)


def release_logger(print_to_screen=True):
    """
    Release the logger from the program.
    Should called at the end of the program
    """
    root_logger = get_logger()
    if print_to_screen:
        root_logger.info(r'Closing logger')
    handlers = root_logger.handlers[:]
    for handler in handlers:
        handler.close()
        root_logger.removeHandler(handler)


def get_working_dir():
    """
    :return: string, working directory the logger uses
    """
    return WORKING_DIRECTORY


def get_project():
    """
    :return: string, project name
    """
    return PROJECT

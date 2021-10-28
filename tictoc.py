#!/usr/bin/python3

from time import time
from colorama import Fore, Back, Style

global start_time


def tic():
    """
    This function places the moment where the codes
    starts on a global variable named start_time
    """
    global start_time
    start_time = time()
    return


def toc():
    """
    After using the tic function, the toc functions reads
    the global variable and calculates the elapsed time
    """
    global start_time
    final_time = time()
    elapsed_time = final_time - start_time
    print('Time elapsed: ' + Fore.RED + str(elapsed_time) + Style.RESET_ALL + ' seconds.')
    return


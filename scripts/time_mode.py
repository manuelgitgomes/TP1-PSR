#!/usr/bin/python3

from colorama import Fore, Back, Style
import readchar
from tictoc import *
import random


def time_mode(max_value):
    print("Program stops after " + Fore.BLUE + str(max_value) + Style.RESET_ALL + ' seconds')
    print("Click on a letter to start the test")


    a = readchar.readkey()
    tic()
    t=time()

    # (maybe) first seeing the ascii table and doing a list with all the lower case letters
    letters = [chr(x) for x in range(97, 123)]

    print(letters)
    elapsed = time() - t

    while elapsed < max_value:
        rand_letter = random.choice(letters)
        print('The program wants' + rand_letter)
        typed_letter = readchar.readkey()
        if typed_letter == ' ':
            print('the program was interrupted')
            break
        #the toc prints the value and elapsed works for the while cycle
        elapsed = time() - t
        toc()

#!/usr/bin/python3

from colorama import Fore,Back, Style
import readchar


def printing_test(max_value):
    print("Program stops after " + Fore.RED + str(max_value) + Style.RESET_ALL + ' letters')
    print("Click on a letter to start the test")

    a = readchar.readkey()

    # (maybe) first seeing the ascii table and doing a list with all the lower case letters
    letters = [chr(x) for x in range(97, 123)]

    print(letters)
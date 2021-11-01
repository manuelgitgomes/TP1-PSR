#!/usr/bin/python3

from colorama import Fore, Back, Style
import readchar
from collections import namedtuple
from time import ctime
import random
from tictoc import *
import sys

# Define the named tuple
letters_tuple = namedtuple('letters_tuple', ['req', 'typed', 'time'])


def typing_test(max_value):
    """
    Through a series of prints, shows the a random letter and the user needs to type it correctly with a limited number
    of letters.

    :param max_value: Integer
    :return tuple_list: List of named tuples
    """

    # Defining the list for the named tuples
    tuple_list = []

    # Defining the letters to randomize from
    letters = [chr(x) for x in range(97, 123)]

    # Defining other variables
    letters_miss = 0
    letters_hit = 0
    break_bool = False

    # Print the starting parameters
    print("Program stops after " + Fore.RED + Style.BRIGHT + str(max_value) + Style.RESET_ALL + ' letters')
    print("Click on any letter to start the test. Press spacebar to end.")

    # Saves start time
    start_time = ctime()

    # While the number of members in the list of tuples does not surpass the max_value
    while len(tuple_list) < max_value:
        # Randomizes the letter and shows it
        rand_letter = random.choice(letters)
        print('The program wants ' + Style.BRIGHT + rand_letter + Style.RESET_ALL)

        # Starts counting the time
        tic()

        # Read the typed key and places the data on the named tuple and then places it on a list
        typed_letter = readchar.readkey()
        letters_tuple1 = letters_tuple(rand_letter, typed_letter, toc())
        tuple_list.append(letters_tuple1)

        # If the typed letter is the spacebar, the program stops
        if typed_letter == ' ':
            print('The program was interrupted, you pressed the spacebar!')
            break_bool = True
            break
        # If the typed letter is different then the one shown, inform the user and count it
        elif typed_letter != rand_letter:
            print(
                'And you have typed ' + typed_letter + ', ' + Style.BRIGHT + Fore.RED + 'incorrectly' + Style.RESET_ALL + '.')
            letters_miss += 1
        # If the typed letter is equal then the one shown, inform the user and count it
        else:
            print('And you have typed ' + typed_letter + ', ' + Style.BRIGHT + Fore.GREEN + 'correctly' + Style.RESET_ALL + '.')
            letters_hit += 1

    # If the cycle broke in a natural matter, print the respective text
    if not break_bool:
        print('You have reached the maximum value of ' + str(max_value) + ' letters, typing test ended.')
    else:
        sys.exit(1)

    # Saves stop time
    stop_time = ctime()
    return tuple_list, start_time, stop_time


#!/usr/bin/python3

from colorama import Fore, Back, Style
import readchar
from tictoc import *
import random
from collections import namedtuple
from time import time

# Define the named tuple
letters_tuple = namedtuple('letters_tuple', ['req', 'typed', 'time'])


def time_mode(max_value):
    """
   Through a series of prints, shows the a random letter and the user needs to type it correctly with a limited number
   of time.

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

    # Start counting the overall time
    start_time = tic()

    # Print the starting parameters
    print("Program stops after " + Fore.BLUE + Style.BRIGHT + str(max_value) + Style.RESET_ALL + ' seconds')
    print("Click on any letter to start the test. Press spacebar to end.")

    # Continuous while cycle
    while True:
        # Randomizes the letter and shows it
        rand_letter = random.choice(letters)
        print('The program wants ' + Style.BRIGHT + rand_letter + Style.RESET_ALL)

        # Starts counting the time
        tic()

        # Read the typed key and
        typed_letter = readchar.readkey()

        # If the ellapsed time is larger then the predetermined one, break the cycle
        if time() - start_time > max_value:
            print(
                'And you have typed ' + typed_letter + ', ' + Style.BRIGHT + Fore.YELLOW + 'too late' + Style.RESET_ALL + '.')
            break

        # Places the data on the named tuple and then places it on a list
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
            print(
                'And you have typed ' + typed_letter + ', ' + Style.BRIGHT + Fore.GREEN + 'correctly' + Style.RESET_ALL + '.')
            letters_hit += 1

    # If the cycle broke in a natural matter, print the respective text
    if not break_bool:
        print('You have reached the maximum value of ' + str(max_value) + ' seconds, typing test ended.')

    # Saves stop time
    stop_time = time.time()
    return tuple_list, start_time, stop_time

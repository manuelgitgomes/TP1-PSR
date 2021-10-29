#!/usr/bin/python3

from colorama import Fore,Back, Style
import readchar


def printing_test(max_value):
    print("Program stops after " + Fore.RED + str(max_value) + Style.RESET_ALL + ' letters')
    print("Click on a letter to start the test")

    a = readchar.readkey()

    # (maybe) first seeing the ascii table and doing a list with all the lower case letters
    letters = [chr(x) for x in range(97, 123)]
    counter = 0

    #create a better way than a counter in a while
    while counter <= max_value:
        rand_letter = random.choice(letters)
        print('The program wants' + rand_letter)
        typed_letter = readchar.readkey()
        if typed_letter == ' ':
            print('the program was interrupted')
            break
        if typed_letter != rand_letter:
          # fazer aqui o print da letra (visto que estes if's são iguais secalhar uma função que recebe a typed letter 
          # e a rand_letter seria o melhor
            letters_miss += 1
        else
            letters_hit += 1
        counter += 1

#!/usr/bin/python3

# ---------------------------
# python project for the TP1
# nº88729 - Sara Costa Pombinho
# nº88939 - Manuel Alberto Silva Gomes
# nº109483 - Diogo dos Santos Covêlo Simão Vieira
# G9 from the class P2
# -----------------------------


import argparse
from typing_test import *
from time_mode import *
from dic import *


def main():
    """
    Defines the parser, its argumetns and runs the functions
    :return:
    """
    # Arguments asked for the program
    parser = argparse.ArgumentParser()
    parser.add_argument('-utm ', '--use_time_mode', help='To run the program using the time mode',
                        action='store_true')
    parser.add_argument('-mv ', '--max_value', help='maximum number of inputs for number of inputs mode',
                        type=int)
    args = vars(parser.parse_args())
    max_value = args['max_value']
    utm = args['use_time_mode']

    # If you select time mode, time mode is ran. If not, letter mode is ran.
    if utm:
        tuple_list, start_time, stop_time = time_mode(max_value)
    else:
        tuple_list, start_time, stop_time = typing_test(max_value)

    # Calculates the stats and the prints them
    statsDict(tuple_list, start_time, stop_time)

    return


if __name__ == '__main__':
    main()
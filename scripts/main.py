#!/usr/bin/python3

from time import sleep
import argparse
from tictoc import *


def main():
    tic()
    sleep(10)       # This is just a debug line, so we can make sure it works.
    toc()

    #the functions are still not done
    #arguments asked for the program
    parser = argparse.ArgumentParser()
    parser.add_argument('-utm ', '--use_time_mode', help='To run the program using the time mode',
                        action='store_true')
    parser.add_argument('-mv ', '--max_value', help='maximum number of inputs for number of inputs mode',
                        type=int)
    args = vars(parser.parse_args())

    #thinking in a way to separate both types of tests
    if args['use_time_mode']:
        time_mode(args['max_value']) #function using the time mode
    else:
        printing_test(args['max_value']) #function not using the time mode


    return


if __name__ == '__main__':
    main()
#!/usr/bin/python3



def statsDict(inputTupleList, test_start, test_end):
    """
    Function recieves a list of namedtuples, which are the Inputs, the begining and end date, calculates stats and
    prints them

    :param inputTupleList: Named tuple list
    :param test_start: ctime()
    :param test_end: ctime()
    :return:
    """


    #Defining counting vars
    number_of_misses = 0
    number_of_hits = 0
    test_duration = 0
    number_of_types = 0
    type_hit_total_duration = 0
    type_miss_total_duration = 0
    print('Here are your stats:')

    #Accounting for each letter typed
    for i in inputTupleList:
        test_duration += i[2] #Add each typing duration to the total
        number_of_types += 1 #Increase the number of types by 1 for each letter

        if (i[1] == i[0]):
            number_of_hits += 1
            type_hit_total_duration += i[2]

        else:
            number_of_misses += 1
            type_miss_total_duration += i[2]

    accuracy = number_of_hits/number_of_types
    type_average_duration = test_duration/number_of_types

    #In case of there being no hits, there is no "hit average duration"
    if (number_of_hits == 0):
        type_hit_average_duration = None

    else:
        type_hit_average_duration = type_hit_total_duration/number_of_hits

    #The same thing happens for the average miss duration
    if (number_of_misses == 0):
        type_miss_average_duration = None

    else:
        type_miss_average_duration = type_miss_total_duration / number_of_misses


    #Defining the dictionary
    my_dict = {
        'accuracy': accuracy,
        'inputs': inputTupleList,
        'number_of_hits': number_of_hits,
        'number_of_types': number_of_types,
        'test_duration': test_duration,
        'test_end': test_end,
        'test_start': test_start,
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration}

    for key in my_dict:
        if (key == "inputs"):
            print('inputs : [')
            for i in inputTupleList:
                print(i)
            print(']')
        else:
            print(key, ':', my_dict[key])
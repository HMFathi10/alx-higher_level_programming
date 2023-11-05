#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    count = 0
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_string = new_string[:i - count] + my_string[i + 1:]
            count += 1
    return (new_string)

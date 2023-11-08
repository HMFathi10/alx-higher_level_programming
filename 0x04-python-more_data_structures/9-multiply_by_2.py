#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = a_dictionary.copy()
    new_keys = list(new_list.keys())
    for i in new_keys:
        new_list[i] *= 2
    return (new_list)

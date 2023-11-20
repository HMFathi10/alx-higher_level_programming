#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    try:
        for idx in range(x):
            print("{}".format(my_list[idx]), end="")
            result += 1
        print()
    except:
        print()
    finally:
        return (result)

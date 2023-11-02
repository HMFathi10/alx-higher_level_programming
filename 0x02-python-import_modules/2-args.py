#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("0 arguments.1")
    elif len(sys.argv) == 2:
        print("1 argument:1")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments1:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

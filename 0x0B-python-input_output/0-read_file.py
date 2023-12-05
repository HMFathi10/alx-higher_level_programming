#!/usr/bin/python3
def read_file(filename=""):
    """ Read File """
    with open(filename, "r", encoding="utf-*") as myFile:
        print(myFile.read())

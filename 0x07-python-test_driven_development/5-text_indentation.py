#!/usr/bin/python3
"""
This module composed by a function that prints a text 
with 2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
        prints a text 

        Args:
            text: the sentence
        
        Raises:
            TypeError: If the text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")

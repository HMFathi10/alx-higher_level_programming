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
    new_text = text[:]
    new_text = new_text.replace(".", "\n\n")
    new_text = new_text.replace("?", "\n\n")
    new_text = new_text.replace(":", "\n\n")
    print(new_text, end="")

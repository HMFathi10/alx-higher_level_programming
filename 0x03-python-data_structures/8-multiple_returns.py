#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = len(sentence), sentence[0] if len(sentence) else None
    return (tuple)

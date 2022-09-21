#!/usr/bin/python3
""" indents text """


def text_indentation(text):
    """ indentator """
    if type(text) != str:
        raise TypeError("text must be a string")

    punctuationWasFound = False
    for i in range(len(text)):
        if punctuationWasFound:
            if text[i] == " ":
                continue
            punctuationWasFound = False
            continue
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            punctuationWasFound = True
            print()
            print()

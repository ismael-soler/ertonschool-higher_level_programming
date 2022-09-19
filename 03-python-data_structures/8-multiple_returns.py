#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ""):
        return (0, "None")
    firstChar = sentence[:1]
    sentenceLength = len(sentence)
    newTuple = (sentenceLength, firstChar)
    return newTuple

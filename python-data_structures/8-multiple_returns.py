#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == None):
        return
    firstChar = sentence[:1]
    sentenceLength = len(sentence)
    newTuple = (sentenceLength, firstChar)
    return newTuple
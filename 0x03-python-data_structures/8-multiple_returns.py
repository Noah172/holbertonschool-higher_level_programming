#!/usr/bin/python3
def multiple_returns(sentence):
    if(sentence == "") or (sentence is None):
        return (0, None)

    s = len(sentence)
    return (s, sentence[0])

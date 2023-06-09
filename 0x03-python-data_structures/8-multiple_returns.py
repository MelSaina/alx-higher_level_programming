#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns the length and the  first character of a string."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

def simple_delete(a_dictionary, ky=""):
    if ky in a_dictionary:
        del a_dictionary[ky]
    return a_dictionary

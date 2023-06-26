#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = 0
    new_l = []
    result = 0
    for n in range(0, list_length):
        try:
            result = (my_list_1[n] / my_list_2[n])
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_l.append(result)
    return new_l

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dt = a_dictionary.copy()
    for ky in nw_dt.keys():
        nw_dt[ky] *= 2
    return nw_dt

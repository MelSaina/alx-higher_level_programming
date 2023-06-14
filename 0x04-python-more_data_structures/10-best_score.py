#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary !=  None:
        student_num = len(a_dictionary.values())
        if student_num > 0:
            score = max(a_dictionary.values())
            for ky in a_dictionary.keys():
                if a_dictionary[ky] == score:
                    return ky
    return None

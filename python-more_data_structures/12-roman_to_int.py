#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    # rtoi = roman to integer (or arabic)
    rtoi = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    suma = 0
    for i in range(len(roman_string)):
        if (i > 0) and (rtoi[roman_string[i]] > rtoi[roman_string[i - 1]]):
            suma += rtoi[roman_string[i]] - rtoi[roman_string[i - 1]] * 2
            continue
        suma += rtoi[roman_string[i]]
    return suma

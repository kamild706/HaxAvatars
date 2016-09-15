#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 The program allows you to convert numbers within different bases
 Run the program from console with no parameters to see built-in tutorial
 $ python NumberBaseConverter.py
"""

from sys import argv
import os

__author__ = "Matt23"
__copyright__ = "Copyright 2016"
__license__ = "MIT"


def convert_number(number, old_base, new_base):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # all available characters the value can be written in
    written_as_decimal = 0  # decimal representation of given number

    if old_base > 36 or new_base > 36:
        return "Numbers based on systems grater than 36 are not supported\nPlease provide proper values"

    # converting number to the 10 based system and checking its correctness
    for exponent, i in enumerate(number[::-1]):
        if characters.index(i) >= old_base:
            return "Value {} is not written in {} based system, conversion impossible".format(number, old_base)
        written_as_decimal += characters.index(i) * old_base ** exponent

    # converting number to the requested base
    converted_number = ""
    while written_as_decimal >= 1:
        converted_number += characters[written_as_decimal % new_base]
        written_as_decimal //= new_base

    return "{}({}) = {}({})".format(number, old_base, converted_number[::-1], new_base)

if len(argv) != 4:
    message = "Number Base Converter expects 3 parameters:\n" \
              "-- The number to be converted\n" \
              "-- Base the number is written in\n" \
              "-- Base the number will be written in\n" \
              "------------------------------------------\n" \
              "Example usage: python {} DEAD 16 10\n" \
              "Output: DEAD(16) = 57005(10)\n" \
              "---------------------------".format(os.path.basename(__file__))
    print(message)
else:
    print(convert_number(str(argv[1]).upper(), int(argv[2]), int(argv[3])))

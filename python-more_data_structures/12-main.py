#!/usr/bin/python3
""" Test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

print(roman_to_int("IV"))
if type(roman_to_int("I")) is not int:
    print("Doesn't return an integer")
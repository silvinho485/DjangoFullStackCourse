#!/bin/python3

import sys

def testType(string):
    try:
        int(string)
    except ValueError:
        string = "Bad String"
    return string

S = "não é um numero"
print(testType(S))
# try:
#     print(testType(S))
# except ValueError:
#     print('Bad String')

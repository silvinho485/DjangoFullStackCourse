#!/bin/python3.5
def swap_case(string):
    return ''.join([(letter.lower() if letter.isupper() else letter.upper()) for letter in string])

if __name__ == '__main__':
    s = "UUUlll"
    result = s
    print(result)

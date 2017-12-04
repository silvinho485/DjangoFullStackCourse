#!/bin/python

import sys


def biggest_sum(arr):
    summer = 0
    for counter in range(1, len(arr)):
        summer += arr[counter]
        print(counter)
    return summer

def littlest_sum(arr):
    summer = 0
    for counter in range(0, len(arr)-1):
        summer += arr[counter]
        print(counter)
    return summer

arr = map(int, raw_input().strip().split(' '))
arr.sort()

print(littlest_sum(arr), biggest_sum(arr))

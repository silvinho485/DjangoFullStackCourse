#!/bin/python3.5
import sys

class Solution:
    def __init__(self, queue = [], stack = []):
        self._queue = queue
        self._stack = stack

    def pushCharacter(self, char):
        if char == ' ':
            pass
        else:
            self._stack.append(char.lower())
        
    def enqueueCharacter(self, char):
        if char == ' ':
            pass
        else:
            self._queue.insert(0, char.lower())

    def popCharacter(self):
        return self._stack.pop()

    def dequeueCharacter(self):
        return self._queue.pop()


s=input()

obj=Solution()

l=len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True

for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")


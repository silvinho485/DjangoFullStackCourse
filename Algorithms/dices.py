#!/bin/python3
import random

class Dice:
    amount = 6
    def __init__(self, faces=[(x) for x in range(amount)]):
        self._faces = faces


    @property
    def faces(self):
        return self._faces

    @faces.setter
    def faces(self, newval):
        print("Setting new faces")
        self._faces = [(x) for x in range(newval)]

    def play(self):
        return random.choice(self.faces)
    
    def __str__(self):
        return "{} faces".format(self.faces)

    

dado = Dice()
dado.play()

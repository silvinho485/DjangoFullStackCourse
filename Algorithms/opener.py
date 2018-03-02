#!/bin/python3
import os.path

file_path = os.path.join(os.path.dirname(__file__), 'foo.txt')
myfile = open(file_path, "r")
cont = myfile.read()
print(cont)
myfile.close()

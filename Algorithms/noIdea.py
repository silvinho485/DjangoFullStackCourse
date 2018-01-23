#!/bin/python3.5

n, m = input("n e m - ").split()
elements = input("elements - ").split()
a = set(input("A - ").split())
b = set(input("B - ").split())
print(sum([(1 if x in a else (-1 if x in b else 0))for x in elements]))

# 3, 2 = Quantos elementos terão no Array / Quantos terão nos arrays a calcular.
# 1 5 3 = numeros a serem calculados.
# 3 1 = Array gostavel
# 5 7 = Array desgostavel

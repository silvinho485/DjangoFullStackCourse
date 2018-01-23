#!/bin/python3
#List comprehension example:
x, y, z, n = int(1), int(1), int(1), int(2)
arr = [[a, b, c]
       for a in range(0, x+1)
       for b in range(0, y+1)
       for c in range(0, z+1)
       if a + b + c != n]
print(arr)
#====================================

#
# #Classical example
# x = int(1)
# y = int(1)
# z = int(1)
# n = int(2)
# ar = []
# p = 0
# for i in range ( x + 1 ) :
#     for j in range( y + 1):
#         for k in range(z + 1):
#             if i+j+k != n:
#                 ar.append([])
#                 ar[p] = [ i , j , k]
#                 p+=1
# print(ar)
# #====================================

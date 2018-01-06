#!/bin/python3.5
names = ["Harry","Berry","Tina","Akriti","Harsh",]
scores = [37.21,37.21,37.2,41,39]
marksheet = list(zip(names, scores))
second_lowest = sorted(set(marksheet))[1][1]
print("\n".join([(name) for name, mark in marksheet if mark == second_lowest]))




# marksheet = list(zip(names, scores))
# print('\n'.join([(names) for names, scores in marksheet\
#                  if scores == sorted(set(marksheet))[1][1]]))

# names = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
# scores = [37.21, 37.21, 37.2, 41, 39]
# marksheet = list(zip(names, scores))
# second_lower = sorted(set(marksheet))[1][1]
# print('\n'.join([(names)for names, scores in marksheet if scores ==second_lower]))


 # nested = list(zip(names, scores))
    # nested.sort(key=lambda x:x[1])
    # print(nested[1])
    # less = nested[0][1]
    # lessers = []
    # for finder in nested:
    #     if finder[1] > less:
    #         less = finder[1]
    #         break

    # for finder in nested:
    #     if finder[1] == less:
    #         lessers.append(finder[0])

    # for x in sorted(lessers):
    #     print(x)

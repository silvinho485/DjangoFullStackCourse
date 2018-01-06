#!/bin/python3.5
inputers = [
     "Krishna 67 68 69",
     "Arjun 70 98 63",
     "Malika 52 56 60",]
mydict = {line.split()[0]:sum(map(float, line.split()[1:]))/len(line.split()[1:]) for line in inputers}

print(mydict['Malika'])
print(mydict['Arjun'])
print(mydict['Krishna'])
#print(mydict[input("Digite um nome para a consulta da nota media: ")])



# my_dict = {line.split()[0] : sum(map(float, line.split()[1:]))/len(line.split()[1:]) for line in inputers}
# mydict = {line.split()[0]:sum(map(int, line.split()[1:]))/3
#           for line in [input() for _ in range(int(input()))]}

# for grabber in inputers:
#     name, *mark = grabber.split()
#     mark = sum(int(x) for x in mark) /3
#     mydict[name] = mark

# print(mydict["Arjun"])

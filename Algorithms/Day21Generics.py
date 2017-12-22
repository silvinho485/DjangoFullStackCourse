#!/bin/python3.5

# class Commands:
#     def appender(array, args):
#         return self.array.append(int(self.args))

#     def inserter(array, args):
#         return self.array.insert(*map(int self.args))
    
#     def printer(array):
#         print(self.array)

#     def remove(array, args):
#         return self.array.remove(*map(int, args))
    
#     def popper(array, args):
#         return self.array.pop(int(args))

#     def reverser(array):
#         return self.array.reveres()

# interpr = Commands()
# my_dict = {
#     'insert':interpr.inserter,
# }

class Nome:
    def nomes(self, nome):
        return "Hello {}".format(nome)

silvio = Nome()
printadeira = getattr(silvio, 'nomes')("Silvinho da 47")

    
my_list = []
commands = [
    'insert 0 5',
    'insert 1 10', 
    'insert 0 6',
    'print ',
    'remove 6',
    'append 9',
    'append 1',
    'sort ',
    'print',
    'pop',
    'reverse',
    'print',
]

for command in commands:
    method, *args = command.split()
    if method != "print":
        function = getattr(my_list, method)
        function(*map(int, args))
    else:
        print(my_list)

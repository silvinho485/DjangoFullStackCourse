##!/bin/python3

currentRoom = 1
inventory = []
rooms = {
    1 : {'name':'Hall',
         'south':3,
         'east':2},
    2: {'name':'Bedroom',
        'west':1,
        'south':4,
        'item':'sword'},
    3 : {'name':'Kitchen',
         'north':1},
    4 : {'name':'Bathroom',
         'north':2}
}

print("you are in the room " + str(currentRoom))
print("This is the " + rooms[currentRoom]['name'])


def showStatus():
    print("-"*10)
    print("You're in the " + rooms[currentRoom]['name'])
    if 'item' in rooms[currentRoom]:
        print('You see an ' + rooms[currentRoom]['item'])
    print("-"*10)
    
while True:
    showStatus()
    move = input("Select room: ").lower().split()
    # curentRoom = rooms[currentRoom][move]
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")

    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] == rooms[currentRoom]['item']:
            inventory.append(move[1])
            print('{} got!'.format(rooms[currentRoom]['item']))
            del rooms[currentRoom]['item']
        else:
            print("Can't get {}!".format(rooms[currentRoom]['item']))

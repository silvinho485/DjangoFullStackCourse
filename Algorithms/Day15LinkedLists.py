#!/bin/python3.5
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        node = Node(data)
        if head is None:
            head = node
        else:
            current = head
            while(current.next is not None):
                current = current.next
            current.next = node
        return head

if __name__ == "__main__":

    mylist= Solution()
    T=int(4)
    head=None
    a = [2,3,4,1]
    for i in a:
        data=int(i)
        head=mylist.insert(head,data)
    mylist.display(head);


# class No:
#     def __init__(self, carga=None, proximo=None):
#         self._carga = carga
#         self._proximo = proximo


#     def __str__(self):
#         return "Carga {}\nProxima {}".format(self._carga, self._proximo)


# if __name__ == '__main__':
#     no3 = No(3)
#     no2 = No(2, no3)
#     no1 = No(1, no2)
#     no3._proximo = no1

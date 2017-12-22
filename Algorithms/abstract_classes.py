from abc import ABCMeta, abstractmethod
class Book(object):
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass


class MyBook(Book):
    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title, author)
        self.price = price

    def __str__(self):
        return "Title: {}\nAuthor: {}\nPrice: {}".format(
            self.title, self.author, self.price
        )
    
    def display(self): 
        print("Title: {}\nAuthor: {}\nPrice: {}".format(
            self.title, self.author, self.price

        ))


        
#Python 3 example
# from abc import ABCMeta, abstractmethod
# class Book(object, metaclass=ABCMeta):
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author   
#     @abstractmethod
#     def display(): pass
# class MyBook(Book):
#     def __init__(self, title, author, price):
#         super().__init__(title, author)
#         self.price = price

#     def display(self): 
#         print("Title: {}\nAuthor: {}\nPrice: {}".format(
#             self.title, self.author, self.price
#         ))

title="The alchemist"
author="Paulo Coelho"
price=int(248)
new_novel=MyBook(title,author,price)
new_novel.display()

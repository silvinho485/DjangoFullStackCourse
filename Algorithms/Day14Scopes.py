class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = abs(min(self.__elements)-max(self.__elements))

_ = 4
a = [1,2,5]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

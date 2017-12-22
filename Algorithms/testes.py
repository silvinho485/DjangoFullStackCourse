class Vehicle (object):
    def __init__(self, tires, engine=False):
        super(Vehicle, self).__init__()
        self._tires = tires
        self._engine = engine

    def ride(self):
        print "Riding..."

    def __str__(self):
        return "Number of tires: {}\nEngine: {}".format(self._tires, self._engine)

class Bike(Vehicle):
    def __init__(self, tires, engine=False, cilinders=1):
        super(Bike, self).__init__(tires, engine)
        self._cilinders = cilinders


    def cortar_giro(self):
        print "braananananananana"

class Quadbike(Bike):
    def __init__(self, tires, engine=True, cilinders=1, seats=2):
        super(Quadbike, self).__init__(tires, engine, cilinders)
        self._seats = seats

    def __str__(self):
        return "Tires: {}\nEngine: {}\nCilinders: {}\nSeats: {}".format(
            self._tires, self._engine, self._cilinders, self._seats
        )
    

# class Quadbike(Bike):
#     def __init__(self, tires, engine=True, cilinder=1, seats=2):
#         super().__init__(tires, engine, cilinders)
#         self._seats = seats

        
if __name__ == '__main__':
    bicicle = Vehicle(2)

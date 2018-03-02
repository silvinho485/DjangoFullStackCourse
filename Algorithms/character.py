class Character(object):

    def __init__(self, name, hp, atk):
        self._name = name
        self._hp = hp
        self._atk = atk

    def get_atr(self):
        return self._name

    @property
    def name(self):
        print('Getting name...')
        return self._name

    @name.setter
    def name(self, new_name):
        print('Setting name...')
        self._name = new_name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        self._hp = new_hp

    @property
    def atk(self):
        return self._atk

    @atk.setter
    def atk (self, new_atk):
        self._atk = new_atk

    def __str__(self):
        return ("Name:   {}\n"
                "HP:     {}\n"
                "Attack: {}").format(self._name,
                                     self._hp,
                                     self.atk)

if __name__ == '__main__':

    cat = Character("Fido", 5, 2)
    print(cat)

    dog = Character("Scooby", 7, 3)
    print(dog)

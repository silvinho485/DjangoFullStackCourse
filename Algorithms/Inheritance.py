#!/bin/python3

class Veiculo:
    def __init__(self, rodas=2, cor="branco"):
        self.rodas = rodas
        self.cor = cor

    def eu (self):
        print("Sou um veiculo!")

    def serial(self, numero):
        self.numero = numero
        return "Numero de série: {}".format(self.numero)

    def __str__(self):
        return "{} rodas, cor {}".format(self.rodas, self.cor)


class Carro(Veiculo):
    def __init__(self, rodas, cor, motor=True):
        super().__init__(rodas, cor)
        self.motor = motor

    def eu (self):
        print("Sou um carro!")
        super().eu()

    def __str__(self):
        return "{} rodas, cor {}, motor: {}".format(self.rodas, self.cor, self.motor)
    
if __name__ == '__main__':
    bicicleta = Veiculo()
    caloi = Veiculo(3, 'amarela')
    uno = Carro(4, 'preto')
    
    print(bicicleta)
    print(caloi)
    print(uno)
    bicicleta.eu()
    uno.eu()

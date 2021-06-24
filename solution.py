import random
import math
from sat import Sat

TEMPERATURA_MINIMA = 0.001

class estado():
    def __init__(self, bit_array, value):
        self.bit_array = bit_array
        self.value = value

class Solution(Sat):
    def __init__(self, temperaturainicial, resfriamento, lacointerno, file):
        super(Solution, self).__init__(file)
        self.temperaturainicial = temperaturainicial
        self.resfriamento = resfriamento
        self.lacointerno = lacointerno

    def pegarvizinhos(self, state):
        new_bit_array = list(state.bit_array)
        random_position = random.randint(0, self.num_variaveis - 1)
        new_bit_array[random_position] = (new_bit_array[random_position] + 1) % 2

        num_naosatisfativeis, num_satisfativeis, ehsat = self.clausulasvdd(new_bit_array)

        new_value = num_satisfativeis

        return estado(new_bit_array, new_value)

    def estadoaleatorio(self):
        return estado([0 for i in range(self.num_variaveis)], 0)

    def resfria(self, temperatura):
        return temperatura * self.resfriamento

    @staticmethod
    def checkcongelou(temperatura):
        return temperatura > TEMPERATURA_MINIMA    

    def get_qtd(self, estado):
        new_bit_array = list(estado.bit_array)
        return self.clausulasvdd(new_bit_array)

    def makeestado(self, estado):
        return estado(estado)

    def evaluate(self, ehvetornulo):
        if ehvetornulo:
            estadonulo = [0 for i in range(self.num_variaveis)]
            estado = self.makeestado(estadonulo)
            return self.get_qtd(estado)
        else:
            estado = self.makeestado(self.estadofile)
            return self.get_qtd(estado)

    def SimulatedAnnealing(self):
        estado = self.estadoaleatorio()
        temperatura = self.temperaturainicial

        best_estado = None

        while self.checkcongelou(temperatura):
            for i in range(self.lacointerno):
                neighbor = self.pegarvizinhos(estado)
                if neighbor.value > estado.value:
                    estado = neighbor
                elif math.e**((neighbor.value - estado.value)/temperatura) >= random.random():
                    estado = neighbor

                if not best_estado:
                    best_estado = estado
                elif best_estado.value < estado.value:
                    best_estado = estado

            temperatura = self.resfria(temperatura)
        return best_estado
import random
import math
from sat import Sat

TEMPERATURA_MINIMA = 1

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

    def pegarvizinhos(self, estado):
        new_bit_array = list(estado.bit_array)
        random_position = random.randint(0, self.variables_count - 1)
        new_bit_array[random_position] = (new_bit_array[random_position] + 1) % 2

        c, w = self.get_ratios(new_bit_array)
        new_value = (self.ratio*c) + ((1-self.ratio)*w)
        return estado(c, w, new_value, new_bit_array)

    def estadoaleatorio(self):
        return estado([0 for i in range(self.variables_count)], 0)

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

            temperatura = self.resfria(temperatura)
        return best_estado
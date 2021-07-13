import random
from random import randint
import math
from sat import Sat
import matplotlib.pyplot as plt

TEMPERATURA_MINIMA = 0.001

class estado():
    def __init__(self, bit_array, custo, sat, ehsat):
        self.bit_array = bit_array
        self.custo = custo
        self.sat = sat
        self.ehsat = ehsat

class Solution(Sat):
    def __init__(self, resfriamento, lacointerno, file):
        super(Solution, self).__init__(file)
        self.temperaturainicial = self.tempinicial()
        self.resfriamento = resfriamento
        self.lacointerno = lacointerno

    def pegarvizinhos(self, state):
        new_bit_array = list(state.bit_array)
        random_position = random.randint(0, self.num_variaveis - 1)
        new_bit_array[random_position] = (new_bit_array[random_position] + 1) % 2

        num_naosatisfativeis, num_satisfativeis, ehsat = self.objetivo(new_bit_array)

        new_custo = num_naosatisfativeis

        return estado(new_bit_array, new_custo, num_satisfativeis, ehsat)

    def estadoaleatorio(self):
        array = [randint(0, 1) for i in range(self.num_variaveis)]
        array = list(array)
        num_naosatisfativeis, num_satisfativeis, ehsat = self.objetivo(array)
        return estado(array, num_naosatisfativeis, num_satisfativeis, ehsat)
       #return estado([0 for i in range(self.num_variaveis)], 0)

    def resfria(self, temperatura):
        return temperatura * self.resfriamento

    @staticmethod
    def checkcongelou(temperatura):
        return temperatura > TEMPERATURA_MINIMA    

    def tempinicial(self):
        estado = self.estadoaleatorio()
        energias = []
        k = randint(1, 100)
        j = 0
        best_estado = None

        while j < k:
            neighbor = self.pegarvizinhos(estado)
            E = neighbor.custo - estado.custo
            if (E > 0):
                energias.append(E)
                j = j + 1
        temperatura = 4.48*(sum(energias)/k)        
        return temperatura

    def SimulatedAnnealing(self):
        estado = self.estadoaleatorio()
        temperatura = self.temperaturainicial
        estados = []
        iteracoes = []
        t = 0

        best_estado = None

        while self.checkcongelou(temperatura):
            for i in range(self.lacointerno):
                neighbor = self.pegarvizinhos(estado)
                E = neighbor.custo - estado.custo

                if E < 0:
                    estado = neighbor
                elif math.e**(-E/temperatura) >= random.random():
                    estado = neighbor

                if not best_estado:
                    best_estado = estado
                elif best_estado.custo > estado.custo:
                    best_estado = estado

            temperatura = self.resfria(temperatura)
            iteracoes.append(t)
            estados.append(estado.custo)
            t = t + 1
            
        #plt.plot(iteracoes, estados)
        #plt.title("3-SAT Simulated Annealing")
        #plt.xlabel('Iterações')
        #plt.ylabel('Custo')
        #plt.show()    
        return best_estado, self.num_clausulas
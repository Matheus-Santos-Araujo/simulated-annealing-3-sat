from solution import Solution
import time
import math

class File(list):

    def __init__(self, path):
        self = [self.append(x) for x in File.load(path)]

    @staticmethod
    def load(path):
        with open(path) as f:
            return f.readlines()

def solve(temperaturainicial, resfriamento, lacointerno, files):
    for file in files:
        solution = Solution(temperaturainicial, resfriamento, lacointerno, File(file))
        inicio = time.time()
        sa = solution.SimulatedAnnealing()
        duracao = time.time() - inicio
    return sa, duracao

def main():
    
    iter = 0
    resfriamento = 0.001
    temperaturainicial = 1000
    #temperaturainicial = 4.48 * E
    lacointerno = 200
    arquivocnf = ["SAT1.txt"]
    #arquivocnf = ["SAT2.txt"]
    #arquivocnf = ["SAT3.txt"]
    
    while (iter < 100):
        sa, duracao = solve(temperaturainicial, resfriamento, lacointerno, arquivocnf)

        print("Melhor solucao = ")
        print(sa.bit_array)
        print("Clausulas Satisfeitas = %d" % sa.value)
        print("Duracao: %f" % duracao)
        iter = iter + 1

if __name__ == '__main__':
    main()

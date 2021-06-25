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

def solve(resfriamento, lacointerno, files):
    for file in files:
        solution = Solution(resfriamento, lacointerno, File(file))
        inicio = time.time()
        sa, qtd = solution.SimulatedAnnealing()
        duracao = time.time() - inicio
    return sa, duracao, qtd

def main():
    
    iter = 0
    alpha = 0.8
    temperaturainicial = 2.5
    #temperaturainicial = 4.48 * E
    lacointerno = 200
    arquivocnf = ["SAT1.txt"]
    #arquivocnf = ["SAT2.txt"]
    #arquivocnf = ["SAT3.txt"]
    
    while (iter < 1):
        sa, duracao, qtd = solve(alpha, lacointerno, arquivocnf)

        print("Melhor solucao = ")
        print(sa.bit_array)
        print("Custo = %d" % sa.value)
        print("Total de Clausulas: %d" % qtd)
        print("Clausulas Satisfeitas: %d" % sa.sat)
        porcentagem = (sa.sat/qtd)* 100
        print("Porcentagem: %f%%" % porcentagem)
        print("E SAT?: %s" % str(sa.ehsat))
        print("Duracao: %f" % duracao)
        iter = iter + 1

if __name__ == '__main__':
    main()

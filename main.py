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
        sa, qtd, inicial, minimo, media = solution.SimulatedAnnealing()
        duracao = time.time() - inicio
    return sa, duracao, qtd, inicial, minimo, media

def main():
    
    iter = 0
    alpha = 0.98
    lacointerno = 1000
    arquivocnf = ["SAT1.txt"]
    #arquivocnf = ["SAT2.txt"]
    #arquivocnf = ["SAT3.txt"]
    #arquivocnf = ["SAT4.txt"]
    #arquivocnf = ["NM1.txt"]
    #arquivocnf = ["NM2.txt"]
    #arquivocnf = ["NM3.txt"]
    #arquivocnf = ["NM4.txt"]
    
    while (iter < 1):
        sa, duracao, qtd, inicial, minimo, media = solve(alpha, lacointerno, arquivocnf)

        print("Melhor solucao = ")
        print(sa.bit_array)
        print("Custo = %d" % sa.custo)
        print("Total de Clausulas: %d" % qtd)
        print("Melhor: %d" % sa.sat)
        print("Inicial: %d" % inicial)
        print("Minimo: %f" % minimo)
        print("Media: %f" % media)
        porcentagem = (sa.sat/qtd)* 100
        print("GAP: %f" % (sa.sat/qtd))
        print("Porcentagem: %f%%" % porcentagem)
        print("E SAT?: %s" % str(sa.ehsat))
        print("Tempo: %f" % duracao)
        iter = iter + 1

if __name__ == '__main__':
    main()

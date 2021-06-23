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

def solve(ehvetornulo, temperaturainicial, resfriamento, lacointerno, files):
    for file in files:
        solution = Solution(File(file))
        inicio = time.time()
        sa = solution.SimulatedAnnealing(temperaturainicial, resfriamento, lacointerno, files)
        duracao = time.time() - inicio
    return sa, duracao

def main():
    #arquivocnf = ["SAT2.txt"]
    #arquivocnf = ["SAT3.txt"]
    ehvetornulo = False
    #ehvetornulo = True
    
    resfriamento = 0.001
    temperaturainicial = E / math.log(0.8)
    lacointerno = 200
    arquivocnf = ["SAT1.txt"]
    
    resultqtd, resultehsat, duracao = solve(arquivocnf)

    if resultehsat:
        print("F(X) = %d SAT" % resultqtd)
        print("Duracao: %f" % duracao)
    else:
        print("F(X) = %d unSAT" % resultqtd)
        print("Duracao: %f" % duracao)

if __name__ == '__main__':
    main()

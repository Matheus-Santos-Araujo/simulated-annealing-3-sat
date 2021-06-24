class Sat(object):
    def __init__(self, file):
        self.clausulas = []
        for line in file:
            if line == file[0]:
                meta_data = line.split()
                self.num_variaveis = int(meta_data[0])
                self.num_clausulas = int(meta_data[1])
            elif line == file[-1]:
                self.statefile = [l.rstrip() for l in line]
                self.statefile.pop()
                self.statefile = [int(i) for i in self.statefile]
            else:
                clausula = []
                for var in line.split()[:]:
                    clausula.append(int(var))
                if len(clausula) == 3:
                    self.clausulas.append(clausula)

    def objetivo(self, bits):
        num_satisfativeis = 0
        num_naosatisfativeis = 0
        ehsat = True
        for clausula in self.clausulas:
            if Sat.ehsatisfativel(clausula, bits):
                num_satisfativeis += 1
            else:
                ehsat = False
                num_naosatisfativeis += 1    

        return num_naosatisfativeis, num_satisfativeis, ehsat

    @staticmethod
    def ehsatisfativel(clausula, bits):
        for x in clausula:
            if (x > 0 and bits[abs(x)-1]) or (x < 0 and not bits[abs(x)-1]):
                return True
        return False

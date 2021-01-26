

class Entity:
    def __init__(self,gene):
        self._gene = gene
        self._Efitness = 0

    def fitness(self,but):
        for i in range(len(self._gene)):
            if self._gene[i] == but[i]:
                self._Efitness += 1


    def get_fitness(self):
        return self._Efitness


    def to_string(self):
        return " gene = "+ self._gene+" \n"+" fitness = "+str(self._Efitness)



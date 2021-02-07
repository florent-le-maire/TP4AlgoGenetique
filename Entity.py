import random
import string
from GlobalEntity import GlobalEntity


class Entity(GlobalEntity):
    def __init__(self,gene):
        self._gene = gene
        self._Efitness = 0

    def fitness(self,but):
        self._Efitness = 0
        for i in range(len(self._gene)):
            if self._gene[i] == but[i]:
                self._Efitness += 1
        self._Efitness /= len(self._gene)
        # self._Efitness = random.random()

    def cross_over(self, entity2):
        cut = round(len(self._gene) / 2)
        return Entity(self._gene[:cut] + entity2.get_gene()[cut:])

    def mutation_gene(self):
        mut_indice = round(random.random() * (len(self._gene)-1))
        mot_tmp = list(self._gene)
        mot_tmp[mut_indice] = random.choice(string.ascii_letters + string.whitespace)
        self._gene = ''.join(mot_tmp)

    def get_fitness(self):
        return self._Efitness

    def get_gene(self):
        return self._gene

    @staticmethod
    def get_random_global_entity(list_obj):
        letters = string.ascii_letters + string.whitespace
        return ''.join(random.choice(letters) for i in range(len(list_obj)))

    def to_string(self):
        return "[ gene = "+ self._gene+" "+" fitness = "+str(self._Efitness)+"]"



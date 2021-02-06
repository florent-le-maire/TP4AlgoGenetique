import random
import string
from Ville import Ville

class EntityVille:
    def __init__(self,gene):
        self._gene = gene
        self._Efitness = 0

    def fitness(self):
        self._Efitness = 0
        for i in range(0,len(self._gene)):
            deux = (i+1)%len(self._gene)
            self._Efitness += self._gene[i].get_distance_entre_ville(self._gene[deux])
        return 1/self._Efitness


    def mutation_gene(self):
        list1 = random.sample(range(len(self._gene)-1), 2)
        mut_ville_1 = list1[0]
        mut_ville_2 = list1[1]


    def get_fitness(self):
        return self._Efitness

    def get_gene(self):
        return self._gene


    def to_string(self):
        return "[ gene = "+ self._gene+" "+" fitness = "+str(self._Efitness)+"]"



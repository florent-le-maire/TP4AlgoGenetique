import random
import string
from GlobalEntity import GlobalEntity


class EntityVille(GlobalEntity):
    def __init__(self, gene):
        self._gene = gene
        self._Efitness = 0

    def fitness(self, but=None):
        self._Efitness = 0
        for i in range(0, len(self._gene)):
            deux = (i + 1) % len(self._gene)
            self._Efitness += self._gene[i].get_distance_entre_ville(self._gene[deux])
        self._Efitness = (1 / self._Efitness)

    def cross_over(self, ville2):
        portion = random.sample(range(len(self._gene)), 2)
        portion.sort()
        copyList = []
        copyList[:] = self._gene
        list_tmp = []
        list_tmp[:] = ville2._gene
        set1 = set(x.get_id() for x in copyList[portion[0]:portion[1]])
        t = [x for x in list_tmp if x.get_id() not in set1]

        copyList[:portion[0]] = t[:portion[0]]
        copyList[portion[1]:] = t[portion[0]:]
        return EntityVille(copyList)

    def mutation_gene(self):
        swapList1 = random.sample(range(len(self._gene)), 2)
        vTmp = self._gene[swapList1[0]]
        self._gene[swapList1[0]] = self._gene[swapList1[1]]
        self._gene[swapList1[1]] = vTmp

    def get_fitness(self):
        return self._Efitness

    def get_gene(self):
        return self._gene

    @staticmethod
    def get_random_global_entity(list_obj):
        random.shuffle(list_obj)
        return list_obj
    
    def conditionDarret(self,i,listDesE,nbGen):
        mean = 0
        value = 0
        for ville in listDesE:
            ville.fitness()
            value += ville.get_fitness()
        
        mean = value / len(listDesE)
        
        print(mean)
            
        return i < nbGen and listDesE[0].get_fitness() != mean and listDesE[0].get_fitness() != 1


    def to_string(self):
        string = ""
        for v in self._gene:
            string += str(v.get_id())
        return "[ gene = " + string + " " + " fitness = " + str(self._Efitness) + "]"

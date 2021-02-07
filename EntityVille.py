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
        return 1 / self._Efitness

    def cross_over(self, ville2):
        portion = random.sample(range(len(self._gene)), 2)
        portion.sort()
        copyList = []
        copyList[:] = self._gene
        list_tmp = []
        list_tmp[:] = ville2._gene
        print(portion[0], portion[1])
        set1 = set(x.get_id() for x in copyList[portion[0]:portion[1]])
        t = [x for x in list_tmp if x.get_id() not in set1]

        copyList[:portion[0]] = t[:portion[0]]
        copyList[portion[1]:] = t[portion[0]:]
        return copyList

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
    def get_random_global_entity(length):
        letters = string.ascii_letters + string.whitespace
        return ''.join(random.choice(letters) for i in range(length))

    def to_string(self):
        return "[ gene = " + self._gene + " " + " fitness = " + str(self._Efitness) + "]"

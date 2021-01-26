import random
import string
from Entity import Entity


def tri_ins(t, j=1):
    if j < len(t):
        insere(t, j)
        tri_ins(t, j + 1)


def insere(t, j):
    if j > 0 and t[j] < t[j - 1]:
        t[j - 1], t[j] = t[j], t[j - 1]
        insere(t, j - 1)


class CycleDeLaVie:
    def __init__(self, pop, tmut, tsel, objectif):
        self._tauxDeMutation = tmut
        self._nombreDePop = pop
        self._tauxDeSelection = tsel  # en pourcentage
        self._objectif = objectif
        self.listDesEntity = []  # La liste en public pour faire des test il faut la mettre en privé
        self.construction_ecosystem()

    def selection(self):
        copy_des_entity = [];
        for e in self.listDesEntity:
            e.fitness(self._objectif)

        copy_des_entity[:] = self.listDesEntity
        self.tri_ins(copy_des_entity)

        nombre_entity_garder = round( (len(self.listDesEntity) * self._tauxDeSelection)/100)

        self.listDesEntity[:] = copy_des_entity[:nombre_entity_garder]

    def tri_ins(self, t, j=1):
        if j < len(t):
            self.insere(t, j)
            self.tri_ins(t, j + 1)

    def insere(self, t, j):
        if j > 0 and t[j].get_fitness() > t[j - 1].get_fitness():
            t[j - 1], t[j] = t[j], t[j - 1]
            self.insere(t, j - 1)

    def crossover(self):
        copyList = []
        copyList[:] = self.listDesEntity
        cut = round(len(self._objectif)/2)
        for i in range(0,len(self.listDesEntity),2):
            if i+1 < len(self.listDesEntity):
                self.listDesEntity.append(Entity(copyList[i].get_gene()[:cut]+copyList[i].get_gene()[cut:]))
                self.listDesEntity.remove(copyList[i])
                self.listDesEntity.remove(copyList[i+1])

    @staticmethod
    def mutation():
        print("je fais la mutation")

    def go(self):
        self.selection()
        self.crossover()

    def construction_ecosystem(self):
        for i in range(self._nombreDePop):
            self.listDesEntity.append(Entity(self.get_random_string(len(self._objectif))))

    @staticmethod
    def get_random_string(length):
        letters = string.printable
        return ''.join(random.choice(letters) for i in range(length))

    def printList(self):
        for e in self.listDesEntity:
            print(e.to_string())


m = CycleDeLaVie(10, 1, 70, "SALUT")
m.go()



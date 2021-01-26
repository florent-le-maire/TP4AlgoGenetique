import random
import string
from Entity import Entity


class CycleDeLaVie:
    def __init__(self, pop, tmut, tsel, objectif):
        self._tauxDeMutation = tmut
        self._nombreDePop = pop
        self._tauxDeSelection = tsel
        self._objectif = objectif
        self.listDesEntity = []  # La liste en public pour faire des test il faut la mettre en privé
        self.construction_ecosystem()

    @staticmethod
    def selection():
        print("tt")

    @staticmethod
    def crossover():
        print("je fais le crossoveur")

    @staticmethod
    def mutation():
        print("je fais la mutation")

    @staticmethod
    def go():
        print("je jeu commence")

    def construction_ecosystem(self):
        for i in range(self._nombreDePop):
            self.listDesEntity.append(Entity(self.get_random_string(len(self._objectif))))

    @staticmethod
    def get_random_string(length):
        letters = string.printable
        return ''.join(random.choice(letters) for i in range(length))


m = CycleDeLaVie(10, 1, 1, "SALUT")
for e in m.listDesEntity:
    print(e.to_string())

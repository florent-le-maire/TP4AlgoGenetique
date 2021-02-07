import random
import string
from Entity import Entity
from EntityVille import EntityVille
from Ville import Ville


# def tri_ins(t, j=1):
#     if j < len(t):
#         insere(t, j)
#         tri_ins(t, j + 1)
#
#
# def insere(t, j):
#     if j > 0 and t[j] < t[j - 1]:
#         t[j - 1], t[j] = t[j], t[j - 1]
#         insere(t, j - 1)


class CycleDeLaVie:
    def __init__(self, pop, tmut, tsel, objectif):
        self._tauxDeMutation = tmut
        self._nombreDePop = pop
        self._tauxDeSelection = tsel  # en pourcentage
        self._objectif = objectif
        self.listDesEntity = []  # La liste en public pour faire des test il faut la mettre en privé
        self.construction_ecosystem()

    def selection(self):
        copy_des_entity = []
        for e in self.listDesEntity:
            e.fitness(self._objectif)

        copy_des_entity[:] = self.listDesEntity
        self.tri_insertion(copy_des_entity)
        copy_des_entity.reverse()
        nombre_entity_garder = round((len(self.listDesEntity) * self._tauxDeSelection) / 100)

        self.listDesEntity[:] = copy_des_entity[:nombre_entity_garder]

    def tri_insertion(self, L):
        N = len(L)
        for n in range(1, N):
            cle = L[n]
            j = n - 1
            while j >= 0 and L[j].get_fitness() > cle.get_fitness():
                L[j + 1] = L[j]  # decalage
                j = j - 1
            L[j + 1] = cle

    def crossover(self):
        copyList = []
        copyList[:] = self.listDesEntity
        # cut = round(len(self._objectif) / 2)
        for i in range(0, len(copyList), 2):
            if i + 1 < len(copyList):
                self.listDesEntity.append(copyList[i].cross_over(copyList[i+1]))
                # self.listDesEntity.remove(copyList[i])
                # self.listDesEntity.remove(copyList[i+1])

    def mutation(self):
        for i in range(len(self.listDesEntity)):
            r = round(random.random() * 100)
            if r <= self._tauxDeMutation:
                self.listDesEntity[i].mutation_gene()
                self.listDesEntity[i].fitness(self._objectif)

    def go(self):
        i = 0
        while i < 1000 and self.listDesEntity[0].get_fitness() != 1:
            print("generation " + str(i) + " nombre d'habitant " + str(len(self.listDesEntity)))
            print("individu 0 est " + self.listDesEntity[0].to_string())
            # self.printList()
            self.selection()
            # print("fin de la selection")
            # self.printList()
            self.crossover()
            # print("fin du crossover")
            # self.printList()
            self.mutation()
            # print("fin de la mutation")
            # self.printList()

            i += 1

    def construction_ecosystem(self):
        for i in range(self._nombreDePop):
            self.listDesEntity.append(Entity(Entity.get_random_global_entity(len(self._objectif))))

    def print_list(self):
        for e in self.listDesEntity:
            print(e.to_string())


m = CycleDeLaVie(500, 50, 67, "Je vend une renault peugeaot")
m.go()
print(m.listDesEntity[0].to_string())

# e = Entity("nuy")
# e.fitness("baa")
# print(e.get_fitness())
# list = [Ville(1, 1, "Paris", 1), Ville(2, 1, "Montpellier", 2), Ville(1, 2, "Lyon", 4), Ville(2, 2, "Toulouse", 3)]
# list2 = [Ville(1, 1, "Paris", 2), Ville(2, 1, "Montpellier", 1), Ville(2, 2, "Toulouse", 3), Ville(1, 2, "Lyon", 4)]
# e = EntityVille(list)
# e2 = EntityVille(list2)
# e.cross_over(e2)
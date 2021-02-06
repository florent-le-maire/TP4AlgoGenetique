import random


def fusion(L1, L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    if i1 < n1:
        while i1 < n1:
            L12[i] = L1[i1]
            i1 += 1
            i += 1
    else:
        while i2 < n2:
            L12[i] = L2[i2]
            i2 += 1
            i += 1
    return L12


def tri_fusion_recursif(L):
    n = len(L)
    if n > 1:
        p = int(n / 2)
        L1 = L[0:p]
        L2 = L[p:n]
        print("sépration : ", L1, L2)
        tri_fusion_recursif(L1)
        tri_fusion_recursif(L2)
        L[:] = fusion(L1, L2)
        print("fusion : ", L)


def tri_fusion(L):
    M = list(L)
    tri_fusion_recursif(M)
    return M

    # def tri_ins(self, t, j=1):
    #     if j < len(t):
    #         self.insere(t, j)
    #         self.tri_ins(t, j + 1)
    #
    # def insere(self, t, j):
    #     if j > 0 and t[j].get_fitness() > t[j - 1].get_fitness():
    #         t[j - 1], t[j] = t[j], t[j - 1]
    #         self.insere(t, j - 1)





from math import *


class Ville:
    def __init__(self, x, y, nom, id):
        self._x = x
        self._y = y
        self._nom = nom
        self._id = id

    def get_distance_entre_ville(self, ville2):
        dist = sqrt((ville2._x - self._x) ** 2 + (ville2._y - self._y) ** 2)
        return dist

    def get_id(self):
        return self._id

    def to_string(self):
        return "[ coord = " + str(self._x) + ',' + str(self._y) + " " + " id = " + str(self._id) + "]"

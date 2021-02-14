from abc import ABC, abstractmethod, abstractproperty


class GlobalEntity(ABC):

    @abstractmethod
    def fitness(self, but): pass

    @abstractmethod
    def cross_over(self, entity2): pass

    @abstractmethod
    def mutation_gene(self): pass

    @abstractmethod
    def get_fitness(self): pass

    @abstractmethod
    def get_gene(self): pass

    @staticmethod
    @abstractmethod
    def get_random_global_entity(list_obj): pass

    @abstractmethod
    def to_string(self): pass

    @abstractmethod
    def conditionDarret(self,i,listDesE,nbGen): pass
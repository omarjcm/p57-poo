from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass

class Humano(Animal):
    def mover(self):
        print('Yo puedo caminar, correr y saltar.')

    def imprimirHumano(self, nombre, apellido):
        print( f'{nombre} {apellido}' )


humano = Humano()
humano.imprimirHumano('Guillermo', 'Pizarro')
humano.mover()

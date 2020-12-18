class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    def avanza(self):
        print( 'Estoy caminando...' )


class Ciclista( Persona ):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print( 'Ando en mi bicicleta...' )

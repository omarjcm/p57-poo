class Persona:
    def __init__(self, cedula, nombre, apellido):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido


class Estudiante( Persona ):
    def __init__(self, cedula, nombre, apellido, quintil):
        super().__init__(cedula, nombre, apellido)
        self._quintil = quintil

    @property
    def quintil(self):
        return self._quintil

    @quintil.setter
    def quintil(self, quintil):
        self._quintil = quintil


class Docente( Persona ):
    def __init__(self, cedula, nombre, apellido, esTitular):
        super().__init__(cedula, nombre, apellido)
        self._esTitular = esTitular

    @property
    def esTitular(self):
        return self._esTitular

    @esTitular.setter
    def esTitular(self, esTitular):
        self._esTitular = esTitular

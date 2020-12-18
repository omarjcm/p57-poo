class Autor:
    def __init__(self, idAutor, nombre, apellido, esPrincipal):
        self._idAutor = idAutor
        self._nombre = nombre
        self._apellido = apellido
        self._esPrincipal = esPrincipal

    @property
    def idAutor(self):
        return self._idAutor

    @idAutor.setter
    def idAutor(self, idAutor):
        self._idAutor = idAutor

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

    @property
    def esPrincipal(self):
        return self._esPrincipal

    @esPrincipal.setter
    def esPrincipal(self, esPrincipal):
        self._esPrincipal = esPrincipal

class Libro:
    def __init__(self, isbn, titulo, editorial):
        self._isbn = isbn
        self._titulo = titulo
        self._editorial = editorial
        self.ref_copiaLibros = []

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial

    def reservar(self):
        print( "Reserva del libro {} de la Editorial {}.".format(self._titulo, self._editorial) )

    def prestar(self):
        print( "Préstamo del libro {}.".format(self._titulo) )

    def devolver(self):
        print( "Devolución del libro {}.".format(self._titulo) )

    def imprimir(self):
        print("Título: {}".format(self._titulo))
        print("ISBN: {}".format(self._isbn))
        print("Editorial: {}".format(self._editorial))

class CopiaLibro:
    def __init__(self, idCopiaLibro, estado):
        self._idCopiaLibro = idCopiaLibro
        self._estado = estado

    @property
    def idCopiaLibro(self):
        return self._idCopiaLibro

    @idCopiaLibro.setter
    def idCopiaLibro(self, idCopiaLibro):
        self._idCopiaLibro = idCopiaLibro

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

class Libro:
    def __init__(self, codigo, titulo, isbn, editorial):
        self._codigo = codigo
        self._titulo = titulo
        self._isbn = isbn
        self._editorial = editorial
    
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

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
        print("Código: {}".format(self._codigo))
        print("Título: {}".format(self._titulo))
        print("ISBN: {}".format(self._isbn))
        print("Editorial: {}".format(self._editorial))
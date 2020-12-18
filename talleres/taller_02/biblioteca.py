from libro import Libro
from autor import Autor

if __name__ == "__main__":
    libro = Libro('UPS-GYE-001', 'Los tres Mosqueteros', 'ISBN123456789', 'Murcia')
    libro.codigo = 'UPS-GYE-001'
    libro.reservar()

    libro.imprimir()

    print( id(libro) )
    a = 7
    print(a)

    print( id(a) ) 

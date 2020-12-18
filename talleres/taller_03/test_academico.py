from academico import *

docente1 = Docente('0937564039', 'Guillermo', 'Pizarro', False)
docente2 = Docente('0948562839', 'Omar', 'Vásquez', True)

docentes = [ docente1, docente2 ]

for docente in docentes:
    print( "La cédula del profesor {} {} es {}.".format(docente.nombre, docente.apellido, docente.cedula) )

estudiante = Estudiante('0948572039', 'Karina', 'Ascencio', True)
print( "La cédula del estudiante {} {} es {}.".format(estudiante.nombre, estudiante.apellido, estudiante.cedula) )
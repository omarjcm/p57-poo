from biblioteca import *

libro = Libro('ISBN2398475', 'Programación en Python', 'Ra-Ma')
libro.ref_copiaLibros.append( CopiaLibro( 1, 'BUEN_ESTADO' ) )
libro.ref_copiaLibros.append( CopiaLibro( 2, 'BUEN_ESTADO' ) )
libro.ref_copiaLibros.append( CopiaLibro( 3, 'MAL_ESTADO' ) )

libro.imprimir()
for copiaLibro in libro.ref_copiaLibros:
    print( " - " + copiaLibro.estado )
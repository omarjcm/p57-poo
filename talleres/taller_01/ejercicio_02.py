def imprimir_escalera(numero_maximo):
    for numero in range(1, numero_maximo+1):
        for j in range(1, (numero_maximo-numero)+1):
            print( " ", end="" )
        print( numero )

imprimir_escalera(10)
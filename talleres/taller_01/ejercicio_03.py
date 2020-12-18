numero_maximo = 10

for numero in range(1, numero_maximo+1):
    for j in range(1, (numero_maximo-numero)+1):
        print( " ", end="" )
    for k in range(1, numero+1):
        print( numero, end="" )
    print()

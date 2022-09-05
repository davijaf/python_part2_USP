def ordenada(lista):
    for i in range(len(lista)):
        if len(lista) > 1 and lista[i] != lista[-1]:
            if lista[i]>lista[i+1]:
                return False
    return True

#lista1 = [-432, 0, 33, 900, 55, 10, 77, 2, 11]
#print(ordenada(lista1))
#lista2 = [-432, 0, 2, 10, 11, 33, 55, 77, 900]
#print(ordenada(lista2))
#lista3 = [7]
#print(ordenada(lista3))
#lista4 = [55, 10, 77, 2, 11]
#print(ordenada(lista4))

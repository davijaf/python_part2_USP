def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

#listas = [10,20,30,40]
#print(soma_lista(listas))
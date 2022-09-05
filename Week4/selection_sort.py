def ordena(lista):

    finish = len(lista)

    for i in range(finish - 1):
        minimal_position = i

        for j in range(i+1, finish):
            if lista[j] < lista[minimal_position]:
                minimal_position = j
        lista[i], lista[minimal_position] = lista[minimal_position], lista[i]
    return lista
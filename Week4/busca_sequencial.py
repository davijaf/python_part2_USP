def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

#print(busca(['a', 'e', 'i'], 'e'))
# deve devolver => 1

#print(busca([12, 13, 14], 15))
# deve devolver => False

#print(busca([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 100))

#print(busca([100], 100))
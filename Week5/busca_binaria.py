def busca(lista, elemento):
    first = 0
    last = len(lista)-1
    while first <= last:
        quite = (first + last)//2
        print(quite)
        if lista[quite] == elemento:
            return quite
        else:
            if elemento < lista[quite]:
                last = quite - 1
            else:
                first = quite + 1
    return False

#print(busca(['a', 'e', 'i'], 'e'))
#print(busca([1, 2, 3, 4, 5], 6))
#print(busca([1, 2, 3, 4, 5, 6], 4))
#print(busca([1], 4))
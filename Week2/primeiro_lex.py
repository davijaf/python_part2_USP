def primeiro_lex(lista):
    names_sorted = []
    for name in range(len(lista)):
        names_sorted.append(lista[name].strip())
    names_sorted = sorted(names_sorted)
    lowerName = names_sorted[0]
    #print(names_sorted)
    return lowerName

primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'

primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'
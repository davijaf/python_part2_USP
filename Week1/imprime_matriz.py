def imprime_matriz(minha_matriz):
    for i in range(len(minha_matriz)):
        x = minha_matriz[i]
        y = ""
        for j in range(len(x)):
            y += str(x[j])
            if j < len(x)-1:
                y += " "
        print(y)

minha_matriz = [[1, 2, 3], [4, 5, 6], [4, 5, 6]]
imprime_matriz(minha_matriz)
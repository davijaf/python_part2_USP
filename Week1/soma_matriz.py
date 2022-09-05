def dimensoes(matriz):
    i = len(matriz)
    j = len(matriz[0])
    iXj = str(i)+"X"+str(j)
    return iXj

def soma_matrizes(m1, m2):
    dm1 = dimensoes(m1)
    dm2 = dimensoes(m2)
    if dm1 == dm2:

        m3 = []
        x = []
        y = []
        for i in range(len(m1)):
            x = m1[i]
            y = m2[i]
            line = []
            for j in range(len(x)):
                sum = x[j] + y[j]
                line.append(sum)
            m3.append(line)
        return m3
    else:
        return False

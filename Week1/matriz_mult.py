def dimensoes(matriz):
    i = len(matriz)
    j = len(matriz[0])
    iXj = str(i)+"X"+str(j)
    return iXj

def sao_multiplicaveis(m1, m2):
    if type(m1)==str:
        dm1 = m1
        dm2 = m2
    else:
        dm1 = dimensoes(m1)
        dm2 = dimensoes(m2)
    if dm1[2] == dm2[0]:
        return True
    else:
        return False
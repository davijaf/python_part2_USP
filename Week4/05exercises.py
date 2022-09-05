#2. Question 2 O que precisa ser mudado na função abaixo para que ela retorne a posição onde o elemento se encontra dentro da lista e -1 caso ele não exista.
def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return -1

seq = [1,2,3,4,5,6,7,8,9]
x = 4
print(busca_sequencial(seq,x))

#3. Question 3 Considerando a seguinte lista numeros e algoritmo de Busca Sequencial, assinale a(s) afirmação(ões) INCORRETA(S):


def busca_sequencial2(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False

numeros = [55,33,0,900,-432,10,77,123,11]

print(busca_sequencial2(numeros,33))

#5. Question 5 Analise o algoritmo de ordenação Seleção Direta abaixo e considere a lista numeros abaixo.

def selecao_direta5(lista):
    fim = len(lista)
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
        print(lista)
    return lista

numeros = [55,33,0,900,-432,10,77,2,11]

print(selecao_direta5(numeros))
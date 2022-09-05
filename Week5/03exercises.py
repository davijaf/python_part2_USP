#1. Question 1 Depois da primeira iteração (uma passagem completa) do algoritmo de ordenação da bolha, como ficaria a lista abaixo? [5, 2, 1, 3, 4]

def bubble(list):
    last = len(list)
    k = 1
    for i in range(last-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],list[j]
                #print(list, k)
                k += 1
        print(list, k)
    print(list, k)
    return list

list  = [5, 2, 1, 3, 4]
print(bubble(list))

#2. Question 2 Quantas iterações (passagens completas) o algoritmo de ordenação da bolha (em sua versão melhorada, apresentada na vídeo-aula) faria para ordenar a lista abaixo?

def bubble_ef(list):
    last = len(list)
    k = 1
    for i in range(last-1, 0, -1):
        change = False
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],list[j]
                k += 1
                print(list, k)
                change = True
        if not change:
            #print(list)
            return list

list1  = [1, 2, 3, 5, 4]
#print(bubble_ef(list1))

#3. Question 3 Quando o algoritmo de ordenação da bolha não realiza nenhuma alteração em uma lista (não vazia) durante uma iteração completa (uma passagem por toda a lista), isto significa que:

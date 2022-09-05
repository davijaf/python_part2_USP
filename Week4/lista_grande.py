import random
def lista_grande(n):
    list = []
    for i in range(n):
        list.append(random.randint(1,10))
        #print("Unorder Lists :",lists)
    return list

#print(lista_grande(1))
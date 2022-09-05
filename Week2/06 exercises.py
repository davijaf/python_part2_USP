# 1. Question 1 Considere as strings abaixo e assinale os comandos que irão retornar TRUE.
print("Question 01",end="\n")

a = "gato"
b = "O gato subiu no telhado"
c = "telhado"
testsBool = [a > b, a != c, a > c, c == b[15:],a == b[2:6], c == b[16:],a == b[2:5],a == b]
testsStr = ["a > b", "a != c", "a > c", "c == b[15:]","a == b[2:6]", "c == b[16:]","a == b[2:5]","a == b"]

for test in range(len(testsStr)):
    if testsBool[test]:
        print(testsStr[test],"-",testsBool[test])

print(" ",end = "\n")
#2. Question 2 Assinale a alternativa que melhor descreve o funcionamento da função fazAlgo e mostra o exemplo correto de execução do código abaixo
print("Question 02",end="\n")

def fazAlgo(string):
    pos = len(string)-1
    string = string.upper()
    print("Inverte e capitaliza todas as letras -",end=" ")
    while pos >= 0:
        print(string[pos],end = "")
        pos = pos - 1

fazAlgo("paralelepipedo")

print(" ",end = "\n")
print(" ",end = "\n")
# 3. Question 3 Assinale a alternativa que melhor descreve o funcionamento da função fazAlgo e mostra o exemplo correto de execução do código abaixo
print("Question 03",end="\n")

def fazAlgo(string):
    pos = 0
    string1 = ""
    string = string.lower()
    stringMa = string.upper()
    print("Capitaliza letras alternadas -",end=" ")
    while pos < len(string):
        if pos % 2 == 0:
            string1 = string1 + stringMa[pos]
        else:
            string1 = string1 + string[pos]
        pos = pos + 1
    return string1

print(fazAlgo("paralelepipedo"))

print(" ",end = "\n")

# 4. Question 4 Para que o código abaixo imprima "Éumteste", assinale abaixo a mudança necessária.

def fazAlgo(string):
    pos = 0
    string1 = ""
    while pos < len(string):
        if string[pos] != " ":
            string1 = string1 + string[pos]
        pos = pos + 1
        string1 = string1.capitalize()
    return string1

print(fazAlgo("É UM TESTE"))
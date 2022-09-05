#for c in range(123):
#    print(str(c) + " - " + chr(c))
# A-Z 65-90

def maiusculas(frase):
    upperC = ""
    for i in range(len(frase)):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            upperC += frase[i]
    return upperC

maiusculas('Programamos em python 2?')
maiusculas('Programamos em Python 3.')
maiusculas('PrOgRaMaMoS em python!')
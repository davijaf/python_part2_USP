from re import A
from tkinter import Y


x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

def peso_altura():
    return 77, 1.83

peso, altura = peso_altura()

print(peso)
print(altura)

a = 10
b = 20
a , b = b , a
print(a)
print(b)

x = 10
x += 10
print(x)

x *= 2
print(x)

x **= 2
print(x)

def pagamentoSemanal(valorHora,hTrab = 40):
    assert valorHora > 0 and hTrab > 0
    return valorHora * hTrab

print(pagamentoSemanal(100,36))

print(pagamentoSemanal(200))

# Asserçao de variantes

print(pagamentoSemanal(-100,36))

# Question 1 Considere o método construtor da classe Cafeteira:
class Cafeteira:
  def __init__(self, marca, tipo, tamanho, cor):
    self.marca = marca
    self.tipo = tipo
    self.tamanho = tamanho
    self.cor = cor

# 2 Considere o programa abaixo:
class Cachorro:
  def __init__(self, raça, idade, nome, cor):
    self.raça = raça
    self.idade = idade
    self.nome = nome
    self.cor = cor

rex = Cachorro('vira-lata', 2, 'Bobby', 'marrom')

print(rex.nome == 'rex')
print(rex.idade > 2)
print('vira-lata' == rex.raça)
#print(Bobby.cor == 'marrom')
print(rex.idade == '2')

# 3. Question 3 Considere o seguinte programa
class Lista:
  def append(self, elemento):
    return "Oops! Este objeto não é uma lista"

lista = []
a = Lista()
b = a.append(7)
lista.append(b)

print(lista)
print(a)
print(b)
# 1. Question 1 As linhas de comando abaixo executam cálculos. Assinale as linhas que não resultam em erro e que dão o resultado da operação:

print(float("3.4") + int("10"))
print(24 * 4)
print(float("3.5") + 5)
print(7 % 4)
print(4 ^ 3)
print(22 // 5)

# 2. Question 2 O que o comando abaixo irá resultar?

print("15" + str(34))

# Question 3 O que o comando abaixo irá resultar?

print('Python!' * 5)

# 4. Question 4 Considere o comando abaixo e assinale as afirmações CORRETAS:

palavra = "Python"

print(palavra[4]) # - Retonará: 'o'
print(palavra[3]) # - Retonará: 'h'
print(palavra[0]) # - Retonará: 'P'
print(palavra) # - Retonará: 'Python'
print(palavra[-1]) # - Retonará: 'n'
print(palavra[-2]) # - Retonará: Mensagem de Erro

# 5.Question 5 Considere o comando abaixo e assinale as alternativas CORRETAS.

frase = " Python É Uma Linguagem Poderosa "
# Observação: A string acima tem um espaço em branco no início e 3 no final.

print(frase[14:]) # - Retonará: 'Linguagem Poderosa '
print(frase.lower()) # - Retonará: ' python é uma linguagem poderosa '
print(frase.replace("Poderosa", "Avançada")) # - Retonará: ' Python É Uma Linguagem Avançada '
print(frase.strip()) # - Retonará: 'Python É Uma Linguagem Poderosa'
print(frase[:6]) # - Retonará: ' Pytho'
print(frase.upper()) # - Retonará: ' PYTHON É UMA LINGUAGEM PODEROSA '

# 6. Question 6 Considere o comando abaixo e assinale a alternativa INCORRETA:

frase = "São Paulo é a maior cidade do Brasil"

print(len(frase)) # - Retonará: 36
print(frase.count("o")) # - Retonará: 4
print(frase.find("ai")) # - Retonará: 15
print(frase.find("w")) # - Retonará: False
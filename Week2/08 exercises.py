# 1. Question 1 O quê será impresso pelo código abaixo?
print("Question 01",end="\n")
x, y = 10, 12
x, y = y, x
print("x = ",x,"e y = ",y)

# 2. Question 2 Qual o resultado final impresso pelo código abaixo?
print("Question 02",end="\n")
x = 10
x += 10
x /= 2
x //= 3
x %= 2
x *= 9
print(x)

#3. Question 3 Observe o código abaixo:
print("Question 03",end="\n")
def calculo(x, y = 10, z = 5):
    return x + y * z;
######
print(calculo(1, 2, 3))
print(calculo(7, 2))
print(calculo(7))
print(calculo(0,12, 10))
#print(calculo())

#4. Question 4 O código abaixo transforma as horas, minutos e segundos passados como parâmetro em segundos:
print("Question 04",end="\n")
def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s
######
#print(horario_em_segundos(10,-10,34))
print(horario_em_segundos(3,0,50))
print(horario_em_segundos(1,2,3))
#print(horario_em_segundos(-1,20,30))
#print(horario_em_segundos(1,33,-50))
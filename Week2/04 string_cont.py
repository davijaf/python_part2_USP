x = "teoria"
y = "time"
print(x == y)

z = "teoria"
print(x is z)

# código ordinal no padrao unicode ord("letter")

#for c in range(123):
#    print(str(c) + " - " + chr(c))
sumX = ""
for i in range(len(x)):
    sumX += str(ord(x[i]))+"."
print(sumX)

sumY = ""
for i in range(len(y)):
    sumY += str(ord(y[i]))+"."
print(sumY)

print(x > y)
import requests
import time
import sys

sys.setrecursionlimit(1000000000)

def palindromo(count,digits):
    api = "https://api.pi.delivery/v1/pi?start="+str(count)+"&numberOfDigits="+str(digits)+"&radix=10"
    pi = requests.get(api)
    pi_pal = pi.json()['content']
    pi_palindrome = pi_pal[:]
    numbers = 9
    ranged = digits - numbers + 1
    printNumbers = 0
    for i in range(ranged):
        x = ""
        for d in range(numbers):
            e = i + d
            x += pi_palindrome[e]
        if x == x[::-1]:
            printNumbers += 1
            print(x)
            #arquivo = open('arq01.txt','a')
            #arquivo.write(str(x))
            #arquivo.write("\n")
            #arquivo.close()
    if printNumbers == 0:
        count += (1000 - numbers)
        #arquivo2 = open('arq02.txt','a')
        #arquivo2.write("Contador :")
        #arquivo2.write(str(count))
        #arquivo2.write("\n")
        #arquivo2.close()
        print("Contador :",count)
        palindromo(count,1000)

palindromo(0,1000)
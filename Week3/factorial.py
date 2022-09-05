def factorial(n):
    #n = int(input("Enter a positive number: "))
    #print("n","n!", end = "\t")
    #print()
    if n < 0:
        return 0
    if n >= 0:
        fatorial = 1
        while n > 1:
            fatorial = fatorial * n
            n = n - 1
    return fatorial
        #n = int(input("Enter a positive number: "))

print(factorial(-10))
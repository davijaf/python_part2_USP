

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

import pytest

@pytest.mark.parametrize("entry, value", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
])

def test_factorial(entry, value):
    assert factorial(entry) == value
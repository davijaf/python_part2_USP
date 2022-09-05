class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        self.lados = sorted([self.a, self.b, self.c])
        if self.lados[2]**2 == (self.lados[1]**2 + self.lados[0]**2):
            return True
        else:
            return False
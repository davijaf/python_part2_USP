class Triangulo:
    def __init__(self, a, b, c):
        self.lados = sorted([a, b, c])

    def semelhantes(self,triangulo):
        x = triangulo.lados
        r = [False, False, False]
        for i in range(3):
            if x[i] > self.lados[i]:
                if x[i] % self.lados[i] == 0:
                    r[i] = True
            else:
                if self.lados[i] % x[i] == 0:
                    r[i] = True
        if r[0] + r[1] + r[2] == 3:
            return True
        else:
            return False

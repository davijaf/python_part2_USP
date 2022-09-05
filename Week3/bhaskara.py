import math

class Bhaskara:
    def main(self):
        a = float(input("Input cofficient a : "))
        b = float(input("Input cofficient b : "))
        c = float(input("Input cofficient c : "))

        if c > 0 and b > 0:
            print("Equation:",a,"* x^2","+",b,"* x","+",c,"= 0")
        if c < 0 and b > 0:
            print("Equation:",a,"* x^2","+",b,"* x",c,"= 0")
        if c > 0 and b < 0:
            print("Equation:",a,"* x^2",b,"* x","+",c,"= 0")
        else:
            print("Equation:",a,"* x^2","+",b,"* x",c,"= 0")

        print(self.calc_discriminant(a,b,c))

    def discriminant(self,a,b,c):
        return (b ** 2) - (4 * a * c)

    def quadratic(self, a,b,c,d):
        return (-b + d * math.sqrt(self.discriminant(a,b,c))) / (2 * a)

    def calc_discriminant(self,a,b,c):
        if self.discriminant(a,b,c) >= 0:
            def x1(a,b,c):
                d = 1
                return self.quadratic(a,b,c,d)
            def x2(a,b,c):
                d = -1
                return self.quadratic(a,b,c,d)

            if self.discriminant(a,b,c) == 0:
                if x1(a,b,c) != x2(a,b,c):
                    #print("Roots of this function are",x1(a,b,c,d))
                    roots1 = x1(a,b,c)
                    return 1, roots1
                elif x1(a,b,c) == x2(a,b,c):
                    #print("Root of this function is",x1(a,b,c,d))
                    roots1 = x1(a,b,c)
                    return 1, roots1

            else:
                if x1(a,b,c) < x2(a,b,c):
                    #print("Function real roots are:", x1(a,b,c,d),"e",x2(a,b,c,d))
                    roots1 = x1(a,b,c)
                    roots2 = x2(a,b,c)
                    return 2, roots1, roots2

                else:
                    #print("Function real roots are:",x2(a,b,c,d),"e",x1(a,b,c,d))
                    roots1 = x1(a,b,c)
                    roots2 = x2(a,b,c)
                    return 2, roots1, roots2
        else:
            #print("Function doesn't real roots!")
            return 0
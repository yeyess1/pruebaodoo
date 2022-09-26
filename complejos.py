
class Complejo:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def sumar(self):
        sumar = self.A + self.B
        print(sumar)
    def restar(self):
        restar = self.A+self.B
        print(restar)

    def multiplicar(self):
        multiplicar = self.A+self.B
        print(multiplicar)

    def dividir(self):
        divir = self.A+self.B
        print(divir)

    def modA(self):
        mod = abs(self.A)
        print(mod)
    
    def modB(self):
        mod = abs(self.B)
        print(mod)

c1 = 2 + 2j
c2 = 1 + 5j
calcular = Complejo(c1, c2)
calcular.modA()

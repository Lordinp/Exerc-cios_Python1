import math

#Declaração de variável
A = 0.0
B = 0.0
C = 0.0

#Início
A = float(input("Digite o coeficiente de A:"))
B = float(input("Digite o coeficiente de B:"))
C = float(input("Digite o coeficiente de C:"))

delta = B**2 - 4*A*C

x1 = (-B + (delta ** 0.5)) / (2*A)
x2 = (-B - (delta ** 0.5)) / (2*A)

resultado = "%.2f".format(x1)
resultado = "%.2f".format(x2)

print(f"A Raiz 1 é:",x1)
print(f"A Raiz 2 é:",x2)
#Fim


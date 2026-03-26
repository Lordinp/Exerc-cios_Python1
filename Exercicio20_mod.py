import math
a, b, c = 0.0, 0.0, 0.0

def calcular_equacao():
    global a, b, c
    a = float(input("A: ")); b = float(input("B: ")); c = float(input("C: "))
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print("Não existem raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Raízes: x1={x1:.2f}, x2={x2:.2f}")

def main():
    calcular_equacao()

if __name__ == "__main__":
    main()

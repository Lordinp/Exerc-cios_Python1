v1, v2 = 0, 0

def calcular_diferenca():
    global v1, v2
    v1 = int(input("Digite o 1º valor: "))
    v2 = int(input("Digite o 2º valor: "))
    if v1 > v2:
        print(f"Resultado: {v1 - v2}")
    else:
        print(f"Resultado: {v2 - v1}")

def main():
    calcular_diferenca()

if __name__ == "__main__":
    main()
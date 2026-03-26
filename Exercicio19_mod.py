r1, r2 = 0.0, 0.0

def mostrar_maior():
    global r1, r2
    r1 = float(input("Digite o 1º real: "))
    r2 = float(input("Digite o 2º real: "))
    if r1 > r2:
        print(f"Maior: {r1}")
    else:
        print(f"Maior: {r2}")

def main():
    mostrar_maior()

if __name__ == "__main__":
    main()

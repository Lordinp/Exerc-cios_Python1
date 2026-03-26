v1, v2, v3, v4 = 0, 0, 0, 0

def ordenar_quatro():
    global v1, v2, v3, v4
    print("Digite 3 valores já em ordem crescente:")
    v1 = int(input("1º: ")); v2 = int(input("2º: ")); v3 = int(input("3º: "))
    v4 = int(input("Agora digite o 4º valor (qualquer): "))
    
    lista = [v1, v2, v3, v4]
    lista.sort()
    print(f"Ordenados: {lista}")

def main():
    ordenar_quatro()

if __name__ == "__main__":
    main()

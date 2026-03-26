v1, v2 = 0, 0

def verificar_multiplo():
    global v1, v2
    v1 = int(input("Valor 1: ")); v2 = int(input("Valor 2: "))
    maior, menor = max(v1, v2), min(v1, v2)
    
    if maior % menor == 0:
        print(f"{maior} é múltiplo de {menor}")
    else:
        print(f"{maior} não é múltiplo de {menor}")

def main():
    verificar_multiplo()

if __name__ == "__main__":
    main()

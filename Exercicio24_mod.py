num = 0

def verificar_divisibilidade():
    global num
    num = int(input("Digite um valor: "))
    if num % 2 == 0 and num % 3 == 0:
        print("É divisível por 2 e 3")
    else:
        print("Não é divisível por ambos")

def main():
    verificar_divisibilidade()

if __name__ == "__main__":
    main()

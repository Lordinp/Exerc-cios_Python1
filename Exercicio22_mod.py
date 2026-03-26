v1, v2 = 0, 0

def ordenar_dois():
    global v1, v2
    v1 = int(input("Valor 1: ")); v2 = int(input("Valor 2: "))
    if v1 < v2:
        print(v1, v2)
    else:
        print(v2, v1)

def main():
    ordenar_dois()

if __name__ == "__main__":
    main()

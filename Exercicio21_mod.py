n1, n2, n3, n4 = 0.0, 0.0, 0.0, 0.0
media = 0.0

def verificar_media():
    global n1, n2, n3, n4, media
    n1 = float(input("Nota 1: ")); n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: ")); n4 = float(input("Nota 4: "))
    media = (n1 + n2 + n3 + n4) / 4
    print(f"Média: {media:.2f}")
    if media >= 6.0: print("APROVADO")
    elif media >= 3.0: print("EXAME")
    else: print("RETIDO")

def main():
    verificar_media()

if __name__ == "__main__":
    main()

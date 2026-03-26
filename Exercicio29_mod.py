def calcular_investimento(tipo, valor):
    # Uso de variáveis locais para o cálculo
    if tipo == 1:
        rendimento = valor * 1.03
        print(f"Valor corrigido em Poupança: R$ {rendimento:.2f}")
    elif tipo == 2:
        rendimento = valor * 1.05
        print(f"Valor corrigido em Renda Fixa: R$ {rendimento:.2f}")
    else:
        print("Tipo de investimento inválido!")

def main():
    print("1 - Poupança | 2 - Renda Fixa")
    t = int(input("Escolha o tipo: "))
    v = float(input("Valor investido: R$ "))
    calcular_investimento(t, v)

if __name__ == "__main__":
    main()

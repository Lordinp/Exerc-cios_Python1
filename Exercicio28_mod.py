def ajustar_preco(preco_atual, venda_media):
    # Lógica de decisão baseada em parâmetros
    if venda_media < 500 or preco_atual < 30:
        novo_preco = preco_atual * 1.10  # Aumento de 10%
    elif venda_media >= 500 or preco_atual >= 30:
        novo_preco = preco_atual * 0.95  # Redução de 5%
    else:
        novo_preco = preco_atual
        
    print(f"O novo preço do produto é: R$ {novo_preco:.2f}")

def main():
    p = float(input("Preço atual: R$ "))
    v = float(input("Venda mensal média: "))
    ajustar_preco(p, v)

if __name__ == "__main__":
    main()

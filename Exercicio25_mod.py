h1, m1, h2, m2 = 0, 0, 0, 0

def calcular_duracao():
    global h1, m1, h2, m2
    h1 = int(input("Hora Início: ")); m1 = int(input("Min Início: "))
    h2 = int(input("Hora Fim: ")); m2 = int(input("Min Fim: "))
    
    inicio = (h1 * 60) + m1
    fim = (h2 * 60) + m2
    
    if fim <= inicio:
        duracao = (1440 - inicio) + fim # 1440 min = 24h
    else:
        duracao = fim - inicio
        
    print(f"Tempo total: {duracao // 60}h e {duracao % 60}min")

def main():
    calcular_duracao()

if __name__ == "__main__":
    main()

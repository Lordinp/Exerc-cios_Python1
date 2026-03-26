def calcular_velocidade(voltas, comprimento, tempo_min):
    # Processamento com variáveis locais
    distancia_total_km = (voltas * comprimento) / 1000
    tempo_horas = tempo_min / 60
    velocidade_media = distancia_total_km / tempo_horas
    
    print(f"A velocidade média é de {velocidade_media:.2f} km/h")

def main():
    v = int(input("Quantidade de voltas: "))
    c = float(input("Comprimento da pista (metros): "))
    t = float(input("Tempo de duração (minutos): "))
    # Passagem de parâmetros
    calcular_velocidade(v, c, t)

if __name__ == "__main__":
    main()

#Declaração de variável
tempo_perc = 0
vel_media = 0

tempo_perc = int(input("Digite o tempom de percurso:"))
vel_media = int(input("Digite a velocidade média:"))

Litros_Gastos = (tempo_perc*vel_media)/12

print("A quantidade de litros gastos é de:", Litros_Gastos)
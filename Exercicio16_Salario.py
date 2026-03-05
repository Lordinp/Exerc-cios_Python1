#Declaração de variável
hor_trab = 0
vlr_hora = 0
perc_desc = 0
num_descendentes = 0

#Início
hor_trab = int(input("Digite a quantidade de horas trabalhadas:"))
vlr_hora = int(input("Digite o valor ganho por hora:"))
perc_desc = int(input("Digite o percentual de desconto:"))
perc_desc = (perc_desc/100)

num_descendentes = int(input("Digite o número de decendentes:"))

Salario_bruto = (hor_trab*vlr_hora)
Salario_liq = (Salario_bruto*(perc_desc))
total_descendentes = Salario_liq + (num_descendentes*100)

print("O salário que será recebido é de:", total_descendentes)


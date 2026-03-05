#Declaração de Variável
Vlr_real1 = 0.0
Vlr_real2 = 0.0

#Início
Vlr_real1 = float(input("Digite um valor real:"))
Vlr_real2 = float(input("Digite outro valor real:"))

if Vlr_real1 > Vlr_real2 : 
    difer = (Vlr_real1 - Vlr_real2) 
else:
    difer = (Vlr_real2 - Vlr_real1)

print("A diferença dos valores é de:", difer)
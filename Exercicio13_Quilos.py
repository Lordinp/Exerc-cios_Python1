#Declaração de variável
quilo_alim = 0

#Início
quilo_alim = int(input("Digite a quanti de quilos do alimento:"))
quilo_alim_g = (quilo_alim*100)
dur_alim = (quilo_alim_g/50)

print("Com a quantidade de quilos, o alimento durará", dur_alim ,"dias")
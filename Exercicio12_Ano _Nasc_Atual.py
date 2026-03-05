#Declaração de Variável
ano_nasc = 0
ano_atual = 0

#Início
ano_nasc = int(input("Digite seu ano de nascimento:"))
ano_atual = int(input("Digite o ano atual:"))

idade = (ano_atual - ano_nasc)
idade_17_anos_futuros = (idade + 17)

print("A sua idade é", idade ,"e a idade que você terá daqui a 17 anos é", idade_17_anos_futuros)
#Fim

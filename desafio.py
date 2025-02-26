# Desafio: Cálculo de Bônus com Entrada do Usuário

CONSTANTE_BÔNUS = 1000

Nome_de_usuário = input("Digite o seu nome: ")

Valor_do_salário = float(input("Digite o seu salário: "))

Valor_do_bônus_recebido = float(input("Digite o valor do bônus recebido: "))

Valor_total_bônus = CONSTANTE_BÔNUS + Valor_do_salário * Valor_do_bônus_recebido

print(f"O usuário {Nome_de_usuário} possui o bônus de {Valor_total_bônus}")
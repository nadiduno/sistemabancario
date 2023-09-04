menu = """

[d] Depositar 
[s] Sacar
[e] Estrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":


    elif opcao == "s":

    elif opcao == "e":

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
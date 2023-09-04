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
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "s":

    elif opcao == "e":

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
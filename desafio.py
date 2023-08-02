menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES =3

aux_deposito = 0
aux_saque = 0


while True:
    opcao = input(menu)

    if opcao == "d":
        print("################ Função de Depósito ################\n")

        aux_deposito = str(input("Favor Informar o valor para depósito. => ")).replace(',','.')

        aux_deposito = float(aux_deposito)

        if aux_deposito > 0:
            saldo += aux_deposito
            extrato += (f'Valor depósitado R$ {aux_deposito: .2f}\n')
            print("\nDepósito Realizado com Sucesso!\n")
        else:
            print('\nValor digitado, NÃO Permitido!\n \nOperação NÃO Realizada')

    elif opcao == "s":
        print("################ Função de Saque ################\n")

        if numero_saque >= LIMITE_SAQUES:
            print('\nLimite de saque excedido!\n \nOperação NÃO Realizada')
        else:
            aux_saque = str(input("Favor Informar o valor para saque. => ")).replace(',','.')
            aux_saque = float(aux_saque)

            if aux_saque > 0:
                if aux_saque <= limite:
                    if aux_saque <= saldo:
                        saldo -= aux_saque
                        extrato += (f'Valor de saque R$ {aux_saque: .2f}\n')
                        numero_saque += 1
                        print("\nSaque Realizado com Sucesso!\n")
                    else:
                        print('\nSaldo Insuficiente!\n \nOperação NÃO Realizada')
                else:
                    print('\nLimite de Valor maximo excedido!\n \nOperação NÃO Realizada')
            else:
                print('\nValor digitado, NÃO Permitido!\n \nOperação NÃO Realizada')

    elif opcao == "e":
        print("################ Função de Extrato ################\n")

        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

        print("\n################ Extrato Finalizada ################\n")


    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
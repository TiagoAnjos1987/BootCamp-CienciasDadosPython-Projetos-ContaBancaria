menu = """
[d] \tDepositar
[s] \tSacar
[e] \tExtrato
[c] \tCriar Conta Corrente
[u] \tCadastar Usuário
[lu] \tListar Usuários
[lc] \tListar Contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES =3

usuarios = []
contas = []
AGENCIA = "0001"

def depositar(saldo,extrato, /):
    
    aux_deposito = str(input("Favor Informar o valor para depósito. => ")).replace(',','.')

    aux_deposito = float(aux_deposito)

    if aux_deposito > 0:
        saldo += aux_deposito
        extrato += (f'Valor depositado R$ \t{aux_deposito: .2f}\n')
        print("\n########## Depósito Realizado com Sucesso! ##########\n")
    else:
        print('\n@@@@@@@@@@@@ Valor digitado, NÃO Permitido! @@@@@@@@@@@@\n \n@@@@@@@@@@@@ Operação NÃO Realizada @@@@@@@@@@')

    return saldo, extrato

def sacar(*,saldo,limite,numero_saque,limite_saque,extrato):
    if numero_saque >= limite_saque:
        print('\n@@@@@@@@@@ Limite de saque excedido! @@@@@@@@@@\n \n@@@@@@@@@@ Operação NÃO Realizada @@@@@@@@@@')
    else:
        aux_saque = str(input("Favor Informar o valor para saque. => ")).replace(',','.')
        aux_saque = float(aux_saque)

        if aux_saque > 0:
            if aux_saque <= limite:
                if aux_saque <= saldo:
                    saldo -= aux_saque
                    extrato += (f'Valor de saque R$ \t{aux_saque: .2f}\n')
                    numero_saque += 1
                    print("\n########## Saque Realizado com Sucesso! ##########\n")
                else:
                    print('\n@@@@@@@@@@ Saldo Insuficiente! @@@@@@@@@@\n \n@@@@@@@@@@ Operação NÃO Realizada @@@@@@@@@@')
            else:
                print('\n@@@@@@@@@@ Limite de Valor maximo excedido! @@@@@@@@@@\n \n@@@@@@@@@@ Operação NÃO Realizada @@@@@@@@@@')
        else:
            print('\n@@@@@@@@@@ Valor digitado, NÃO Permitido! @@@@@@@@@@\n \n@@@@@@@@@@ Operação NÃO Realizada @@@@@@@@@@')

    return saldo, extrato, numero_saque

def exibir_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: \tR$ {saldo:.2f}")

def cadastar_usuario(usuarios):
    usuario = {"Nome":"","Data de Nascimento":"","CPF":"","Endereço":""}
    cpf_existente = False
    cpf = int(input("\nDigite o CPF do Usuário, somente numeros\t"))
    cpf = str(cpf)
            
    # print("Checando se o CPF é existente: ") 

    for user in usuarios:
        if cpf == user["CPF"]:
            cpf_existente = True

    if not cpf_existente:
        nome = input("\nDigite o Nome do Usuário\t").title()
        data_nascimento = input("\nDigite data de nascimento, formato dd/mm/yyyy\t").lower()
        lagradouro = input("\nDigite o nome da rua\t").title()
        numero = input("\nDigite o número do endereço\t").upper()
        bairro = input("\nDigite o Bairro\t").title()
        cidade = input("\nDigite a cidade\t").title()
        estado = input("\nDigite o Estado com duas Siglas\t").upper()
        endereco = lagradouro + ", " + numero + " - " + bairro + " - " + cidade + "/" + estado
        usuario["Nome"] = (nome)
        usuario["Data de Nascimento"] = (data_nascimento)
        usuario["CPF"] = (cpf)
        usuario["Endereço"] = (endereco)
        usuarios.append(usuario)
        print("\n########## Usuário Cadastrado com Sucesso! ##########n")
    else:
        print('\n@@@@@@@@@@ Usuário Já Cadastrado no Sistema! @@@@@@@@@@\n \n@@@@@@@@@@ Operação NÃO Realizada @@@@@@@@@@')
    
    return usuarios

def criar_conta_corrente(contas):
    usuario = []
    conta = {"Agencia":"","Conta Corrente":"","Nome Usuário":"","CPF Usuário":""}
    cpf_existente = False
    cpf = int(input("\nDigite o CPF do Usuário, somente numeros\t"))
    cpf = str(cpf)
            
    # print("Checando se o CPF é existente: ") 

    for user in usuarios:
        if cpf == user["CPF"]:
            cpf_existente = True
            break

    if cpf_existente:
        qtdDeItens = len(contas)
        conta["Agencia"] = (AGENCIA)
        conta["Conta Corrente"] = (qtdDeItens + 1)
        conta["Nome Usuário"] = (user["Nome"])
        conta["CPF Usuário"] = (user["CPF"])
        contas.append(conta)
        print()
        print(conta)
        print("\n########## Conta Criada com Sucesso! ##########n")
        
    else:
        print('\n@@@@@@@@@@ Usuário NÃO Cadastrado no Sistema! @@@@@@@@@@\n \n@@@@@@@@@@ Operação NÃO Realizada @@@@@@@@@@')

    return contas


while True:
    opcao = input(menu)

    if opcao == "d": 
        print("################ Função de Depósito ################\n")

        retorno_depositar = depositar(saldo, extrato)
        saldo = retorno_depositar[0]
        extrato = retorno_depositar[1]
        
    elif opcao == "s":
        print("################ Função de Saque ################\n")

        retorno_sacar = sacar(saldo=saldo,limite=limite,numero_saque=numero_saque,limite_saque=LIMITE_SAQUES,extrato=extrato)
        saldo = retorno_sacar[0]
        extrato = retorno_sacar[1]
        numero_saque = retorno_sacar[2]

    elif opcao == "e":

        print("################ Função de Extrato ################\n")

        retorno_extrato = exibir_extrato(saldo,extrato=extrato)

        print("\n################ Extrato Finalizada ################\n")

    elif opcao == "c":
        print("################ Função Criar Conta ################\n")
        contas = criar_conta_corrente(contas=contas)

    elif opcao == "u":
        print("################ Função Criar Usuário ################\n")
        usuarios = cadastar_usuario(usuarios = usuarios)

    elif opcao == "lu":
        print("################ Função Listar Usuários ################\n")
        for user in usuarios:
            print(user)

    elif opcao == "lc":
        print("################ Função Listar contas ################\n")
        for c_c in contas:
            print(c_c)
                   
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
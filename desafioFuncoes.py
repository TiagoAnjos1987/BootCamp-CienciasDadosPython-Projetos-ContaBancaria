menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Conta Corrente
[u] Cadastar Usuário
[lu] Listar Usuários
[lc] Listar Contas
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

def depositar(saldo,extrato):
    
    aux_deposito = str(input("Favor Informar o valor para depósito. => ")).replace(',','.')

    aux_deposito = float(aux_deposito)

    if aux_deposito > 0:
        saldo += aux_deposito
        extrato += (f'Valor depósitado R$ {aux_deposito: .2f}\n')
        print("\nDepósito Realizado com Sucesso!\n")
    else:
        print('\nValor digitado, NÃO Permitido!\n \nOperação NÃO Realizada')

    return saldo, extrato

def sacar(saldo,limite,numero_saque,limite_saque,extrato):
    if numero_saque >= limite_saque:
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

    return saldo, extrato

def exibir_extrato(saldo,extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def cadastar_usuario(usuarios):
    usuario = []
    cpf_existente = False
    cpf = int(input("Digite o CPF do Usuário, somente numeros\n"))
    cpf = str(cpf)
            
    # print("Checando se o CPF é existente: ") 

    for user in usuarios:
        if (cpf in user): 
            cpf_existente = True

    if not cpf_existente:
        nome = input("Digite o Nome do Usuário\n").title()
        data_nascimento = input("Digite data de nascimento, formato dd/mm/yyyy\n").lower()
        lagradouro = input("Digite o nome da rua\n").title()
        numero = input("Digite o número do endereço\n").upper()
        bairro = input("Digite o Bairro\n").title()
        cidade = input("Digite a cidade\n").title()
        estado = input("Digite o Estado com duas Siglas\n").upper()
        endereco = lagradouro + ", " + numero + " - " + bairro + " - " + cidade + "/" + estado
        usuario.append(nome)
        usuario.append(data_nascimento)
        usuario.append(cpf)
        usuario.append(endereco)
        usuarios.append(usuario)
        print("\n################ Usuário Cadastrado com Sucesso! ################\n")
    else:
        print('\nUsuário Já Cadastrado no Sistema!\n \nOperação NÃO Realizada')
    
    return usuarios

def criar_conta_corrente(contas):
    usuario = []
    conta = []
    cpf_existente = False
    cpf = int(input("Digite o CPF do Usuário, somente numeros\n"))
    cpf = str(cpf)
            
    # print("Checando se o CPF é existente: ") 

    for user in usuarios:
        if (cpf in user): 
            cpf_existente = True

    if cpf_existente:
        qtdDeItens = len(contas)
        conta.append(AGENCIA)
        conta.append(qtdDeItens + 1)
        conta.append(user)
        contas.append(conta)
        print()
        print(conta)
        print("\n################ Conta Criada com Sucesso! ################\n")
        
    else:
        print('\nUsuário NÃO Cadastrado no Sistema!\n \nOperação NÃO Realizada')

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
    
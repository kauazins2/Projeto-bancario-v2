import textwrap

def menu():
    menu = """

    [d] \tDepositar
    [s] \tSaldo
    [e] \tExtrato
    [g] \tSaque
    [nc] \tNova Conta
    [nu] \tNovo Usuario
    [lc] \tListar Contas
    [q] \tSair

    => """

    return input(textwrap.dedent(menu))

def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado: \t R${valor:.2f}\n"
        print("\n == Depósito realizado com suceesso! ==")
    else:
        print("\n == Depósito com falha, tente outro valor! ==")
        
    return saldo, extrato

def saque (*, saldo, numero_saques, limite_saques, extrato, valor, limite):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_saques
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("@@@ Saldo insuficiente! @@@")
        
    elif excedeu_limite:
        print("@@@ O valor do saque atingi seu limite atual! Tente novamente. @@@")
        
    elif excedeu_saques:
        print("@@@ Numero de saques atingiu seu limite @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor: .2f}" 
        numero_saques += 1
        print("Saque realizado com sucesso")
        
    else:
        print("@@@ O valor informado não é válido @@@")
        
    
    return saldo, extrato
               
def extrato(saldo,/, *, extrato):
        print("\n======= EXTRATO =======")
        print("Não foi realizado movimentações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=======================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros)")
    usuario = filtrar_usuario(cpf, usuario)
    
    if usuario:
        print("@@@ Usuário ja existente! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informa a data de nascimento (dia / mês / ano): ")
    endereco = input("Informe o seu endereço (logradouro, número, bairro, cidade e estado")
    
    usuarios.append({"nome": nome, "data de nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Parabens! Usuário criado com sucesso")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuario)
    
    if usuario:
        print("Parabéns, conta criada com sucesso!")
        return{"agencia": agencia, "numero da conta": numero_conta, "usuario": usuario}
    print("@@@ Usuario nao foi encontrado, tente novamente! @@@")
   
def listar_contas(contas):
    for conta in contas:
        linha = f""" \
                Agência: {conta ['agencia']}
                C/C: {conta['numero_conta']}
                Titular: {conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))
               
def main():
    
    agencia = "0001"
    saldo = 0
    limite = 1500
    numero_saques = 0
    limite_saques = 5
    extrato = ""
    usuario = []
    contas = []
    #definições de variáveis

    while True:
    #utilizaremos while pois queremos gerar um loop, onde o usuario definirá quando parar    
        opcao = input(menu)
        
        if opcao == "d":
            valor = float(input("Digite um valor de deposito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)    
            
        elif opcao == "g":
            valor = float(input("Digite um valor de saque: "))
            
            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite, 
                numero_saques = numero_saques,
                limite_saques = limite_saques,
            )

        elif opcao == "s":
            print("Seu saldo: ", saldo)
            
            
                
        
        elif opcao == "e":
            extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuario)
        
        elif opcao == "nc":
            criar_conta(contas)
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuario)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "q":
            break    
        
        else:
            print("Comando inválido, por favor, selecione qual a operação desejada")
            

    main()
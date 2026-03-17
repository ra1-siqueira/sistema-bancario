
def menu():
    menu = """

    [d ]  Depositar
    [s ]  Sacar
    [e ]  Extrato
    [u ]  Criar Usuário
    [c ]  Criar Conta
    [lc]  Listar Contas
    [q ]  Sair

    => """

    return input(menu)


def criar_usuario(usuario):
    nome = input("Digite seu nome de usuário: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite seu CPF (apenas números): ")
    endereco = input("Digite seu endereço: (Cidade/ESTADO): ")

    usuario.append({"nome" : nome, "Data de Nascimento" : data_nascimento, "CPF" : cpf, "Endereço" : endereco})

    return usuario


def criar_conta(num_conta, usuario, contas):

    nome_usuario = input("Digite seu nome de usuário: ")

    for i, user in enumerate(usuario):
        if nome_usuario == usuario[i]["nome"]:
            contas.append({"Agência" : "0001", "Número da conta" : num_conta + 1,  nome_usuario : usuario})

    return contas


def listar_contas(contas):
    print(contas)



def deposit(saldo, valor, extrato, /):  
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def visualizar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuario = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposit(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == "e":
            visualizar_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            usuario = criar_usuario(usuario)

        elif opcao == "c":
            num_conta = 0
            contas = criar_conta(num_conta, usuario, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
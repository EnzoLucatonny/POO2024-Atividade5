from Conta_Bancaria import Conta_Bancaria
from Conta_Corrente import Conta_Corrente
from Conta_poupança import Conta_Poupança

print("***Bem vindo ao Banco!***")
print("1) Criar conta")
print("2) Depositar")
print("3) Sacar ")
print("4) Verificar Saldo")
print("5) Verificar Rendimento")
print("6) Aplicar Rendimento")
print("7) SAIR ")

Conta_Bancaria = []

opcao = int(input("Digite a sua opção: "))
while(opcao != 7):


    if opcao == 1:
        cpf = input("Informe o cpf do Usuario: ").strip()
        titular = int(input("Informe o titular: ")) 
        saldo = float(input("Informe o saldo do Usuario: "))
        tipo = int(input("Informe o tipo de Conta: 1) Corrente  2) Poupança: "))
        numerocc = int(input("Informe o Numero da Conta: "))
        
        if (tipo == 1):
            Usuario = Conta_Corrente(titular, cpf, saldo, numerocc)
            Conta_Bancaria.append(Usuario)
        elif (tipo == 2):
            rendimento = float(input("Digite o rendimento: "))
            Usuario = Conta_Poupança(titular, cpf, saldo, rendimento)
            Conta_Bancaria.append(Usuario)
        else:
            print("Tipo inválido")


    elif opcao == 2:
        cpf = input("Informe o cpf: ")
        for teste in Conta_Bancaria:
            if cpf == teste.cpf:
                valor = float(input("Depositar o valor: "))
                print(teste.depositar())

    elif opcao == 3:
        cpf = input("Informe o cpf: ")
        for teste in Conta_Bancaria:
            print(teste.sacar())

    elif opcao == 4:
        cpf = input("Informe o cpf: ")
        for teste in Conta_Bancaria:
            print(teste.verificar_saldo())

    elif opcao == 5:
        cpf = input("Informe o cpf: ")
        for teste in Conta_Bancaria:
            print(teste.ver_redinmento())

    elif opcao == 6:
        cpf = input("Informe o cpf: ")
        for teste in Conta_Bancaria:
            print(teste.render())

    elif opcao == 7:
            print("Finalizando Sessão!")

    elif opcao !=7:
            print("Opção não existente tente novamente!")

print("***Bem vindo ao Banco!***")
print("1) Criar conta")
print("2) Depositar")
print("3) Sacar ")
print("4) Verificar Saldo")
print("5) Verificar Rendimento")
print("6) Aplicar Rendimento")
print("7) SAIR ")
opcao = int(input("Digite a sua opção: "))
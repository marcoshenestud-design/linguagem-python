class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado!")
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        elif valor <= 0:
            print("Valor inválido!")
        else:
            self.saldo -= valor
            print("Saque realizado!")

    def ver_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

nome = input("Digite o nome do titular: ")
conta = Conta(nome)

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Valor para depositar: "))
        conta.depositar(valor)

    elif opcao == "2":
        valor = float(input("Valor para sacar: "))
        conta.sacar(valor)

    elif opcao == "3":
        conta.ver_saldo()

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
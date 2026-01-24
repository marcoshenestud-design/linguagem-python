class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, saque):
        if saque <= self.saldo:
            self.saldo -= saque
            print("Saque realizado!")
        else:
            print("Saldo insuficiente.")


    def mostrar_saldo(self):
        return f"O seu saldo atual é R$ {self.saldo:.2f}."
        

cliente = ContaBancaria('Vitor')
cliente.depositar(5845)
cliente.sacar(1000)
print(cliente.mostrar_saldo())



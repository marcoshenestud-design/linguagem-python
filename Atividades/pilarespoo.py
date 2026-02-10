# PILAR 1: ABSTRAÇÃO
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass  # Método abstrato (será implementado nas classes filhas)


# PILAR 2: ENCAPSULAMENTO
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado (encapsulado)
    
    # Getter
    def get_saldo(self):
        return self.__saldo
    
    # Setter com validação
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

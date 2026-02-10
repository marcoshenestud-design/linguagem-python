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


# PILAR 3: HERANÇA
class Cachorro(Animal):  # Herda de Animal
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama construtor da classe pai
        self.raca = raca
    
    # POLIMORFISMO: Sobrescrevendo método da classe pai
    def emitir_som(self):
        return "Au Au!"
    
    def buscar_osso(self):
        return f"{self.nome} está buscando o osso!"


class Gato(Animal):  # Também herda de Animal
    def emitir_som(self):
        return "Miau!"


# PILAR 4: POLIMORFISMO
def fazer_barulho(animal):
    print(f"{animal.nome} diz: {animal.emitir_som()}")



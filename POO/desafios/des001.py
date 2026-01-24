#DESEFIO 1

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    

eu = Pessoa('Marcos', 20)
print(eu.apresentar())


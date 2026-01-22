# Classe (molde)
class Gafanhoto:
    def __init__(self):
        self.nome = ""      # atributo
        self.idade = 0    # atributo


    def aniversario(self):    # método de instância
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


# Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())
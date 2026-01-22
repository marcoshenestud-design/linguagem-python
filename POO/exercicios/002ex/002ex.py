#MELHORANDO A NOSSAS CLASSES

# Classe (molde)
class Gafanhoto:
    """
Essa classe cria um gafanhoto, que pe uma pessoa que tem nome idade.

Papa criar uma pessoa, use
variável = Gafanhoto(nome, idade)
    """
    
    def __init__(self, nome = "vazio", idade = 0):
        self.nome = nome     # atributo
        self.idade = idade    # atributo


    def aniversario(self):    # método de instância
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


# Declaração de objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)

g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())
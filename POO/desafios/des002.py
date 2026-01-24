#DESAFIO 2

class Produto:
    def __init__(self, nome, preco): 
        self.nome = nome
        self.preco = preco

    def motrar_preco(self):
        return f"O produto {self.nome} é R${self.preco:.2f}."


produto1 = Produto('Leite', 15)
print(produto1.motrar_preco())

produto2 = Produto('Arroz', 5.21)
print(produto2.motrar_preco())
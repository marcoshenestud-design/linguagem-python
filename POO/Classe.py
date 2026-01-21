# Classe (molde)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # atributo
        self.idade = idade    # atributo

    def apresentar(self):    # método
        print(f"Oi, meu nome é {self.nome} e eu tenho {self.idade} anos.")

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos 🎉")


# Criando objetos (instâncias da classe)
pessoa1 = Pessoa("Marcos", 20)
pessoa2 = Pessoa("Ana", 25)

# Usando os métodos
pessoa1.apresentar()
pessoa1.fazer_aniversario()

pessoa2.apresentar()

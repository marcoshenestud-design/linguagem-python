#Você tem uma lista de dicionários, onde cada dicionário representa uma pessoa com nome e idade. Use a função sorted() com uma expressão lambda como chave (key) para ordenar a lista de pessoas da mais nova para a mais velha.

pessoas = {
    'Marcos': 20,
    'Carlos': 26,
    'Bob': 18,
    'Jainy': 26,
}


lista = [{'nome': nome, 'idade': idade} for nome, idade in pessoas.items()]

pessoas_ordenadas = sorted(lista, key= lambda pessoa: pessoa['idade'])
print(pessoas_ordenadas)
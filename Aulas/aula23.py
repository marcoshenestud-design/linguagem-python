#LISTAS - coleções ordenadas e MUTÁVEIS de itens

frutas = ['maçã', 'banana', 'laranja', 'abacaxi']
print(f'Lista de frutas: {frutas}')

print(f'\nA primeira fruta é {frutas[0]}')

print(f'\nA última fruta é {frutas[-1]}') #encontra a última [] da lista.

frutas.append('uva') #adiciona [] da lista
print(frutas)

frutas.remove('laranja') #remove [] da lista
print(frutas)

#MODIFICANDO UM ITEM
frutas[0] = 'morango'
print(frutas)


#CONTAR O TAMANHO DA LISTA
print(f'A lista tem {len(frutas)} frutas')

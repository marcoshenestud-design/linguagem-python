notas = [7.5, 8.0, 6.2, 9.1, 5.8, 10.0]

print(max(notas))
print(min(notas))

media = sum(notas) / len(notas)
print(media)

notas.sort(reverse=True)
print(f'Lista ordenada {notas}')
#print(len(notas)) conta a quantidade de elementos que tem dentro da lista
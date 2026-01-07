#CONJUNTOS - conjuntos são coleções não ordenadas de itens únicos e imutáveis. eles são úteis para remover duplicatas e realizar operaçãoes matemáticas de conjuntos (união e interseção)

numeros = {1, 2, 3, 4, 5}

print(f'Conjuntos de números (sem duplicatas): {numeros}')
print(type(numeros))

#ADICIONAR UM ITEM
numeros.add(6)
print(numeros)

#REMOVER UM ITEM
numeros.remove(2)
print(numeros)


##############################


#OPERAÇÕES DE CONJUNTOS
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

#união
uniao = conjunto_a.union(conjunto_b)
print(uniao)

#interseção
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)
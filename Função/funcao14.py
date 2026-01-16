#Dada uma lista de números, crie uma nova lista usando list comprehension que contenha o quadrado de cada número par da lista original.

numeros = [1, 25, 4, 98, 2, 5]
quadrado = [num**2 for num in numeros if num % 2 == 0]

print(quadrado)
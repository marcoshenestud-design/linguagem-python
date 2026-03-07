#Dada uma lista de frases, use a função map() em conjunto com uma expressão lambda para criar uma nova lista onde cada frase é convertida para letras maiúsculas e tem a palavra "PYTHON" anexada ao final.

frases = ['marcos', 'MarIo', 'OsiAs', 'MiNael']

frase = list(map(lambda frases: f'{frases.upper()} PYTHON', frases))

print(frase)

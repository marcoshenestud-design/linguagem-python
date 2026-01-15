def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]*=2
        pos +=1


valores = [7,2,5,0,4]
dobra(valores)
print(valores)

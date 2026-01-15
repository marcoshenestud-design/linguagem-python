def soma(*valores):
    s=0
    for num in valores:
        s+= num
    print(f'Somando os valores {valores} temos {s}.')

soma(5,4,1)
soma(5,79,1)
#Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

def triangulo(a,b,c):
    
    #NÃO É UM TRIÂNGULO
    if a + b <= c or a + c <= b or c + b <=a:
        print('Esse triângulo NÃO existe.')
    
    #EQUILÁTERO
    elif a==b==c:
        print('Esse triângulo é EQUILÁTERO.')
    
    #ISÓSCELES
    elif a==b or b==c or a==c:
        print('Esse triângulo é ISÓSCELES.')
    
    
    else:
        print('Esse triângulo é ESCALENO.')


print('PROGRAMA DE ANÁLISE - TRIÂNGULO')
print('-'*20)

x = float(input('Lado 1: '))
y = float(input('Lado 2: '))
z = float(input('Lado 3: '))

triangulo(x, y, z)
#Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.

def numeroint(a):
    for i in range(1,11):
        operacao = a*i
        print(f'{a} x {i} = {operacao}')

print('-' * 30)
print('VAMOS FAZER OPERAÇÃO DE MULTIPLICAÇÃO')
numero = int(input('\nDigite um número inteiro: '))

numeroint(numero)

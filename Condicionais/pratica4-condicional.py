# Faça uma calculadora que some, subtraia, multiplique ou divida

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
operação = input('Qual operação deseja realizar entre os dois números? ').lower()

if (operação== 'soma'):
    print(num1 + num2)

elif operação == 'subtracao':
    print(num1 - num2)

elif operação == 'multiplicação':
    print(num1 * num2)

elif operação == 'divisao':

    if num2 != 0:
        print(num1 / num2)

    else:
        print('Erro: divisão por zero')
        
else:
    print('Escolha entre soma, subtração, multiplicação ou divisão. ')
# Classifique o IMC de acordo com a tabela:
# Abaixo de 18.5: Abaixo do peso
# 18.5 - 24.9: Normal
# 25.0 - 29.9: Sobrepeso
# 30.0 ou mais: Obesidade

peso = float(input('Qual a sua peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso!')

elif imc >= 18.5 and imc <= 24.9:
    print('Você está com peso normal!')

elif imc >= 25 and imc <= 29.9:
    print('Você está com sobrepeso!')

else:
    print('Você está com obesidade!')
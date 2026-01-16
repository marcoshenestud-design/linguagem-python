#Crie uma função chamada calcula_imc que aceite dois argumentos: peso (em kg) e altura (em metros). A função deve calcular o Índice de Massa Corporal (IMC) usando a fórmula IMC=peso/altura^2 e retornar o valor do IMC.

def calcula_imc(peso, altura):
    imc = peso/(altura**2)
    
    return imc

print('\nCALCULADORA DE IMC')
x = float(input('\nPESO (kg): '))
y = float(input('ALTURA (metros): '))

imc = calcula_imc(x,y)
print(f'O seu IMC é {imc:.2f}')

soma = float(0)

while True:
    num = float(input('Digite um número: '))


    if num == -1:
        print('Programa encerrado!')
        break

    soma = soma + num

print('Soma total:', soma)
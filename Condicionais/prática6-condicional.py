# Receba um número de 1 a 7 e mostre o dia da semana correspondente

dia = int(input("Digite um número (1-7): "))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-Feira')
elif dia == 3:
    print('Terça-Feira')
elif dia == 4:
    print('Quarta-Feira')
elif dia == 5:
    print('Quinta-Feira')
elif dia == 6:
    print('Sexta-Feira')
elif dia == 7:
    print('Sábado')
else:
    print('ERRO: digite um número entre 1 e 7')
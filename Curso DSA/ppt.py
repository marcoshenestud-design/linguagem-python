#JOGO DE PEDRA, PAPEL E TESOURA - Projeto de certificação do curso de Python do básico a inteligência artificial.

pedro = str(input('Pedro, escolha.\nPedra, papel ou tesoura: ').upper().strip())
ana = str(input('\nVez da Ana escolher.''\nPedra, papel ou tesoura: ').upper().strip())

objetos = ['PEDRA', 'PAPEL', 'TESOURA']


if pedro in objetos and ana in objetos:
    if pedro != ana:

        #(PEDRO - ANA) - CONDIÇÕES QUE ANA VENCE

        #PEDRA - PAPEL
        if (ana == 'PEDRA' and pedro == 'TESOURA') or \
           (ana == 'PAPEL' and pedro == 'PEDRA') or \
           (ana == 'TESOURA' and pedro == 'PAPEL'):

            print('Ana venceu!')

        else:
            print('Pedro venceu!')
    else:
        print('EMPATE')
else:
    print('\nERRO!!!')
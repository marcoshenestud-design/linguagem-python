print('CONTROLE DE TERRENOS'.center(50))
print('-'*50)

def area(largura,comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento}m')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)

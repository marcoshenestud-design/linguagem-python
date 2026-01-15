################################
################################
################################
#AULA90#########################



import time


def contagem():
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1,11):
        print(i, end=' ', flush=True)
        time.sleep(0.5)
    print('FIM!')

def con2tagem():
    print('Contagem de 10 até 0 de 2 em 2')
    for a in range(10,1,-2):
        print(a, end=' ', flush=True)
        time.sleep(0.5)
    print('FIM!')


def contagemcliente(a, b):
    print('Agora é sua vez de personalizar a contagem!')
    valores = (a, b)
    for valor in range(a,b+1):
        print(valor, end=' ', flush=True)
        time.sleep(0.5)
    print('FIM!')



contagem()

con2tagem()

ini = int(input('INÍCIO: '))
fim = int(input('FIM: '))
contagemcliente(ini, fim)
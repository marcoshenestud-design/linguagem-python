primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))

for i in range (primeiro + 1, segundo):
    par = i % 2

    if par == 0:
        print(i)
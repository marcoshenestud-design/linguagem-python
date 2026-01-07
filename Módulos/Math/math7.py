# Calcule a hipotenusa de um triângulo retângulo
# com catetos 3 e 4 usando a função hypot()

#EU NÃO SABIA QUAL FUNÇÃO USAR

from math import hypot as hp

cateto1 = int(input('Cateto 1: '))
cateto2 = int(input('Cateto 2: '))
hipotenusa = hp(cateto1, cateto2)

print(f'A hipotenusa é: {hipotenusa}')
#descobrir a raio e a circunferência de círculo

from math import pi


raio = float(input('Qual o raio do círculo: '))
area = pi * (raio**2)
circunferencia = 2 * pi * raio


print(f"A área é {area} e a circunferência é {circunferencia}.")
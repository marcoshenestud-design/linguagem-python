# Verifique se 3 lados formam um triângulo e qual o tipo
# Equilátero: todos lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos lados diferentes

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 != lado2 and lado2 != lado3:
    print('Escaleno')
elif lado1 == lado2 and lado3 != lado1:
    print('Isósceles')
elif lado1 == lado3 and lado2 == lado1:
    print('Equilátero')
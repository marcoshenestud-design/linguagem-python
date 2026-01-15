#CALCULADORA DE GEOMETRIA
import math as mt

print("=== GEOMETRIA ===")
print("1. Figuras Planas \n2.Figuras Espaciais (3D)")

geo = input("\n(1) Plana ou (2) Espacial: ")



#FIGURAS PLANA
if geo == "1":
    print("==FÍGURAS PLANAS==")
    print("1. Quadrado \n2. Retângulo \n3. Triângulo \n4. Círculo \n5. Trapézio \n6. Losango")
    plana = (input("Qual figura você quer calcular a área, a diagonal (caso tenha) e o perímetro? "))

#QUADRADO
    if plana == "1":
        lado_quadrado = float(input("Qual o valor do lado do quadrado: "))

        perimetro_qua = (4 * lado_quadrado)  #:.4f
        diagonal_qua = lado_quadrado * mt.sqrt(2)
        area_qua = (lado_quadrado * lado_quadrado)

        print(f'Perimetro: {perimetro_qua:.2f}' f"\nDiagonal: {diagonal_qua:.2f}" f"\nÁrea: {area_qua:.2f}")
#RETÂNGULO
    elif plana == "2":
        lado_retangulo1 = float(input("Qual o valor de um dos lados do retângulo: "))
        lado_retangulo2 = float(input("Qual o valor do outro lado do retângulo: "))

        perimetro_ret = 2 * (lado_retangulo1 + lado_retangulo2)
        diagonal_ret = mt.sqrt(lado_retangulo2 ** 2 + lado_retangulo1 ** 2)
        area_ret = (lado_retangulo1 * lado_retangulo2)
        print(f'Perimetro: {perimetro_ret:.2f}')
        print(f'Diagonal {diagonal_ret:.2f}')
        print(f'Área: {area_ret:.2f}')
#TRIÂNGULO
    elif plana == "3":
        print("Exitem três tipos de triângulo (1) equilátero, (2) isósceles e (3) escaleno.")
        triangulo = input('Qual o seu triângulo?')


        #EQUILÁTERO
        if triangulo == '1':
            lado_tri_equi = float(input('Qual o valor do lado do triângulo: '))

            perimetro_tri_equi = 3 * lado_tri_equi
            diagonal_tri_equi = ('Triângilo não tem diagonal.')
            area_tri_equi = ((lado_tri_equi ** 2) * mt.sqrt(3)) / 4
            altura_equi = (lado_tri_equi * mt.sqrt(3)) / 2
            print(f'Perimetro do Equilátero: {perimetro_tri_equi:.2f}')
            print(f'Área do triângulo equilátero: {area_tri_equi:.2f}')
            print(f'Altura do triângulo equilátero: {altura_equi:.2f}')

        #ISÓSCELES
        elif triangulo == '2':
            lado_igual = float(input('Qual o valor dos lados iguais do triângulo: '))
            base_tri = float(input('Qual o valor da base do triângulo: '))

            altura_tri_isosc = mt.sqrt(lado_igual**2 - (base_tri / 2)**2)
            perimetro_tri_isos = 2 * lado_igual + base_tri
            area_tri_isos = (base_tri * altura_tri_isosc) / 2

            print(f'Altura do triângulo isósceles: {altura_tri_isosc:.2f}')
            print(f'Perímetro do triângulo isósceles: {perimetro_tri_isos:.2f}')
            print(f'Área do triângulo isósceles: {area_tri_isos:.2f}')

        #ESCALENO
        elif triangulo == '3':
            lado_escaleno1 = float(input('Qual o valor do primeiro lado do triângulo escaleno: '))
            lado_escaleno2 = float(input('Qual o valor do segundo lado do triângulo escaleno: '))
            lado_escaleno3 = float(input('Qual o valor do terceiro lado do triângulo escaleno: '))

            perimetro_escaleno = lado_escaleno1 + lado_escaleno2 + lado_escaleno3
            semiperimetro = perimetro_escaleno / 2

            area_escaleno = mt.sqrt(
                semiperimetro *
                (semiperimetro - lado_escaleno1) *
                (semiperimetro - lado_escaleno2) *
                (semiperimetro - lado_escaleno3)
            )

            print(f'\nTriângulo Escaleno:')
            print(f'Lados: {lado_escaleno1}, {lado_escaleno2}, {lado_escaleno3}')
            print(f'Perímetro: {perimetro_escaleno:.2f}')
            print(f'Área (Fórmula de Herão): {area_escaleno:.2f}')

        else:
            print('Está opção não existe!')
#CÍRCULO
    elif plana == '4':
        raio = float(input("Qual o valor do raio: "))

        circunferencia = 2 * raio * mt.pi
        area_cir = mt.pi * raio ** 2

        print(f'\nCírculo:')
        print(f'Raio: {raio:.2f}')
        print(f'Circunferência: {circunferencia:.2f}')
        print(f'Área: {area_cir:.2f}')
        print('Círculo não tem diagonal.')
#TRAPÉZIO
    elif plana == '5':
        base_maior = float(input("Qual o valor da base maior: "))
        base_menor = float(input("Qual o valor da base menor: "))
        altura_trap = float(input("Qual o valor da altura do trapézio: "))
        area_trap = (base_maior + base_menor) * altura_trap / 2

        trap_analise = input('O trapézio é isósceles? ').upper()
        
        if trap_analise == 'SIM':
            diagonal_trap = mt.sqrt(
    altura_trap**2 + ((base_maior - base_menor)/2)**2
)
            print(f'A diagonal do trapézio é {diagonal_trap:.2f}.')
        
        else:
            print('Não conseguimos calcular ainda. 🙁')

        print(f'Área do trapézio: {area_trap:.2f}')
#LOSANGO
    elif plana == '6':
        diag_maior_losan = float(input("Qual o valor do diagonal maior losango? "))
        diag_menor_losan = float(input("Qual o valor do diagonal menor losango? "))
        area_losango = (diag_menor_losan * diag_maior_losan) * 1/2
        lado_losango = mt.sqrt((diag_maior_losan/2)**2 + (diag_menor_losan/2)**2)
        perimetro_losango = 4 * lado_losango

        print(f'Área do losango: {area_losango:.2f}')
        print(f'Lado do losango: {lado_losango:.2f}')
        print(f'Perímetro do losango: {perimetro_losango:.2f}')
        print('As diagonais já foram usadas para calcular a área do losango.')
#OPÇÃO INCORRETA
    else:
        print('ESCOLHA UMA OPÇÃO EXISTENTE. \nA resposta deve ser um número.')




#FIGURAS ESPACIAIS
elif geo == '2':
    print("\n== FIGURAS ESPACIAIS (3D) ==")
    print("1. Cubo")
    print("2. Paralelepípedo (Prisma retangular)")
    print("3. Esfera")
    print("4. Cilindro")
    print("5. Cone")
    print("6. Pirâmide de base quadrada")
    print("7. Prisma triangular")
    print("8. Tetraedro regular")
    
    espacial = input('\nQual figura você quer calcular (1-9)? ')

#CUBO
    if espacial == '1':
        lado_cubo = float(input('Qual o lado do cubo? '))
        area_total_cubo = 6 * lado_cubo ** 2
        area_lateral_cubo = 4 * lado_cubo ** 2
        area_base_cubo = lado_cubo ** 2
        volume_cubo = lado_cubo ** 3

        print(f'A área total do cubo é {area_total_cubo:.2f}.')
        print(f'A área lateral do cubo é {area_lateral_cubo:.2f}.')
        print(f'A área da base do cubo é {area_base_cubo:.2f}.')
        print(f'O volume total do cubo é {volume_cubo:.2f}.')

#PARALELEPÍDO
    elif espacial == '2':
        lado_paralel_a = float(input('Qual o lado a do paralelepípedo? '))
        lado_paralel_b = float(input('Qual o lado b do paralelepípedo? '))
        lado_paralel_c = float(input('Qual o lado c do paralelepípedo? '))

        area_base_paral = lado_paralel_a * lado_paralel_b
        area_total_paral = (2*area_base_paral) + (2*lado_paralel_b*lado_paralel_c) + (2*lado_paralel_a* lado_paralel_c)
        area_lateral_paral = 2*(lado_paralel_a * lado_paralel_c) + 2*(lado_paralel_b * lado_paralel_c)
        volume_paral = lado_paralel_a * lado_paralel_b * lado_paralel_c

        print(f'A área da base do paralelepípedo é {area_base_paral:.2f}.')
        print(f'A área total do paralelepípedo é {area_total_paral:.2f}.')
        print(f'A área lateral do paralelepípedo é {area_lateral_paral:.2f}.')
        print(f'O volume total do paralelepípedo é {volume_paral:.2f}.')

#ESFERA
    elif espacial == '3':
        raio_esfera = float(input('Qual o raio da esfera? '))

        area_esfera = 4 * mt.pi * mt.pow(raio_esfera,2)
        volum_esfera = (4 * mt.pi * mt.pow(raio_esfera, 3)) / 3

        print(f'A área total da esfera é {area_esfera:.2f}')
        print(f'O volume total da esfera é {volum_esfera:.2f}')

#CILINDRO
    elif espacial == '4':

        raio_cilind = float(input('Qual o raio do cilindro? '))
        altura_cilind = float(input('Qual a altura do cilindro? '))

        area_base_cilind = mt.pi * mt.pow(raio_cilind, 2)
        area_lateral_cilind = 2 * mt.pi * raio_cilind * altura_cilind
        area_total_cilind = 2 * area_base_cilind + area_lateral_cilind
        volume_cilindro = mt.pi * mt.pow(raio_cilind, 2) * altura_cilind

        print(f'A área da base do cilindro é {area_base_cilind:.2f}.')
        print(f'A área da lateral do cilindro é {area_lateral_cilind:.2f}.')
        print(f'A área total do cilindro é {area_total_cilind:.2f}.')
        print(f'O volume total do cilindro é {volume_cilindro:.2f}.')

#CONE
    elif espacial == '5':
        raio_cone = float(input('Qual o raio da base do cone? '))
        altura_cone = float(input('Qual a altura do cone? '))
        geratriz_cone = float(input('Qual a geratriz do cone? (Se não souber, digite 0): '))
        
        if geratriz_cone == 0:
            geratriz_cone = mt.sqrt(raio_cone**2 + altura_cone**2)
        
        area_base_cone = mt.pi * raio_cone**2
        area_lateral_cone = mt.pi * raio_cone * geratriz_cone
        area_total_cone = area_base_cone + area_lateral_cone
        volume_cone = (mt.pi * raio_cone**2 * altura_cone) / 3
        
        print(f'\nCone:')
        print(f'Área da base: {area_base_cone:.2f}')
        print(f'Área lateral: {area_lateral_cone:.2f}')
        print(f'Área total: {area_total_cone:.2f}')
        print(f'Volume: {volume_cone:.2f}')

#PIRÂMIDE DE BASE QUADRADA
    elif espacial == '6':
        lado_base_piram = float(input('Qual o lado da base quadrada da pirâmide? '))
        altura_piram = float(input('Qual a altura da pirâmide? '))
        apotema_lateral = float(input('Qual o apótema lateral? (Se não souber, digite 0): '))
        
        area_base_piram = lado_base_piram**2
        perimetro_base = 4 * lado_base_piram
        
        if apotema_lateral == 0:
            apotema_lateral = mt.sqrt(altura_piram**2 + (lado_base_piram/2)**2)
        
        area_lateral_piram = (perimetro_base * apotema_lateral) / 2
        area_total_piram = area_base_piram + area_lateral_piram
        volume_piram = (area_base_piram * altura_piram) / 3
        
        print(f'\nPirâmide de base quadrada:')
        print(f'Área da base: {area_base_piram:.2f}')
        print(f'Área lateral: {area_lateral_piram:.2f}')
        print(f'Área total: {area_total_piram:.2f}')
        print(f'Volume: {volume_piram:.2f}')

#PRISMA TRIANGULAR
    elif espacial == '7':
        print('\nPrisma Triangular (triângulo equilátero na base):')
        lado_tri_prisma = float(input('Qual o lado do triângulo equilátero da base? '))
        altura_prisma = float(input('Qual a altura do prisma? '))
        
        area_base_prisma = (lado_tri_prisma**2 * mt.sqrt(3)) / 4
        perimetro_base_prisma = 3 * lado_tri_prisma
        area_lateral_prisma = perimetro_base_prisma * altura_prisma
        area_total_prisma = 2 * area_base_prisma + area_lateral_prisma
        volume_prisma = area_base_prisma * altura_prisma
        
        print(f'\nPrisma Triangular:')
        print(f'Área da base: {area_base_prisma:.2f}')
        print(f'Área lateral: {area_lateral_prisma:.2f}')
        print(f'Área total: {area_total_prisma:.2f}')
        print(f'Volume: {volume_prisma:.2f}')

#TETRAEDRO REGULAR
    elif espacial == '8':
        aresta_tetra = float(input('Qual a aresta do tetraedro regular? '))
        
        area_total_tetra = aresta_tetra**2 * mt.sqrt(3)
        volume_tetra = (aresta_tetra**3 * mt.sqrt(2)) / 12
        altura_tetra = aresta_tetra * mt.sqrt(6) / 3
        
        print(f'\nTetraedro Regular:')
        print(f'Área total: {area_total_tetra:.2f}')
        print(f'Volume: {volume_tetra:.2f}')
        print(f'Altura: {altura_tetra:.2f}')

    else: 
        print('ESCOLHA UMA OPÇÃO EXISTENTE. \n A resposta deve ser um número.')




#CASO ESCOLHA UMA OPÇÃO NÃO EXISTENTE
else:
    print('ESCOLHA UMA OPÇÃO EXISTENTE. \nA resposta deve ser um número.')

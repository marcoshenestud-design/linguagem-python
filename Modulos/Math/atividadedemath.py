import math as mt

print("=== CALCULADORA CIENTÍFICA ===")
print("1. Seno")
print("2. Cosseno")
print("3. Tangente")
print("4. Logaritmo natural")
print("5. Potência")
print("6. Raiz quadrada")

operação = input("Digite qual operação você quer realizar: ")

#SENO
if operação == "1":
    a = input("Você vai colocar em (1) radiano ou em (2) ângulo? ")
    
    if a == "1":
        numero11 = float(input("Digite o número em radiano: "))
        seno_rad = mt.sin(numero11)
        print(f"O seno desse radiano é: {seno_rad}")
    
    elif a == "2":
        numero12 = float(input("Digite o número em ângulo: "))
        seno_ang = mt.sin(mt.radians(numero12))
        print(f"O seno desse ângulo é: {seno_ang}")
    
    else:
        print("Opção inválida!")

#COSSENO
elif operação == "2":
    b = input("Você vai colocar em (1) radiano ou em (2) ângulo? ")
    
    if b == "1":
        numero21 = float(input("Digite o número em radiano: "))
        coss_rad = mt.cos(numero21)
        print(f"O cosseno desse radiano é: {coss_rad}")
    
    elif b == "2":
        numero22 = float(input("Digite o número em ângulo: "))
        coss_ang = mt.cos(mt.radians(numero22))
        print(f"O cosseno desse ângulo é: {coss_ang}")
    
    else:
        print("Opção inválida!")

#TANGENTE
elif operação == "3":
    c = input("Você vai colocar em (1) radiano ou em (2) ângulo? ")

    if c == "1":
        numero31 = float(input("Digite o número em radiano: "))
        tang_rad = mt.tan(numero31)
        print(f"A tangente desse radiano é: {tang_rad}")

    elif c == "2":
        numero32 = float(input("Digite o número em ângulo: "))
        tang_ang = mt.tan(mt.radians(numero32))
        print(f"A tangente desse ângulo é: {tang_ang}")
    
    else: 
        print("Operação inválida!")

#LOGARITMO NATURAL
elif operação == "4":
    numero41 = float(input("Digite o número: "))
    log_nat = mt.log(numero41)
    print(f"O logaritmo natural desse número é: {log_nat}")

    if numero41 > 0:
        log_nat = mt.log(numero41)
        print(f"O logaritmo natural desse número é: {log_nat}")
    else:
        print("Erro: Logaritmo natural só é definido para números positivos!")


#POTÊNCIA
elif operação == "5":
    base = float(input("Digite um valor: "))
    potencia = float(input("Digite um valor: "))
    resultado_potencia = mt.pow(base, potencia) #não conhecia o pow
    print(f"O resultado da potênciação é: {resultado_potencia}")

#RAIZ QUADRADA - sqrt
elif operação == "6":
    numero61 = float(input("Digite um número: "))
    raiz_quad = mt.sqrt(numero61)
    print(f"A raiz quadrada desse número é: {raiz_quad}")

else:
    print("Operação inválida!")
#APRESENTAÇÃO DA CALCULADORA
print(str("===CALCULADORA==="))

#APRESENTAÇÃO DAS OPERAÇÕES DISPONÍVEIS
operação = input("1 - SOMA\n"
      "2 - SUBTRAÇÃO\n"
      "3 - MULTIPLICACAO\n"
      "4 - DIVISÃO\n"
"Qual operação desejada? ")

#NÚMEROS QUE O USUÁRIO IRA CADASTRAR NO PROGRAMA
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

#SOMA
if operação=="1":
    print(n1 + n2)

#SUBTRAÇÃO
elif operação == "2":
    print(n1 - n2)

#MULTIPLICAÇÃO
elif operação == "3":
    print(n1 * n2)

#DIVISÃO
else:
    print(n1 / n2)


#AGORA O OBJETIVO É USAR MATCH CASE
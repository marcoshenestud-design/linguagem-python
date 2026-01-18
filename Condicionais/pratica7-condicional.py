# Verifique se um ano é bissexto
# Regras: Divisível por 4, mas não por 100, exceto se for divisível por 400

ano = int(input("Digite um ano: "))

if (ano % 4 ==0 and ano % 100 !=0) or (ano % 400 == 0):
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')
# Calcule o desconto baseado no valor da compra
# Até R$100: sem desconto
# R$100 - R$500: 10% de desconto
# Acima de R$500: 15% de desconto

valor_compra = float(input("Valor da compra: R$ "))

if valor_compra < 100:
    print('Não terá desconto!')
elif valor_compra >=100 and valor_compra <= 500:
    print('Você terá um desconto de 10%!')
else:
    print('Você tera desconto de 15%!')
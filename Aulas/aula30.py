produtos = {"arroz": 25, "feijão": 12, "carne": 45, "macarrão": 8}


for item, preco in produtos.items():
    if preco > 20:
        print(f"{item} custa {preco} reais (acima de 20)")
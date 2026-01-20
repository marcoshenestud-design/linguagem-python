#Crie uma função que receba uma lista de números inteiros e retorne um dicionário contendo a contagem de quantos números são pares e quantos são ímpares.

numerosInteiros = [1,2,3,52,84,94,87,13,55,70]

def avaliacao(*numeros): #aceita muitos agumentos
    
    impar = []
    par = []

    for lista in numeros:
        for i in numerosInteiros:
            if i % 2 == 0:
                par.append(i)
            else:
                impar.append(i)

    resultado = {
        'pares': len(par),
        'impar': len(impar)
    }

    return resultado


print(avaliacao(numerosInteiros))
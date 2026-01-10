# Argumentos de tamanho variável (*args)
def soma_numeros(*args):
    
    """Soma um número variável de argumentos.
    Quando não souber a quantidade de argumentos.
    """
    
    total = 0
    
    for numero in args:
        total += numero
    
    return total
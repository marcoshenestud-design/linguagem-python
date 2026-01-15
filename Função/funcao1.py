#Crie uma função validar_senha(senha) que retorne True se a senha:
    #Tiver pelo menos 8 caracteres
    #Contiver pelo menos 1 número
    #Contiver pelo menos 1 letra maiúscula
    #Caso contrário, retorne False.
#💡 Dica: use 
    #any()
    # (isdigit, isupper).

senha = str(input('Digite uma senha: \nA senha deve conter pelo menos 8 caracteres: 1 número e 7 letras.'))

def validar_senha(senha):
    
    if len(senha) < 8:
        return False
    
    tem_numero = any(caractere.isdigit() for caractere in senha)
    tem_maiuscula = any(caractere.isupper() for caractere in senha)

    return tem_numero and tem_maiuscula

print(validar_senha(senha))
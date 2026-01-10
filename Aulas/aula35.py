# Argumentos de tamanho variável (**kwargs)

def exibe_info_pessoa(**kwargs):
    
    """Exibe informações passadas como pares chave-valor."""
    
    print("\nInformações da Pessoa:\n")
    
    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")

exibe_info_pessoa(nome = "Carla", 
                      profissao = "Engenheira de Dados", 
                      hobby = "Leitura")
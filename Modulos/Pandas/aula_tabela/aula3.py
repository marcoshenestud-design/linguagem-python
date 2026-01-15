#AGORA QUERO APRENDER A FAZER MANIPULAÇÃO NA TABELA
import pandas as pd

#Considerando a tabela "Vendas.xlsx" 
    #Quero: 
        #A soma do valor Final das 10 primeiras linhas e a quantidade de profutos vendidos.

data_frame = pd.read_excel('Vendas.xlsx')

primeiras10 = data_frame.head(10).sum()
print(primeiras10)

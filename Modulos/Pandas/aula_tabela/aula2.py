#IMPORTAR APARTIR DE UMA BASE DE DADOS
#MÉTODOS PANDAS

import pandas as pd

vendas_df = pd.read_excel('Vendas.xlsx')

# print(vendas_df.shape) # conta as linhas e as colunas da tabela
# print(vendas_df.describe()) #como estão as informações númericas da tabela - calcúlos estát.
print(vendas_df.head(10)) #conta as 10 primeiras linhas da tabelas

#COLUNA
#produtos = vendas_df['Produto'] 
#print(produtos)

#LINHA
#print(vendas_df.loc[1:5]) 

#PEGAR LINHAS QUE CORRESPONDEM A UMA CONDIÇÃO
#print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'], ['ID Loja'], ['Quantidade'])
    # loc[linha,coluna]


#CRIAR UMA COLUNA
#vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
#print(vendas_df) #criada nova coluna a tabela

#CRIAR UMA COLUNA COM VALOR PADRÃO
#vendas_df['Imposto'] = 0
#print(vendas_df)
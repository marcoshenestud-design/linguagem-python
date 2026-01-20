import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

#criar dados para análise
def criar_dados(num_registros = 600):
    print(f'Iniciando a geração de {num_registros} registros de vendas...')

    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    lista_produtos = list(produtos.keys())

    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }

    lista_cidades = list(cidades_estados.keys())

    dados_vendas = []

    data_inicial = datetime(2026, 1, 1)

    for i in range(num_registros):
        produto_nome = random.choice(lista_produtos) # .choice - escolhe um item aleatório

        cidade = random.choice(lista_cidades)
        quantidade = np.random.randint(1, 8) # .randint - gera números inteiros (primreiro, último)

        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))

        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0) # .uniform - criam números aleatórios
        else:
            preco_unitario = produtos[produto_nome]['preco']


        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })
    print("Geração de dados concluída.\n")
    return pd.DataFrame(dados_vendas)



df_vendas = criar_dados(500)


#MÉTODOS EM PANDAS PARA EXPLORAÇÃO DE DADOS
    # print(df_vendas.head()) #exibe as 5 primeiras linhas do DataFrame
    # print(df_vendas.shape) #linha, coluna
    # print(df_vendas.tail(5)) #exibe as 5 últimas linhas do DataFrame
    # print(df_vendas.info()) #informações gerais sobre o DataFrame (tipos de dados, valores não nulos)
    # print(df_vendas.describe()) #resumo estatístico
    # print(df_vendas.dtypes) #tipo de dados

#LIMPEZA, PRÉ-PROCESSAMENTO E ENGENHARIA DE ATRIBUTOS
df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')

#print(df_vendas.info())


#ANÁLISE
top_10_produtos = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)
#print(top_10_produtos)


sns.set_style("whitegrid")
plt.figure(figsize = (12, 7))
top_10_produtos.sort_values(ascending = True).plot(kind = 'barh', color = 'skyblue')
plt.title('Top 10 Produtos Mais Vendidos', fontsize = 16)
plt.xlabel('Quantidade Vendida', fontsize = 12)
plt.ylabel('Produto', fontsize = 12)
plt.tight_layout()
plt.show()

df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')
faturamento_mensal.map('R$ {:,.2f}'.format)
#print(faturamento_mensal)

plt.figure(figsize = (12, 6))
faturamento_mensal.plot(kind = 'line', marker = 'o', linestyle = '-', color = 'green')
plt.title('Evolução do Faturamento Mensal', fontsize = 16)
plt.xlabel('Mês', fontsize = 12)
plt.ylabel('Faturamento (R$)', fontsize = 12)
plt.xticks(rotation = 45)
plt.grid(True, which = 'both', linestyle = '--', linewidth = 0.5)
plt.tight_layout()
plt.show()

vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending = False)
vendas_estado.map('R$ {:,.2f}'.format)


plt.figure(figsize = (12, 7))
vendas_estado.plot(kind = 'bar', color = sns.color_palette("husl", 7))
plt.title('Faturamento Por Estado', fontsize = 16)
plt.xlabel('Estado', fontsize = 12)
plt.ylabel('Faturamento (R$)', fontsize = 12)
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()

faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending = False)
faturamento_categoria.map('R$ {:,.2f}'.format)


from matplotlib.ticker import FuncFormatter

faturamento_ordenado = faturamento_categoria.sort_values(ascending = False)
fig, ax = plt.subplots(figsize = (12, 7))


def formatador_milhares(y, pos):
    """Formata o valor em milhares (K) com o cifrão R$."""
    return f'R$ {y/1000:,.0f}K'


formatter = FuncFormatter(formatador_milhares)
ax.yaxis.set_major_formatter(formatter)
faturamento_ordenado.plot(kind = 'bar', ax = ax, color = sns.color_palette("viridis", len(faturamento_ordenado)))
ax.set_title('Faturamento Por Categoria', fontsize = 16)
ax.set_xlabel('Categoria', fontsize = 12)
ax.set_ylabel('Faturamento', fontsize = 12)
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()


#listar cada duvida a respeito do projeto e desenvolvimento
#buscar dados de lugares seguros e com problemas
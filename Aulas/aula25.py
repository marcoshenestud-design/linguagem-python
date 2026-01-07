#DICIONÁRIOS - são coleções de pares chave:valor
#São mutáveis

aluno = {
    'nome': 'Bob',
    'Idade': 22,
    'assunto': 'Python',
    'Aluno_ativo': True
}

print(f'Dicionário do aluno: {aluno}')

print(type(aluno))

print(f'Nome do aluno: {aluno["nome"]}')
print(f'Assunto do curso: {aluno.get("assunto")}')  # get é uma forma segura de acessar as chaves


#ADICIONANDO UM NOVO PAR DE CHAVE
aluno['cidade'] = 'São Paulo'
print(f'Dicionário atualizado: \n{aluno}')


#MODIFICANDO UM VALOR EXISTENTE
aluno['Idade'] = 25
print(f'A idade modifica é {aluno["Idade"]}.')

#REMOVER UM PAR CHAVE VALOR
del aluno['Aluno_ativo']
print(f"Dicionário após remover a chave 'ativo': \n{aluno}")
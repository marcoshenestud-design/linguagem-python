#Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas. Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.

alunosnotas = {
    'Marcos': 10,
    'Anna': 4,
    'Jaíny': 5,
    'Elias': 8,
    'Lorena': 9,
    'Golias': 4,
    'Lana': 10
}


def alunos_aprovados(a):
    notas = a.values()
    quantidadealunos = len(notas)
    somanotas = sum(notas)
    med_turma = somanotas / quantidadealunos
    
    print(f'\nA média da turma é {med_turma:.2f}.')

    acima_media = []

    for aluno, nota in a.items():
        if nota >= med_turma:
            acima_media.append(aluno)
        
    return acima_media


alunos_aprovados(alunosnotas)


# def alunos_acima_da_media(alunosnotas):
#     notas = alunosnotas.values()
#     soma_notas = sum(notas)
#     quantidade_alunos = len(alunosnotas)
#     media = soma_notas / quantidade_alunos

#     acima_da_media = []
    
#     for nome, nota in alunosnotas.items():
#         if nota > media:
#             acima_da_media.append(nome)
    
#     return acima_da_media

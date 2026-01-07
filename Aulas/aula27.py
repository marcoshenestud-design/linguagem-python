#CONVERSÃO ENTRE TIPOS DE DADOS EM PYTHON

numero_em_texto = '123'
numero_inteiro = int(numero_em_texto)

print(f"String '{numero_em_texto}' para Inteiro: {numero_inteiro}, Tipo: {type(numero_inteiro)}")


#CONVERSÃO ENTRE ESTRUTURA DE DADOS
lista_com_duplicados = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto_unico = set(lista_com_duplicados) #o set converte para conjuntos, que não aceita duplicatas
lista_sem_duplicados = list(conjunto_unico) #conversão de volta para lista

print(f'\n\nLista original: {lista_com_duplicados}')
print(f'\nConvertida para conjunto: (remove duplicadas): {conjunto_unico}')
print(f'\nConvertida de volta para lista: {lista_sem_duplicados}\n')
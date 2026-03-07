#Crie uma função que receba uma lista de strings (potenciais e-mails) e um parâmetro opcional dominio_desejado (com valor padrão "gmail.com"). A função deve retornar uma nova lista, usando list comprehension, contendo apenas os e-mails que terminam com o domínio desejado.

emails = []

quantidade = int(input("Quantos emails deseja cadastrar? "))

for i in range(quantidade):
    email = input("Digite o email: ")
    emails.append(email)

def filtrar_emails(lista_emails, dominio_desejado="gmail.com"):
    return [email for email in lista_emails if email.endswith(dominio_desejado)]

print(filtrar_emails(emails))
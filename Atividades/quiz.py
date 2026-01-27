tarefas = []
#calculadora
def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")

def ver_tarefas():
    print("\n--- Suas Tarefas ---")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
    print("-------------------")

def main():
    while True:
        print("\n=== MINHA LISTA DE TAREFAS ===")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            ver_tarefas()
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida! Tente 1, 2 ou 3.")

if __name__ == "__main__":
    main()
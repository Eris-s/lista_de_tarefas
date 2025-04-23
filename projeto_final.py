def adicionar_tarefa(lista_de_tarefas, tarefa):   #funções são essenciais em programas grandes para não prcisar ficar alterando manualmente
    """"Adiciona nova tarefa à uma lista pré-existente"""
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    """Exibe uma lista de tarefas enumerada"""
    print("*" * 50)
    print(f"{' ' * 15}Lista de tarefas")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"{n} - {tarefa}")
        n += 1
    print("-" * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    """Deleta uma tarefa de uma lista pré-existente a partir do seu número correspondente"""
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

def exibir_menu():
    """Exibe menu"""
    print('-' * 50)
    print("Escolha uma opção:\n" \
        "1 - Inserir nova tarefa\n" \
        "2 - Listar tarefas\n" \
        "3 - Deletar tarefa\n" \
        "4 - Sair"
    )
    print('-' * 50)    

#Inicia as variáveis
lista_de_tarefas = []
continuar = True

#Cabeçalho do programa
print("." * 50)
print("Bem-vinde à sua Lista de Tarefas")
print("." * 50)

#Loop principal
while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
       listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        #A validação verifica se o valor é numérico, se é menor do que o limite da lista e se é maior que zero"
        tarefa = input("Insira o número da tarefa que deseja deletar: ")
        if not tarefa.isnumeric():
            print("Insira somente os números da lista! Tente novamente.")
        elif int(tarefa) > len(lista_de_tarefas):
            print("Número inválido! Tente novamente.")
        elif int(tarefa) <= 0:
            print("Número inválido! Tente novamente.")
        #tarefa = int(tarefa)
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
#se temos uma lista de dois elementos, o usuário pede para eliminar o item da posição 2, a posição 2 no python é o 3ª
#então se lista[3] vai dar erro, pois só tem dois itens
    elif opcao == "4":
        continuar = False
    else:
        print("Opção inválida, tente novamente, por favor!")
    print('\n')


print("Bem-vindo ao sistema do Acervo Bibliográfico - Gabriel Sousa Oliveira")

# Lista para armazenar os registros (simulando um "banco de dados")
lista_livro = []
id_global = 1  # Começa em 1 para evitar ID 0

def exibir_menu():
    """Exibe o menu principal e retorna a opção escolhida pelo usuário."""
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Adicionar Novo Registro")
    print("2 - Listar Registros")
    print("3 - Atualizar Registro")
    print("4 - Excluir Registro")
    print("5 - Sair")
    
    return input("Digite a opção desejada: ")

def cadastrar_livro():
    """Cadastra um novo livro no sistema."""
    global id_global  # Permite modificar a variável global
    titulo = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    
    livro = {
        "id": id_global,
        "titulo": titulo,
        "autor": autor,
        "editora": editora
    }
    
    lista_livro.append(livro)  # Adiciona o livro na lista
    print(f" Livro cadastrado com sucesso! ID: {id_global}")
    
    id_global += 1  # Incrementa o ID para o próximo livro

def consultar_livros():
    """Consulta livros de diferentes formas."""
    if not lista_livro:
        print(" Nenhum livro cadastrado.")
        return

    print("\n 1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu")
    opcao = input("Digite a opção desejada: ") 
    
    if opcao == "1":
        for livro in lista_livro:
            print(livro)
    elif opcao == "2":
        id_livro = int(input("Digite o ID do livro: "))
        encontrado = False
        for livro in lista_livro:
            if livro["id"] == id_livro:
                print(livro)
                encontrado = True
                break
        if not encontrado:
            print("⚠️ Livro não encontrado.")
    elif opcao == "3":
        autor = input("Digite o autor do livro: ")
        livros_autor = [livro for livro in lista_livro if livro["autor"].lower() == autor.lower()]
        if livros_autor:
            for livro in livros_autor:
                print(livro)
        else:
            print(" Nenhum livro encontrado para esse autor.")
    elif opcao == "4":
        return  
    else:
        print(" Opção inválida!")

def remover_livro():
    """Remove um livro pelo ID."""
    if not lista_livro:
        print(" Nenhum livro cadastrado para remover.")
        return

    try:
        id_livro = int(input("Digite o ID do livro que deseja remover: "))
        for i, livro in enumerate(lista_livro):
            if livro["id"] == id_livro:
                del lista_livro[i]
                print(" Livro removido com sucesso!")
                return
        print(" Livro não encontrado.")
    except ValueError:
        print(" ID inválido. Digite um número válido.")

# Loop principal do sistema
while True:
    opcao = exibir_menu()

    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        consultar_livros()
    elif opcao == "3":
        print("🚧 Funcionalidade de atualização ainda não implementada.")
    elif opcao == "4":
        remover_livro()
    elif opcao == "5":
        print(" Saindo do sistema.")
        break
    else:
        print("Opção inválida! Tente novamente.")
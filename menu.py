from datetime import datetime
 
livros = []

def add_livros():
    titulo = input("Título: ")
    autor = input("Autor: ")

    livros.append([titulo, autor, True])
    print("Livro adicionado!")

def listar_livros():
    for livro in livros:
        print(livro)

def emprestar():
    titulo = ("Digite o título do livro que você deseja emprestar: ")

    for livro in livros:
        if livro[0] == titulo: 
            if livro[2] == True:
                livro[2] = False
                print("Livro emprestado com sucesso!")
                return
            else:
                print("O livro já está emprestado!")
                return
    print("Livro não encontrado!")

def devolver():
    titulo = input("Digite o título do livro que você deseja devolver: ")

    for livro in livros:
        if livro[0] == titulo:
            if livro[2] == False: 
                livro[2] = True

                data_emprestimo_str = input("Digite a data do empréstimo (dd/mm/aaaa)")

                data_emprestimo = datetime.strptime(data_emprestimo_str, "%d/%m/%y")
                data_devolucao = datetime.now()

                dias = (data_devolucao - data_emprestimo).days

                if dias > 3:
                    dias_atraso = dias - 3
                    multa = dias_atraso * 5
                    print("Livro devolvido com {dias_atraso} dias(s) de atraso.")
                    print(f"Multa total: R${multa},00")

                else: 
                    print("Livro devolvido com sucesso!")
                    return
            else:
                print("Esse livro já está disponível!")
                return
    print("Livro não encontrado!")

while True:
    print("\n===== SISTEMA BIBLIOTECA =====")
    print(" ")
    print("1. Adicionar livro")
    print("2. Emprestar livro")
    print("3. Devolver livro")
    print("4. Sair")
    print(" ")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        add_livros()
    elif opcao == "2":
        emprestar()
    elif opcao == "3":
        devolver()
    elif opcao == "4":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida! Tente novamente!")
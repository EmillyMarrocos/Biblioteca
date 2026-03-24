from datetime import datetime, timedelta

usuarios = {}

livros = [
    {"id": 1, 
     "nome": "Dom Casmurro", 
     "autor": "Machado de Assis", 
     "genero": "Romance", 
     "quantidade": 3, 
     "disponivel": True
     },

    {"id": 2, 
     "nome": "O Pequeno Príncipe", 
     "autor": "Antoine de Saint-Exupéry", 
     "genero": "Fábula", 
     "quantidade": 5, 
     "disponivel": True
     },

    {"id": 3, 
     "nome": "1984", 
     "autor": "George Orwell", 
     "genero": "Distopia", 
     "quantidade": 2, 
     "disponivel": True
     },

    {"id": 4, 
     "nome": "Harry Potter e a Pedra Filosofal", 
     "autor": "J. K. Roling", 
     "genero": "Fantasia", 
     "quantidade": 4, 
     "disponivel": True
     },

    {"id": 5, 
     "nome": "Orgulho e Preconceito", 
     "autor": "Jane Austen", 
     "genero": "Romance", 
     "quantidade": 1, 
     "disponivel": True
     }
]

emprestimos = []

#---- MENU INICIAL ----

def menu_inicial():
    while True:
        print("\n=== LIVRARIA ===")
        print("1. Cadastrar")
        print("2. Entrar")
        print("3. Sair")

        opcao = input("Escolha: ")

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            usuario_id = entrar()
            if usuario_id:
                menu_livraria(usuario_id)
        elif opcao == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# --- CADASTRO ---

def cadastrar(): 
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios:
        print("Usuário já existente!")
    else:
        usuarios[usuario] = {
        "id": len(usuarios) + 1,
        "senha": senha
    }
    print("Cadastro realizado!")

# --- LOGIN ---

def entrar():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        print("Login realizado!")
        return usuarios[usuario]["id"]
    else:
        print("Usuário ou senha incorretos!")
        return None

# --- MENU LIVRARIA --- 

def menu_livraria(usuario_id):
    while True:
        print("\n === MENU LIVROS === ")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Emprestar")
        print("4. Devolver")
        print("5. Sair")      

        opcao = input("Escolha: ")

        if opcao == "1":
            add_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            emprestar_livro(usuario_id)
        elif opcao == "4":
            devolver_livro(usuario_id)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

def add_livro():
    nome = input("Nome: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    quantidade = int(input("Quantidade: "))

    novo_id = livros[-1]["id"] + 1 if livros else 1

    livro = {
        "id": novo_id,
        "nome": nome,
        "autor": autor,
        "genero": genero,
        "quantidade": quantidade,
        "disponivel": quantidade > 0
    }

    livros.append(livro)
    print("Livro adicionado com sucesso!")

def listar_livros():
    print("Lista de Livros: ")
    for livro in livros:
        print(f"""
ID: {livro['id']}
Nome: {livro['nome']}
Autor: {livro['autor']}
Gênero: {livro['genero']}
Quantidade: {livro['quantidade']}
Disponível: {livro['disponivel']}
---------------------------
""")
        
def emprestar_livro(usuario_id):
    listar_livros()

    try:
        livro_id = int(input("Digite o ID do livro: "))
        for livro in livros:
            if livro["id"] == livro_id:
                if livro['quantidade'] > 0:
                    livro['quantidade'] -= 1
                    livro['quantidade'] = livro['quantidade'] > 0

                    emprestimos.append({
                        "data_emprestimo": datetime.now(),
                        "usuario_id": usuario_id,
                        "livro_id": livro_id
                    })

                    print("Livro emprestado!")
                else:
                    print("Livro indisponível!")
                return
            
            print("Livro não encontrado.")
    except:
        print("Erro!")

def devolver_livro(usuario_id, dias_uteis):
    hoje = datetime.now()

    meus = [e for e in emprestimos if e["usuario_id"] == usuario_id]

    if not meus:
        print("Você não tem empréstimos.")
        return
    
    print("Seus livros: ")
    for i, e in enumerate(meus):
        for livro in livros:
            if livro["id"] == e["livro_id"]:
                print(f"{i} - {livro['nome']}")

    try:
        i = int(input("Escolha: "))
        emp = meus[i]

        data_emprestimo = emp["data_emprestimo"]
        dias = dias_uteis(data_emprestimo, hoje)

        multa = 0 
        if dias > 3: 
            atraso = dias - 3 
            multa = atraso * 5 

        print("Data do Empréstimo: ", data_emprestimo.strftime("%d/%m/%y"))
        print("Data da Devolução: ", hoje.strftime("%d/%m/%y"))

        if multa > 0:
            print(f"Multa por atraso: R$ {multa}")
        else:
            print("Sem multa!")

        for livro in livros:
            if livro["id"] == emp["livro_id"]:
                livro['quantidade'] += 1
                livro['disponivel'] = True
        
        emprestimos.remove(emp)

        print("Livro devolvido!")
    except:
        print("Erro!")

menu_inicial()
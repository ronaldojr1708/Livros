livros = {}

def cadastrar_livro(id_livro, nome_livro):
    if id_livro in livros:
        print(f"Livro com ID {id_livro} já está cadastrado.")
    else:
        livros[id_livro] = nome_livro
        print(f"Livro '{nome_livro}' cadastrado com sucesso!")

def deletar_livro(id_livro):
    if id_livro in livros:
        del livros[id_livro]
        print(f"Livro com ID {id_livro} deletado com sucesso!")
    else:
        print(f"Livro com ID {id_livro} não encontrado.")


def modificar_nome_livro(id_livro, novo_nome):
    if id_livro in livros:
        livros[id_livro] = novo_nome
        print(f"Nome do livro modificado para '{novo_nome}' com sucesso!")
    else:
        print(f"Livro com ID {id_livro} não encontrado.")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("Livros cadastrados:")
        for id_livro, nome_livro in livros.items():
            print(f"ID: {id_livro} | Nome: {nome_livro}")


cadastrar_livro(1, "O Senhor dos Anéis")
cadastrar_livro(2, "Dom Casmurro")
cadastrar_livro(3, "Harry Potter")

listar_livros()

modificar_nome_livro(2, "Memórias Póstumas de Brás Cubas")

deletar_livro(3)

listar_livros()

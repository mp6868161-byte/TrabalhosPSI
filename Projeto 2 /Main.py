base_artistas = []


def criar_artista():
    print("\n--- Registar Novo Artista ---")
    try:
        id_artista = int(input("ID: "))

        # Verificar se o ID já existe
        if any(a['id'] == id_artista for a in base_artistas):
            print("Erro: Já existe um artista com este ID!")
            return

        # Recolha de dados
        artista = {
            "id": id_artista,
            "nome": input("Nome: "),
            "nif": input("NIF (9 dígitos): "),
            "genero": input("Género Musical: "),
            "bancada": input("Bancada: "),
            "setor": input("Setor: "),
            "nacionalidade": input("Nacionalidade: "),
            "tipo": input("Tipo (Ex: Solo, Banda): ")
        }

        base_artistas.append(artista)
        print(f"Sucesso: O artista '{artista['nome']}' foi registado!")
    except ValueError:
        print("Erro: O ID tem de ser um número inteiro.")


def listar_artistas():
    print("\n--- Lista de Artistas do Concerto ---")
    if not base_artistas:
        print("A base de dados está vazia.")
        return

    for a in base_artistas:
        print(f"ID: {a['id']} | Nome: {a['nome']} | NIF: {a['nif']} | Local: {a['bancada']}/{a['setor']}")


def atualizar_artista():
    try:
        id_procura = int(input("\nID do artista a atualizar: "))
        for a in base_artistas:
            if a['id'] == id_procura:
                print(f"A editar dados de: {a['nome']} (Deixe em branco para manter o atual)")

                # Atualização seletiva
                a['nome'] = input(f"Novo Nome [{a['nome']}]: ") or a['nome']
                a['nif'] = input(f"Novo NIF [{a['nif']}]: ") or a['nif']
                a['genero'] = input(f"Novo Género [{a['genero']}]: ") or a['genero']
                a['bancada'] = input(f"Nova Bancada [{a['bancada']}]: ") or a['bancada']
                a['setor'] = input(f"Novo Setor [{a['setor']}]: ") or a['setor']

                print("Dados atualizados com sucesso!")
                return
        print("Aviso: Artista não encontrado.")
    except ValueError:
        print("Erro: Digite um ID válido.")


def eliminar_artista():
    try:
        id_procura = int(input("\nID do artista a eliminar: "))
        for i, a in enumerate(base_artistas):
            if a['id'] == id_procura:
                confirmar = input(f"Tem a certeza que quer eliminar {a['nome']}? (s/n): ")
                if confirmar.lower() == 's':
                    del base_artistas[i]
                    print("Artista removido do sistema.")
                return
        print("Aviso: Artista não encontrado.")
    except ValueError:
        print("Erro: Digite um ID válido.")


def menu():
    while True:
        print("\n" + "=" * 35)
        print("   GESTÃO DE ARTISTAS - CONCERTO")
        print("=" * 35)
        print("1. Registar Artista")
        print("2. Listar Todos")
        print("3. Atualizar Dados")
        print("4. Eliminar Artista")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            criar_artista()
        elif opcao == '2':
            listar_artistas()
        elif opcao == '3':
            atualizar_artista()
        elif opcao == '4':
            eliminar_artista()
        elif opcao == '0':
            print("A encerrar o programa...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()

import utils

artistas = {}


def menu():
    print("\n=== GESTOR DE CONCERTOS ===")
    print("1. Adicionar Artista")
    print("2. Ver Artistas/Bandas")
    print("5. Criar Bilhete para Artista")
    print("0. Sair")
    return input("Escolha uma opção: ")


def adicionar_artista():
    print("\n--- Novo Artista ---")
    nome = input("Nome do Artista/Banda: ")
    genero = input("Género Musical: ")

    # CORREÇÃO: Usamos o módulo utils + a função lá dentro
    id_novo = utils.gerar_id_utilizador()

    artistas[id_novo] = {
        "nome": nome,
        "genero": genero,
        "bilhetes": []
    }
    print(f"Sucesso! {nome} registado com ID: {id_novo}")


def listar_artistas():
    print("\n--- Lista de Bandas ---")
    if not artistas:
        print("Nenhum artista registado.")
    for id_art, info in artistas.items():
        print(f"ID: {id_art} | Nome: {info['nome']} | Género: {info['genero']} | Bilhetes: {len(info['bilhetes'])}")


def criar_bilhete():
    listar_artistas()
    if not artistas: return

    id_art = input("\nID do artista para o bilhete (ex: U001): ").upper()

    if id_art in artistas:
        preco = input("Preço do bilhete: ")
        lugar = input("Lugar/Fila: ")
        data = input("Data do Concerto (AAAA-MM-DD): ")

        # CORREÇÃO: Usamos a função de validar_data do utils
        if utils.validar_data(data):
            bilhete = {
                "id_bilhete": len(artistas[id_art]["bilhetes"]) + 1,
                "preco": preco,
                "lugar": lugar,
                "data": data
            }
            artistas[id_art]["bilhetes"].append(bilhete)
            print("Bilhete criado com sucesso!")
        else:
            print("Erro: Data inválida!")
    else:
        print("Artista não encontrado.")


# --- Ciclo Principal ---
while True:
    opcao = menu()
    if opcao == "1":
        adicionar_artista()
    elif opcao == "2":
        listar_artistas()
    elif opcao == "5":
        criar_bilhete()
    elif opcao == "0":
        print("A sair...")
        break
    else:
        print("Opção inválida.")
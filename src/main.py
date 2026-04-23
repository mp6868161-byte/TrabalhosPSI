db_artistas = {}
db_bilhetes = {}
#colocar imports da main nas entidades, codigos de erro tp 201 em returns

# --- CRUD ARTISTA ---
def criar_artista():
    idx = input("ID do Artista: ")
    nome = input("Nome da Banda/Artista: ")
    genero = input("Género Musical: ")

    # Criar um dicionário para o artista
    db_artistas[idx] = {
        "id": idx,
        "nome": nome,
        "genero": genero
    }
    print(f"Artista {nome} adicionado com sucesso!")


def ler_artistas():
    print("\n--- Lista de Bandas ---")
    if not db_artistas:
        print("Nenhum artista registado.")
        return
    for a in db_artistas.values():
        print(f"ID: {a['id']} | Nome: {a['nome']} | Género: {a['genero']}")


def atualizar_artista():
    idx = input("ID do artista a editar: ")
    if idx in db_artistas:
        db_artistas[idx]["nome"] = input("Novo nome: ")
        db_artistas[idx]["genero"] = input("Novo género: ")
        print("Dados atualizados!")
    else:
        print("Artista não encontrado.")


def eliminar_artista():
    idx = input("ID do artista a remover: ")
    if db_artistas.pop(idx, None):
        print("Artista removido.")
    else:
        print("ID inexistente.")


# --- CRUD BILHETES ---
def criar_bilhete():
    idx = input("ID do Bilhete: ")
    id_c = input("ID do Concerto: ")
    preco = input("Preço: ")
    tipo = input("Tipo (VIP/Normal): ")
    lugar = input("Lugar: ")
    fila = input("Fila: ")
    bancada = input("Bancada/Setor: ")
    nif = input("NIF do Comprador: ")
    nac = input("Nacionalidade: ")

    # Criar um dicionário para o bilhete
    db_bilhetes[idx] = {
        "id": idx,
        "preco": preco,
        "tipo": tipo,
        "lugar": lugar,
        "fila": fila,
        "id_concerto": id_c,
        "bancada": bancada,
        "nif": nif,
        "nacionalidade": nac
    }
    print("Bilhete emitido!")


def ler_bilhetes():
    print("\n--- Consulta de Bilhetes ---")
    if not db_bilhetes:
        print("Nenhum bilhete emitido.")
        return
    for b in db_bilhetes.values():
        print(
            f"ID: {b['id']} | Concerto: {b['id_concerto']} | Preço: {b['preco']}€ | Lugar: {b['lugar']} (Fila {b['fila']})")


def eliminar_bilhete():
    idx = input("ID do bilhete a eliminar: ")
    if db_bilhetes.pop(idx, None):
        print("Bilhete cancelado/eliminado.")
    else:
        print("Bilhete não encontrado.")


# --- MAIN LOOP ---
def main():
    while True:
        print("\n=== GESTOR DE CONCERTOS ===")
        print("1. Gerir Artistas")
        print("2. Gerir Bilhetes")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n[1] Adicionar [2] Ver [3] Editar [4] Remover")
            sub = input("Ação: ")
            if sub == "1":
                criar_artista()
            elif sub == "2":
                ler_artistas()
            elif sub == "3":
                atualizar_artista()
            elif sub == "4":
                eliminar_artista()

        elif opcao == "2":
            print("\n[1] Criar Bilhete [2] Consultar [3] Eliminar")
            sub = input("Ação: ")
            if sub == "1":
                criar_bilhete()
            elif sub == "2":
                ler_bilhetes()
            elif sub == "3":
                eliminar_bilhete()

        elif opcao == "0":
            print("A sair...")
            break


if __name__ == "__main__":
    main()
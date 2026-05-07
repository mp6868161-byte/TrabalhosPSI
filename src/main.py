db_artistas = {}
db_bilhetes = {}
db_staff = {}      
db_concertos = {}   

# --- CRUD ARTISTA ---
def criar_artista():
    idx = input("ID do Artista: ")
    if idx in db_artistas:
        print("Erro: ID já existe.")
        return
    nome = input("Nome da Banda/Artista: ")
    genero = input("Género Musical: ")
    db_artistas[idx] = {"id": idx, "nome": nome, "genero": genero}
    print(f"Artista {nome} adicionado com sucesso!")

def ler_artistas():
    print("\n--- Lista de Bandas ---")
    if not db_artistas:
        print("Nenhum artista registado.")
        return
    for a in db_artistas.values():
        print(f"ID: {a['id']} | Nome: {a['nome']} | Género: {a['genero']}")

# --- CRUD STAFF (NOVO) ---
def criar_staff():
    idx = input("ID do Funcionário: ")
    if idx in db_staff:
        print("Erro: ID já existe.")
        return
    db_staff[idx] = {
        "id": idx,
        "nif": input("NIF: "),
        "nome": input("Nome: "),
        "funcao": input("Função (Segurança/Técnico/etc): "),
        "telemovel": input("Telemóvel: ")
    }
    print("Funcionário registado!")

def ler_staff():
    print("\n--- Lista de Staff ---")
    if not db_staff:
        print("Nenhum funcionário registado.")
        return
    for s in db_staff.values():
        print(f"ID: {s['id']} | Nome: {s['nome']} | Função: {s['funcao']}")

# --- CRUD CONCERTO (NOVO) ---
def criar_concerto():
    idx = input("ID do Concerto: ")
    if idx in db_concertos:
        print("Erro: ID já existe.")
        return
    id_art = input("ID do Artista: ")
    if id_art not in db_artistas:
        print("Erro: Artista não encontrado. Crie o artista primeiro.")
        return

    db_concertos[idx] = {
        "id": idx,
        "id_artista": id_art,
        "data": input("Data (DD/MM/AAAA HH:MM): "),
        "local": input("Local: "),
        "estado": "Agendado",
        "lista_ids_staff": [],
        "lista_ids_bilhetes_vendidos": []
    }
    print("Concerto agendado!")

def ler_concertos():
    print("\n--- Agenda de Concertos ---")
    if not db_concertos:
        print("Agenda vazia.")
        return
    for c in db_concertos.values():
        artista = db_artistas[c['id_artista']]['nome']
        print(f"ID: {c['id']} | Artista: {artista} | Local: {c['local']} | Estado: {c['estado']}")

# --- CRUD BILHETES --- (Mantido conforme o teu original)
def criar_bilhete():
    idx = input("ID do Bilhete: ")
    id_c = input("ID do Concerto: ")
    if id_c not in db_concertos:
        print("Erro: Concerto inexistente.")
        return
    
    preco = input("Preço: ")
    tipo = input("Tipo (VIP/Normal): ")
    lugar = input("Lugar: ")
    fila = input("Fila: ")
    
    db_bilhetes[idx] = {
        "id": idx, "preco": preco, "tipo": tipo, "lugar": lugar, 
        "fila": fila, "id_concerto": id_c
    }
    # Link do bilhete ao concerto
    db_concertos[id_c]["lista_ids_bilhetes_vendidos"].append(idx)
    print("Bilhete emitido e associado ao concerto!")

# --- MAIN LOOP ---
def main():
    while True:
        print("\n=== GESTOR DE CONCERTOS ===")
        print("1. Gerir Artistas")
        print("2. Gerir Bilhetes")
        print("3. Gerir Staff")
        print("4. Gerir Concertos")
        print("0. Sair")

        opcao = input("Escolha uma área: ")

        if opcao == "1":
            print("\n[1] Adicionar [2] Ver")
            sub = input("Ação: ")
            if sub == "1": criar_artista()
            elif sub == "2": ler_artistas()

        elif opcao == "2":
            print("\n[1] Criar Bilhete [2] Consultar")
            sub = input("Ação: ")
            if sub == "1": criar_bilhete()
            # Podes adicionar as outras funções aqui...

        elif opcao == "3":
            print("\n[1] Registar Staff [2] Listar Equipa")
            sub = input("Ação: ")
            if sub == "1": criar_staff()
            elif sub == "2": ler_staff()

        elif opcao == "4":
            print("\n[1] Marcar Concerto [2] Ver Agenda")
            sub = input("Ação: ")
            if sub == "1": criar_concerto()
            elif sub == "2": ler_concertos()

        elif opcao == "0":
            print("A sair...")
            break

if __name__ == "__main__":
    main()

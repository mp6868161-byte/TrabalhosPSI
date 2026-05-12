import json
import os

# --- FICHEIROS DE PERSISTÊNCIA ---
STAFF_FILE = "staff_db.json"
ARTISTAS_FILE = "artistas_db.json"
CONCERTOS_FILE = "concertos_db.json"

# --- DADOS INICIAIS (usados apenas se os ficheiros não existirem) ---
STAFF_INICIAL = {
    "1": {"nif": "123456789", "nome": "Carlos Silva", "funcao": "Técnico de Som", "telemovel": "912345678"},
    "2": {"nif": "987654321", "nome": "Ana Rita", "funcao": "Segurança", "telemovel": "961234567"}
}
ARTISTAS_INICIAL = {
    "10": {"nome": "The Rock Band", "genero": "Rock"},
    "11": {"nome": "DJ Sunset", "genero": "Electronic"}
}
CONCERTOS_INICIAL = {
    "100": {
        "id_artista": 10,
        "ids_staff": [1, 2],
        "data": "2024-06-15 21:00",
        "local": "Altice Arena",
        "estado": "Agendado",
        "bilhetes_vendidos": 1500
    }
}

# --- FUNÇÕES DE PERSISTÊNCIA ---

def carregar(ficheiro, inicial):
    """Carrega dados de um ficheiro JSON. Se não existir, usa os dados iniciais."""
    if os.path.exists(ficheiro):
        with open(ficheiro, "r", encoding="utf-8") as f:
            return json.load(f)
    return inicial.copy()

def guardar(ficheiro, dados):
    """Guarda dados num ficheiro JSON."""
    with open(ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def carregar_tudo():
    """Carrega todas as bases de dados dos ficheiros JSON."""
    staff = carregar(STAFF_FILE, STAFF_INICIAL)
    artistas = carregar(ARTISTAS_FILE, ARTISTAS_INICIAL)
    concertos = carregar(CONCERTOS_FILE, CONCERTOS_INICIAL)
    return staff, artistas, concertos

def guardar_tudo(staff, artistas, concertos):
    """Guarda todas as bases de dados nos ficheiros JSON."""
    guardar(STAFF_FILE, staff)
    guardar(ARTISTAS_FILE, artistas)
    guardar(CONCERTOS_FILE, concertos)

# --- GERADOR DE ID ---

def gerar_id(base_dict):
    """Gera um novo ID inteiro único para o dicionário fornecido."""
    if not base_dict:
        return 1
    return max(int(k) for k in base_dict.keys()) + 1

# --- CRUD STAFF ---

def criar_staff(staff_db, concertos_db, nif, nome, funcao, telemovel):
    id_s = str(gerar_id(staff_db))
    staff_db[id_s] = {
        "nif": nif,
        "nome": nome,
        "funcao": funcao,
        "telemovel": telemovel
    }
    guardar(STAFF_FILE, staff_db)
    print(f"Staff '{nome}' registado com sucesso com ID {id_s}.")
    return int(id_s)

def listar_staff_concerto(staff_db, concertos_db, id_concerto):
    concerto = concertos_db.get(str(id_concerto))
    if not concerto:
        print("Concerto não encontrado.")
        return
    print(f"\nEquipa alocada ao Concerto {id_concerto} ({concerto['local']}):")
    for id_s in concerto["ids_staff"]:
        s = staff_db.get(str(id_s))
        if s:
            print(f"  - ID: {id_s} | Nome: {s['nome']} | Função: {s['funcao']}")

def atualizar_funcao_staff(staff_db, id_s, nova_funcao):
    key = str(id_s)
    if key in staff_db:
        staff_db[key]["funcao"] = nova_funcao
        guardar(STAFF_FILE, staff_db)
        print(f"Função do staff {id_s} atualizada para: {nova_funcao}")
    else:
        print("Staff não encontrado.")

def remover_staff(staff_db, concertos_db, id_s):
    key = str(id_s)
    if key in staff_db:
        nome = staff_db[key]["nome"]
        del staff_db[key]
        # Remove o funcionário de qualquer concerto onde estivesse alocado
        for c_id in concertos_db:
            if id_s in concertos_db[c_id]["ids_staff"]:
                concertos_db[c_id]["ids_staff"].remove(id_s)
        guardar(STAFF_FILE, staff_db)
        guardar(CONCERTOS_FILE, concertos_db)
        print(f"Staff '{nome}' removido do sistema e de todos os turnos.")
    else:
        print("Staff não encontrado.")

# --- CRUD ARTISTAS ---

def criar_artista(artistas_db, nome, genero):
    id_a = str(gerar_id(artistas_db))
    artistas_db[id_a] = {"nome": nome, "genero": genero}
    guardar(ARTISTAS_FILE, artistas_db)
    print(f"Artista '{nome}' registado com ID {id_a}.")
    return int(id_a)

# --- CRUD CONCERTO ---

def criar_concerto(concertos_db, artistas_db, id_artista, data, local):
    if str(id_artista) not in artistas_db:
        print("Erro: Artista não existe na base de dados.")
        return
    id_c = str(gerar_id(concertos_db))
    concertos_db[id_c] = {
        "id_artista": id_artista,
        "ids_staff": [],
        "data": data,
        "local": local,
        "estado": "Agendado",
        "bilhetes_vendidos": 0
    }
    guardar(CONCERTOS_FILE, concertos_db)
    print(f"Concerto {id_c} agendado com sucesso.")
    return int(id_c)

def alocar_staff_concerto(concertos_db, staff_db, id_concerto, id_s):
    key_c = str(id_concerto)
    key_s = str(id_s)
    if key_c not in concertos_db:
        print("Concerto não encontrado.")
        return
    if key_s not in staff_db:
        print("Staff não encontrado.")
        return
    if id_s not in concertos_db[key_c]["ids_staff"]:
        concertos_db[key_c]["ids_staff"].append(id_s)
        guardar(CONCERTOS_FILE, concertos_db)
        print(f"Staff {id_s} alocado ao concerto {id_concerto}.")
    else:
        print("Staff já está alocado a este concerto.")

def listar_agenda(concertos_db, artistas_db):
    print("\n--- AGENDA DE CONCERTOS ---")
    for id_c, info in concertos_db.items():
        artista = artistas_db.get(str(info['id_artista']), {}).get('nome', 'Desconhecido')
        print(
            f"ID: {id_c} | Artista: {artista} | Data: {info['data']} | "
            f"Local: {info['local']} | Estado: {info['estado']}"
        )

# --- EXECUÇÃO DE EXEMPLO ---

if __name__ == "__main__":
    # Carrega tudo dos ficheiros JSON (ou usa dados iniciais se for a primeira execução)
    staff_db, artistas_db, concertos_db = carregar_tudo()

    listar_agenda(concertos_db, artistas_db)

    # Adicionar novo staff e alocar ao concerto 100
    novo_id = criar_staff(staff_db, concertos_db, "111222333", "João Barman", "Barman", "933222111")
    alocar_staff_concerto(concertos_db, staff_db, 100, novo_id)

    # Ver equipa atualizada
    listar_staff_concerto(staff_db, concertos_db, 100)

    # Atualizar função
    atualizar_funcao_staff(staff_db, 1, "Chefe de Som")

    # Remover staff e verificar limpeza
    remover_staff(staff_db, concertos_db, 2)
    listar_staff_concerto(staff_db, concertos_db, 100)

    print("\nDados guardados nos ficheiros JSON com sucesso.")

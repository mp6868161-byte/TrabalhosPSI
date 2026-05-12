import json
import os

FICHEIRO_ARTISTAS = "artistas_db.json"
FICHEIRO_CONCERTOS = "concertos_db.json"

# --- PERSISTÊNCIA ---

def carregar_artistas():
    if os.path.exists(FICHEIRO_ARTISTAS):
        with open(FICHEIRO_ARTISTAS, "r", encoding="utf-8") as f:
            return {int(k): v for k, v in json.load(f).items()}
    # Dados iniciais por defeito
    return {
        10: {"nome": "Xutos & Pontapés", "genero": "Rock Português"},
        11: {"nome": "AC/DC", "genero": "Hard Rock"},
        12: {"nome": "Arctic Monkeys", "genero": "Indie Rock"},
        13: {"nome": "The Rolling Stones", "genero": "Classic Rock"},
        14: {"nome": "Ornatos Alberti", "genero": "Rock Alternativo"}
    }

def guardar_artistas(artistas_db):
    with open(FICHEIRO_ARTISTAS, "w", encoding="utf-8") as f:
        json.dump(artistas_db, f, ensure_ascii=False, indent=4)

def carregar_concertos():
    if os.path.exists(FICHEIRO_CONCERTOS):
        with open(FICHEIRO_CONCERTOS, "r", encoding="utf-8") as f:
            return {int(k): v for k, v in json.load(f).items()}
    # Dados iniciais por defeito
    return {
        100: {
            "id_artista": 10,
            "ids_staff": [1, 2],
            "data": "2024-06-15 21:00",
            "local": "Estádio do Restelo",
            "estado": "Agendado",
            "bilhetes_vendidos": 15000
        }
    }

def guardar_concertos(concertos_db):
    with open(FICHEIRO_CONCERTOS, "w", encoding="utf-8") as f:
        json.dump(concertos_db, f, ensure_ascii=False, indent=4)

# --- CRUD CONCERTO ---

def marcar_concerto(id_c, id_artista, data, local):
    """Create: Regista um novo concerto de rock."""
    if id_c in concertos_db:
        print(f"Erro: O concerto {id_c} já existe.")
        return
    if id_artista not in artistas_db:
        print(f"Erro: Banda com ID {id_artista} não encontrada.")
        return
    concertos_db[id_c] = {
        "id_artista": id_artista,
        "ids_staff": [],
        "data": data,
        "local": local,
        "estado": "Agendado",
        "bilhetes_vendidos": 0
    }
    guardar_concertos(concertos_db)
    print(f"Concerto de '{artistas_db[id_artista]['nome']}' agendado para {local}!")

def listar_agenda():
    """Read: Lista a agenda de rock."""
    print("\n" + "=" * 55)
    print(" TOUR DATES - ROCK MANAGER ")
    print("=" * 55)
    for id_c, info in concertos_db.items():
        banda = artistas_db[info['id_artista']]['nome']
        genero = artistas_db[info['id_artista']]['genero']
        print(f"[{info['estado']}] {banda} ({genero})")
        print(f"      ID: {id_c} | Data: {info['data']} | Local: {info['local']}")
        print(f"      Público: {info['bilhetes_vendidos']} fãs")
        print("-" * 40)

def atualizar_concerto(id_c, nova_data=None, novo_local=None, novo_estado=None):
    """Update: Altera detalhes do show."""
    if id_c not in concertos_db:
        print("Erro: Concerto não encontrado.")
        return
    if nova_data: concertos_db[id_c]["data"] = nova_data
    if novo_local: concertos_db[id_c]["local"] = novo_local
    if novo_estado: concertos_db[id_c]["estado"] = novo_estado
    guardar_concertos(concertos_db)
    print(f"Concerto {id_c} atualizado.")

def cancelar_concerto(id_c):
    """Delete: Remove o concerto."""
    if id_c in concertos_db:
        banda = artistas_db[concertos_db[id_c]['id_artista']]['nome']
        del concertos_db[id_c]
        guardar_concertos(concertos_db)
        print(f"Concerto de {banda} cancelado.")
    else:
        print("Erro: Concerto não encontrado.")

# --- Carrega dados persistidos (ou dados iniciais se for a primeira execução) ---
artistas_db = carregar_artistas()
concertos_db = carregar_concertos()

# Garante que os ficheiros existem desde o início
guardar_artistas(artistas_db)
guardar_concertos(concertos_db)

# --- TESTE DAS BANDAS ---
if __name__ == "__main__":
    marcar_concerto(101, 11, "2024-07-10 20:00", "Passeio Marítimo de Algés")
    marcar_concerto(102, 14, "2024-09-20 22:00", "Coliseu Porto")

    concertos_db[101]["bilhetes_vendidos"] = 55000
    guardar_concertos(concertos_db)

    atualizar_concerto(101, novo_estado="SOLDOUT")
    listar_agenda()

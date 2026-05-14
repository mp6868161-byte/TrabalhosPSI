import json
import os

FICHEIRO_CONCERTOS = "concertos_db.json"
FICHEIRO_ARTISTAS = "artistas_db.json"

concertos_db = {}
artistas_db = {}

# ==========================
# Persistência
# ==========================

def guardar_concertos():
    try:
        with open(FICHEIRO_CONCERTOS, "w", encoding="utf-8") as ficheiro:
            json.dump(concertos_db, ficheiro, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao guardar concertos: {e}")

def carregar_concertos():
    global concertos_db
    try:
        if os.path.exists(FICHEIRO_CONCERTOS):
            with open(FICHEIRO_CONCERTOS, "r", encoding="utf-8") as ficheiro:
                concertos_db = json.load(ficheiro)
        else:
            concertos_db = {}
    except (json.JSONDecodeError, IOError):
        concertos_db = {}

def guardar_artistas():
    try:
        with open(FICHEIRO_ARTISTAS, "w", encoding="utf-8") as ficheiro:
            json.dump(artistas_db, ficheiro, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao guardar artistas: {e}")

def carregar_artistas():
    global artistas_db
    try:
        if os.path.exists(FICHEIRO_ARTISTAS):
            with open(FICHEIRO_ARTISTAS, "r", encoding="utf-8") as ficheiro:
                artistas_db = json.load(ficheiro)
        else:
            artistas_db = {}
    except (json.JSONDecodeError, IOError):
        artistas_db = {}

# ==========================
# CREATE
# ==========================

def marcar_concerto(id_concerto, id_artista, data, local):
    carregar_concertos()
    carregar_artistas()

    if id_concerto in concertos_db:
        return 409, f"Já existe um concerto com o ID {id_concerto}."

    if str(id_artista) not in artistas_db:
        return 404, f"Artista com ID {id_artista} não encontrado."

    concertos_db[id_concerto] = {
        "id": id_concerto,
        "id_artista": id_artista,
        "ids_staff": [],
        "data": data,
        "local": local,
        "estado": "Agendado",
        "bilhetes_vendidos": 0
    }

    guardar_concertos()
    return 201, concertos_db[id_concerto]

# ==========================
# READ ALL
# ==========================

def listar_concertos():
    carregar_concertos()

    if not concertos_db:
        return 404, "Não existem concertos registados."

    return 200, concertos_db

# ==========================
# READ ONE
# ==========================

def consultar_concerto(id_concerto):
    carregar_concertos()

    if id_concerto not in concertos_db:
        return 404, "Concerto não encontrado."

    return 200, concertos_db[id_concerto]

# ==========================
# UPDATE
# ==========================

def atualizar_concerto(id_concerto, id_artista=None, data=None, local=None, estado=None, bilhetes_vendidos=None):
    carregar_concertos()
    carregar_artistas()

    if id_concerto not in concertos_db:
        return 404, "Concerto não encontrado."

    if id_artista is not None:
        if str(id_artista) not in artistas_db:
            return 404, f"Artista com ID {id_artista} não encontrado."
        concertos_db[id_concerto]["id_artista"] = id_artista

    if data is not None:
        concertos_db[id_concerto]["data"] = data
    if local is not None:
        concertos_db[id_concerto]["local"] = local
    if estado is not None:
        concertos_db[id_concerto]["estado"] = estado
    if bilhetes_vendidos is not None:
        concertos_db[id_concerto]["bilhetes_vendidos"] = bilhetes_vendidos

    guardar_concertos()
    return 200, concertos_db[id_concerto]

# ==========================
# DELETE
# ==========================

def cancelar_concerto(id_concerto):
    carregar_concertos()

    if id_concerto not in concertos_db:
        return 404, "Concerto não encontrado."

    concerto_removido = concertos_db.pop(id_concerto)
    guardar_concertos()
    return 200, concerto_removido

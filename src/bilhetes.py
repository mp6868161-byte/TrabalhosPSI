import json
import os

FICHEIRO_BILHETES = "bilheteira.json"
bilheteira = {}

# ==========================
# Persistência
# ==========================

def guardar_bilhetes():
    try:
        with open(FICHEIRO_BILHETES, "w", encoding="utf-8") as ficheiro:
            json.dump(bilheteira, ficheiro, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao guardar bilhetes: {e}")

def carregar_bilhetes():
    global bilheteira
    try:
        if os.path.exists(FICHEIRO_BILHETES):
            with open(FICHEIRO_BILHETES, "r", encoding="utf-8") as ficheiro:
                bilheteira = json.load(ficheiro)
        else:
            bilheteira = {}
    except (json.JSONDecodeError, IOError):
        bilheteira = {}

# ==========================
# CREATE
# ==========================

def criar_bilhete(id_bilhete, preco, tipo, lugar, fila, id_concerto):
    carregar_bilhetes()

    if id_bilhete in bilheteira:
        return 409, f"Já existe um bilhete com o ID {id_bilhete}."

    bilheteira[id_bilhete] = {
        "id": id_bilhete,
        "preco": preco,
        "tipo": tipo,
        "lugar": lugar,
        "fila": fila,
        "id_concerto": id_concerto
    }

    guardar_bilhetes()
    return 201, bilheteira[id_bilhete]

# ==========================
# READ ALL
# ==========================

def listar_bilhetes():
    carregar_bilhetes()

    if not bilheteira:
        return 404, "A bilheteira está vazia."

    return 200, bilheteira

# ==========================
# READ ONE
# ==========================

def consultar_bilhete(id_bilhete):
    carregar_bilhetes()

    if id_bilhete not in bilheteira:
        return 404, "Bilhete não encontrado."

    return 200, bilheteira[id_bilhete]

# ==========================
# UPDATE
# ==========================

def atualizar_bilhete(id_bilhete, preco=None, tipo=None, lugar=None, fila=None, id_concerto=None):
    carregar_bilhetes()

    if id_bilhete not in bilheteira:
        return 404, "Bilhete não encontrado."

    if preco is not None:
        bilheteira[id_bilhete]["preco"] = preco
    if tipo is not None:
        bilheteira[id_bilhete]["tipo"] = tipo
    if lugar is not None:
        bilheteira[id_bilhete]["lugar"] = lugar
    if fila is not None:
        bilheteira[id_bilhete]["fila"] = fila
    if id_concerto is not None:
        bilheteira[id_bilhete]["id_concerto"] = id_concerto

    guardar_bilhetes()
    return 200, bilheteira[id_bilhete]

# ==========================
# DELETE
# ==========================

def eliminar_bilhete(id_bilhete):
    carregar_bilhetes()

    if id_bilhete not in bilheteira:
        return 404, "Bilhete não encontrado."

    bilhete_removido = bilheteira.pop(id_bilhete)
    guardar_bilhetes()
    return 200, bilhete_removido

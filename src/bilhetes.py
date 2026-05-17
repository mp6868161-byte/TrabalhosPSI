import json
import os
import utils

FICHEIRO_BILHETES = "bilheteira.json"
bilheteira = {}


# ==========================
# Persistência
# ==========================

def guardar_bilhetes():
    with open(FICHEIRO_BILHETES, "w", encoding="utf-8") as ficheiro:
        json.dump(bilheteira, ficheiro, indent=4, ensure_ascii=False)


def carregar_bilhetes():
    global bilheteira
    if os.path.exists(FICHEIRO_BILHETES):
        with open(FICHEIRO_BILHETES, "r", encoding="utf-8") as ficheiro:
            bilheteira = json.load(ficheiro)
    else:
        bilheteira = {}


# ==========================
# CREATE
# ==========================

def criar_bilhete(preco, tipo, lugar, fila, id_concerto):
    carregar_bilhetes()

    # O ID deve ser gerado automaticamente para seguir o padrão
    id_bilhete = utils.gerar_id("B", bilheteira)

    novo_bilhete = {
        "id": id_bilhete,
        "preco": preco,
        "tipo": tipo,
        "lugar": lugar,
        "fila": fila,
        "id_concerto": id_concerto
    }

    bilheteira[id_bilhete] = novo_bilhete
    guardar_bilhetes()

    return 201, novo_bilhete


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
    if tipo:
        bilheteira[id_bilhete]["tipo"] = tipo
    if lugar:
        bilheteira[id_bilhete]["lugar"] = lugar
    if fila:
        bilheteira[id_bilhete]["fila"] = fila
    if id_concerto:
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

    del bilheteira[id_bilhete]
    guardar_bilhetes()

    return 200, id_bilhete

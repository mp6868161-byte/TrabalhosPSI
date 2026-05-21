import json
import os
import logging
import utils

FICHEIRO_BILHETES = "bilheteira.json"
bilheteira = {}

logger = logging.getLogger(__name__)

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

    try:
        guardar_bilhetes()
        logger.info(f"criar_bilhete(): bilhete {id_bilhete} emitido — {tipo}, lugar {lugar}")
    except IOError as e:
        logger.error(f"criar_bilhete(): erro ao guardar bilheteira.json — {e}")

    return 201, novo_bilhete


# ==========================
# READ ALL
# ==========================

def listar_bilhetes():
    carregar_bilhetes()
    if not bilheteira:
        logger.warning("listar_bilhetes(): bilheteira vazia")
        return 404, "A bilheteira está vazia."
    logger.debug(f"listar_bilhetes(): {len(bilheteira)} bilhetes carregados")
    return 200, bilheteira


# ==========================
# READ ONE
# ==========================

def consultar_bilhete(id_bilhete):
    carregar_bilhetes()
    if id_bilhete not in bilheteira:
        logger.warning(f"consultar_bilhete(): bilhete {id_bilhete} não encontrado")
        return 404, "Bilhete não encontrado."
    logger.info(f"consultar_bilhete(): bilhete {id_bilhete} consultado com sucesso")
    return 200, bilheteira[id_bilhete]


# ==========================
# UPDATE
# ==========================

def atualizar_bilhete(id_bilhete, preco=None, tipo=None, lugar=None, fila=None, id_concerto=None):
    carregar_bilhetes()

    if id_bilhete not in bilheteira:
        logger.warning(f"atualizar_bilhete(): bilhete {id_bilhete} não encontrado")
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

    try:
        guardar_bilhetes()
        logger.info(f"atualizar_bilhete(): bilhete {id_bilhete} atualizado com sucesso")
    except IOError as e:
        logger.error(f"atualizar_bilhete(): erro ao guardar bilheteira.json — {e}")

    return 200, bilheteira[id_bilhete]


# ==========================
# DELETE
# ==========================

def eliminar_bilhete(id_bilhete):
    carregar_bilhetes()

    if id_bilhete not in bilheteira:
        logger.warning(f"eliminar_bilhete(): bilhete {id_bilhete} não encontrado")
        return 404, "Bilhete não encontrado."

    del bilheteira[id_bilhete]

    try:
        guardar_bilhetes()
        logger.info(f"eliminar_bilhete(): bilhete {id_bilhete} eliminado com sucesso")
    except IOError as e:
        logger.error(f"eliminar_bilhete(): erro ao guardar bilheteira.json — {e}")

    return 200, id_bilhete

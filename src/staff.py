import json
import os
import logging

FICHEIRO_STAFF = "staff_db.json"

staff_db = {}

logger = logging.getLogger(__name__)

# ==========================
# Persistência
# ==========================

def guardar_staff():
    try:
        with open(FICHEIRO_STAFF, "w", encoding="utf-8") as ficheiro:
            json.dump(staff_db, ficheiro, indent=4, ensure_ascii=False)
    except IOError as e:
        logger.error(f"guardar_staff(): erro ao guardar staff_db.json — {e}")

def carregar_staff():
    global staff_db
    try:
        if os.path.exists(FICHEIRO_STAFF):
            with open(FICHEIRO_STAFF, "r", encoding="utf-8") as ficheiro:
                staff_db = json.load(ficheiro)
        else:
            staff_db = {}
    except (json.JSONDecodeError, IOError):
        staff_db = {}

# ==========================
# CREATE
# ==========================

def criar_staff(nif, nome, funcao, telemovel):
    carregar_staff()

    if any(s["nif"] == nif for s in staff_db.values()):
        logger.warning(f"criar_staff(): NIF duplicado — {nif}")
        return 409, f"Já existe um membro de staff com o NIF {nif}."

    if not nif or not nome or not funcao or not telemovel:
        logger.warning("criar_staff(): campos obrigatórios em falta")
        return 400, "Todos os campos são obrigatórios."

    id_staff = str(max((int(k) for k in staff_db.keys()), default=0) + 1)

    staff_db[id_staff] = {
        "id": id_staff,
        "nif": nif,
        "nome": nome,
        "funcao": funcao,
        "telemovel": telemovel
    }

    guardar_staff()
    logger.info(f"criar_staff(): staff ID {id_staff} registado — {nome}")
    return 201, staff_db[id_staff]

# ==========================
# READ ALL
# ==========================

def listar_staff():
    carregar_staff()

    if not staff_db:
        logger.warning("listar_staff(): nenhum membro de staff registado")
        return 404, "Não existem membros de staff registados."

    logger.debug(f"listar_staff(): {len(staff_db)} membros carregados")
    return 200, staff_db

# ==========================
# READ ONE
# ==========================

def consultar_staff(id_staff):
    carregar_staff()

    if id_staff not in staff_db:
        logger.warning(f"consultar_staff(): staff ID {id_staff} não encontrado")
        return 404, "Membro de staff não encontrado."

    logger.info(f"consultar_staff(): staff ID {id_staff} consultado com sucesso")
    return 200, staff_db[id_staff]

# ==========================
# UPDATE
# ==========================

def atualizar_staff(id_staff, nif=None, nome=None, funcao=None, telemovel=None):
    carregar_staff()

    if id_staff not in staff_db:
        logger.warning(f"atualizar_staff(): staff ID {id_staff} não encontrado")
        return 404, "Membro de staff não encontrado."

    if nif is not None:
        if any(s["nif"] == nif and k != id_staff for k, s in staff_db.items()):
            logger.warning(f"atualizar_staff(): NIF duplicado — {nif}")
            return 409, f"Já existe outro membro de staff com o NIF {nif}."
        staff_db[id_staff]["nif"] = nif
    if nome is not None:
        staff_db[id_staff]["nome"] = nome
    if funcao is not None:
        staff_db[id_staff]["funcao"] = funcao
    if telemovel is not None:
        staff_db[id_staff]["telemovel"] = telemovel

    guardar_staff()
    logger.info(f"atualizar_staff(): staff ID {id_staff} atualizado com sucesso")
    return 200, staff_db[id_staff]

# ==========================
# DELETE
# ==========================

def remover_staff(id_staff):
    carregar_staff()

    if id_staff not in staff_db:
        logger.warning(f"remover_staff(): staff ID {id_staff} não encontrado")
        return 404, "Membro de staff não encontrado."

    staff_removido = staff_db.pop(id_staff)
    guardar_staff()
    logger.info(f"remover_staff(): staff ID {id_staff} removido com sucesso")
    return 200, staff_removido

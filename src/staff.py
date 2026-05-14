import json
import os

FICHEIRO_STAFF = "staff_db.json"

staff_db = {}

# ==========================
# Persistência
# ==========================

def guardar_staff():
    try:
        with open(FICHEIRO_STAFF, "w", encoding="utf-8") as ficheiro:
            json.dump(staff_db, ficheiro, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao guardar staff: {e}")

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
        return 409, f"Já existe um membro de staff com o NIF {nif}."

    if not nif or not nome or not funcao or not telemovel:
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
    return 201, staff_db[id_staff]

# ==========================
# READ ALL
# ==========================

def listar_staff():
    carregar_staff()

    if not staff_db:
        return 404, "Não existem membros de staff registados."

    return 200, staff_db

# ==========================
# READ ONE
# ==========================

def consultar_staff(id_staff):
    carregar_staff()

    if id_staff not in staff_db:
        return 404, "Membro de staff não encontrado."

    return 200, staff_db[id_staff]

# ==========================
# UPDATE
# ==========================

def atualizar_staff(id_staff, nif=None, nome=None, funcao=None, telemovel=None):
    carregar_staff()

    if id_staff not in staff_db:
        return 404, "Membro de staff não encontrado."

    if nif is not None:
        if any(s["nif"] == nif and k != id_staff for k, s in staff_db.items()):
            return 409, f"Já existe outro membro de staff com o NIF {nif}."
        staff_db[id_staff]["nif"] = nif
    if nome is not None:
        staff_db[id_staff]["nome"] = nome
    if funcao is not None:
        staff_db[id_staff]["funcao"] = funcao
    if telemovel is not None:
        staff_db[id_staff]["telemovel"] = telemovel

    guardar_staff()
    return 200, staff_db[id_staff]

# ==========================
# DELETE
# ==========================

def remover_staff(id_staff):
    carregar_staff()

    if id_staff not in staff_db:
        return 404, "Membro de staff não encontrado."

    staff_removido = staff_db.pop(id_staff)
    guardar_staff()
    return 200, staff_removido

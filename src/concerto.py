import json
import os
import logging
import utils

FICHEIRO_CONCERTOS = "concertos.json"
db_concertos = {}

logger = logging.getLogger(__name__)


def guardar_concertos():
    with open(FICHEIRO_CONCERTOS, "w", encoding="utf-8") as f:
        json.dump(db_concertos, f, indent=4, ensure_ascii=False)


def carregar_concertos():
    global db_concertos
    if os.path.exists(FICHEIRO_CONCERTOS):
        with open(FICHEIRO_CONCERTOS, "r", encoding="utf-8") as f:
            db_concertos = json.load(f)
    else:
        db_concertos = {}


def criar_concerto(nome, data, local, id_artista):
    carregar_concertos()
    id_c = utils.gerar_id("C", db_concertos)

    novo = {"id": id_c, "nome": nome, "data": data, "local": local, "id_artista": id_artista}
    db_concertos[id_c] = novo

    try:
        guardar_concertos()
        logger.info(f"criar_concerto(): concerto {id_c} agendado — {nome}, {data}")
    except IOError as e:
        logger.error(f"criar_concerto(): erro ao guardar concertos.json — {e}")

    return 201, novo


def atualizar_concerto(id_c, nome=None, data=None, local=None):
    carregar_concertos()
    if id_c not in db_concertos:
        logger.warning(f"atualizar_concerto(): concerto {id_c} não encontrado")
        return 404, "Concerto não encontrado"

    if nome: db_concertos[id_c]["nome"] = nome
    if data: db_concertos[id_c]["data"] = data
    if local: db_concertos[id_c]["local"] = local

    try:
        guardar_concertos()
        logger.info(f"atualizar_concerto(): concerto {id_c} atualizado com sucesso")
    except IOError as e:
        logger.error(f"atualizar_concerto(): erro ao guardar concertos.json — {e}")

    return 200, db_concertos[id_c]


def eliminar_concerto(id_c):
    carregar_concertos()
    if id_c not in db_concertos:
        logger.warning(f"eliminar_concerto(): concerto {id_c} não encontrado")
        return 404, "Concerto não encontrado"

    del db_concertos[id_c]

    try:
        guardar_concertos()
        logger.info(f"eliminar_concerto(): concerto {id_c} cancelado com sucesso")
    except IOError as e:
        logger.error(f"eliminar_concerto(): erro ao guardar concertos.json — {e}")

    return 200, id_c


def listar_concertos():
    carregar_concertos()
    if not db_concertos:
        logger.warning("listar_concertos(): nenhum concerto agendado")
        return 404, "Não existem concertos agendados."
    logger.debug(f"listar_concertos(): {len(db_concertos)} concertos carregados")
    return 200, db_concertos

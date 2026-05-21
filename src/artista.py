import utils
import json
import os
import logging

db_artistas = {}
FICHEIRO_ARTISTAS = "artistas.json"

logger = logging.getLogger(__name__)

def guardar_artistas():
    try:
        with open(FICHEIRO_ARTISTAS, "w", encoding="utf-8") as ficheiro:
            json.dump(db_artistas, ficheiro, indent=4, ensure_ascii=False)
    except IOError as e:
        logger.error(f"guardar_artistas(): erro ao guardar artistas.json — {e}")

def carregar_artistas():
    global db_artistas
    try:
        if os.path.exists(FICHEIRO_ARTISTAS):
            with open(FICHEIRO_ARTISTAS, "r", encoding="utf-8") as ficheiro:
                db_artistas = json.load(ficheiro)
        else:
            db_artistas = {}
    except (json.JSONDecodeError, IOError):
        db_artistas = {}

def criar_artista(nome, genero):
    carregar_artistas()
    id_artista = utils.gerar_id("A", db_artistas)

    db_artistas[id_artista] = {
        "id": id_artista,
        "nome": nome,
        "genero": genero
    }
    guardar_artistas()
    logger.info(f"criar_artista(): artista {id_artista} criado — {nome}")
    return 201, db_artistas[id_artista]


def ler_artistas():
    carregar_artistas()

    if not db_artistas:
        logger.warning("ler_artistas(): nenhum artista registado")
        return 404, "Não existem artistas"

    logger.debug(f"ler_artistas(): {len(db_artistas)} artistas carregados")
    return 200, db_artistas


def atualizar_artista():
    utils.exibir_cabecalho("Atualizar Artista")

    id_procura = input("Introduza o ID do artista a editar: ").strip()

    if id_procura not in db_artistas:
        logger.warning(f"atualizar_artista(): artista {id_procura} não encontrado")
        return 404

    print(f"Dados atuais -> Nome: {db_artistas[id_procura]['nome']}")

    db_artistas[id_procura]["nome"] = utils.ler_obrigatorio("Novo Nome: ")
    db_artistas[id_procura]["genero"] = utils.ler_obrigatorio("Novo Género: ")

    guardar_artistas()
    logger.info(f"atualizar_artista(): artista {id_procura} atualizado com sucesso")
    return 200


def eliminar_artista():
    utils.exibir_cabecalho("Eliminar Artista")

    id_procura = input("Introduza o ID do artista a remover: ").strip()

    if id_procura in db_artistas:
        del db_artistas[id_procura]
        guardar_artistas()
        logger.info(f"eliminar_artista(): artista {id_procura} removido com sucesso")
        return 200

    logger.warning(f"eliminar_artista(): artista {id_procura} não encontrado")
    return 404

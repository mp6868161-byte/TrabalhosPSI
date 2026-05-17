import utils
import json
import os

db_artistas = {}
FICHEIRO_ARTISTAS = "artistas.json"

def guardar_artistas():
    try:
        with open(FICHEIRO_ARTISTAS, "w", encoding="utf-8") as ficheiro:
            json.dump(db_artistas, ficheiro, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao guardar artistas: {e}")

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
    """
    Cria um novo artista e adiciona ao dicionário.
    Retorna 201 em caso de sucesso ou 400 se os dados forem inválidos.
    """
    carregar_artistas()
    id_artista = utils.gerar_id("A", db_artistas)

    db_artistas[id_artista] = {
        "id": id_artista,
        "nome": nome,
        "genero": genero
    }
    guardar_artistas()
    return 201, db_artistas[id_artista]


def ler_artistas():
    """
    Lista todos os artistas registados.
    Retorna 200 se existirem dados ou 404 se estiver vazio.
    """
    carregar_artistas()

    if not db_artistas:
        return 404, "Não existem artistas"

    return 200, db_artistas


def atualizar_artista():
    """
    Atualiza os dados de um artista existente.
    """
    utils.exibir_cabecalho("Atualizar Artista")

    id_procura = input("Introduza o ID do artista a editar: ").strip()

    if id_procura not in db_artistas:
        return 404

    print(f"Dados atuais -> Nome: {db_artistas[id_procura]['nome']}")

    db_artistas[id_procura]["nome"] = utils.ler_obrigatorio("Novo Nome: ")
    db_artistas[id_procura]["genero"] = utils.ler_obrigatorio("Novo Género: ")

    return 200


def eliminar_artista():
    """
    Remove um artista do sistema.
    """
    utils.exibir_cabecalho("Eliminar Artista")

    id_procura = input("Introduza o ID do artista a remover: ").strip()

    if id_procura in db_artistas:
        del db_artistas[id_procura]
        return 200

    return 404

import json
import os
import utils

FICHEIRO_ARTISTAS = "artistas.json"
db_artistas = {}

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

# ==========================
# CREATE
# ==========================

def criar_artista():
    """
    Cria um novo artista e adiciona ao dicionário.
    Retorna 201 em caso de sucesso ou 400 se os dados forem inválidos.
    """
    carregar_artistas()
    utils.exibir_cabecalho("Registar Artista")

    id_artista = utils.gerar_id("A", db_artistas)
    nome = utils.ler_obrigatorio("Nome do Artista/Banda: ")
    genero = utils.ler_obrigatorio("Género Musical: ")

    db_artistas[id_artista] = {
        "id": id_artista,
        "nome": nome,
        "genero": genero
    }

    guardar_artistas()
    print(f"ID atribuído: {id_artista}")
    return 201

# ==========================
# READ ALL
# ==========================

def ler_artistas():
    """
    Lista todos os artistas registados.
    Retorna 200 se existirem dados ou 404 se estiver vazio.
    """
    carregar_artistas()
    utils.exibir_cabecalho("Lista de Artistas")

    if not db_artistas:
        return 404

    for art in db_artistas.values():
        print(f"ID: {art['id']} | Nome: {art['nome']} | Género: {art['genero']}")

    return 200

# ==========================
# READ ONE
# ==========================

def consultar_artista(id_artista):
    """
    Consulta um artista pelo ID.
    Retorna 200 e os dados, ou 404 se não existir.
    """
    carregar_artistas()

    if id_artista not in db_artistas:
        return 404, "Artista não encontrado."

    return 200, db_artistas[id_artista]

# ==========================
# UPDATE
# ==========================

def atualizar_artista():
    """
    Atualiza os dados de um artista existente.
    """
    carregar_artistas()
    utils.exibir_cabecalho("Atualizar Artista")

    id_procura = input("Introduza o ID do artista a editar: ").strip()

    if id_procura not in db_artistas:
        return 404

    print(f"Dados atuais -> Nome: {db_artistas[id_procura]['nome']} | Género: {db_artistas[id_procura]['genero']}")

    db_artistas[id_procura]["nome"] = utils.ler_obrigatorio("Novo Nome: ")
    db_artistas[id_procura]["genero"] = utils.ler_obrigatorio("Novo Género: ")

    guardar_artistas()
    return 200

# ==========================
# DELETE
# ==========================

def eliminar_artista():
    """
    Remove um artista do sistema.
    """
    carregar_artistas()
    utils.exibir_cabecalho("Eliminar Artista")

    id_procura = input("Introduza o ID do artista a remover: ").strip()

    if id_procura not in db_artistas:
        return 404

    del db_artistas[id_procura]
    guardar_artistas()
    return 200

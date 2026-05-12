 import artista  # Import para validar contra o db_artistas

db_bilhetes = {}


def criar_bilhete(id_b, id_c, preco, tipo, lugar, fila):
    # Valida se o artista existe no outro módulo
    if id_c not in artista.db_artistas:
        return 404, "Erro: ID de Artista/Concerto inexistente."

    if id_b in db_bilhetes:
        return 400, "Erro: ID de Bilhete já existe."

    db_bilhetes[id_b] = {
        "id": id_b,
        "id_concerto": id_c,
        "nome_artista": artista.db_artistas[id_c]["nome"],
        "preco": float(preco),
        "tipo": tipo,
        "lugar": lugar,
        "fila": fila
    }
    return 201, "Bilhete emitido com sucesso."


def ler_bilhetes():
    if not db_bilhetes:
        return 404, "Sem bilhetes emitidos."
    return 200, db_bilhetes

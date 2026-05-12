db_artistas = {}


def criar_artista(idx, nome, genero, nacionalidade="N/A", hora="00:00"):
    if idx in db_artistas:
        return 400, "Erro: ID de artista já existe."

    db_artistas[idx] = {
        "id": idx,
        "nome": nome,
        "genero": genero,
        "nacionalidade": nacionalidade,
        "hora_concerto": hora
    }
    return 201, f"Artista {nome} registado."


def ler_artistas():
    if not db_artistas:
        return 404, "Nenhum artista na base de dados."
    return 200, db_artistas


def eliminar_artista(idx):
    if idx in db_artistas:
        del db_artistas[idx]
        return 200, "Artista removido."
    return 404, "Erro: ID não encontrado."

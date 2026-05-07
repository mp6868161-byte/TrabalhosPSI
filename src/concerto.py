
artistas_db = {
    10: {"nome": "Xutos & Pontapés", "genero": "Rock Português"},
    11: {"nome": "AC/DC", "genero": "Hard Rock"},
    12: {"nome": "Arctic Monkeys", "genero": "Indie Rock"},
    13: {"nome": "The Rolling Stones", "genero": "Classic Rock"},
    14: {"nome": "Ornatos Alberti", "genero": "Rock Alternativo"}
}

concertos_db = {
    100: {
        "id_artista": 10,
        "ids_staff": [1, 2],
        "data": "2024-06-15 21:00",
        "local": "Estádio do Restelo",
        "estado": "Agendado",
        "bilhetes_vendidos": 15000
    }
}


# --- CRUD CONCERTO ---

def marcar_concerto(id_c, id_artista, data, local):
    """Create: Regista um novo concerto de rock."""
    if id_c in concertos_db:
        print(f"Erro: O concerto {id_c} já existe.")
        return

    if id_artista not in artistas_db:
        print(f"Erro: Banda com ID {id_artista} não encontrada.")
        return

    concertos_db[id_c] = {
        "id_artista": id_artista,
        "ids_staff": [],
        "data": data,
        "local": local,
        "estado": "Agendado",
        "bilhetes_vendidos": 0
    }
    print(f"Concerto de '{artistas_db[id_artista]['nome']}' agendado para {local}!")


def listar_agenda():
    """Read: Lista a agenda de rock."""
    print("\n" + "=" * 55)
    print(" TOUR DATES - ROCK MANAGER ")
    print("=" * 55)
    for id_c, info in concertos_db.items():
        banda = artistas_db[info['id_artista']]['nome']
        genero = artistas_db[info['id_artista']]['genero']
        print(f"[{info['estado']}] {banda} ({genero})")
        print(f"      ID: {id_c} | Data: {info['data']} | Local: {info['local']}")
        print(f"      Público: {info['bilhetes_vendidos']} fãs")
        print("-" * 40)


def atualizar_concerto(id_c, nova_data=None, novo_local=None, novo_estado=None):
    """Update: Altera detalhes do show."""
    if id_c not in concertos_db:
        print("Erro: Concerto não encontrado.")
        return

    if nova_data: concertos_db[id_c]["data"] = nova_data
    if novo_local: concertos_db[id_c]["local"] = novo_local
    if novo_estado: concertos_db[id_c]["estado"] = novo_estado

    print(f"Concerto {id_c} atualizado.")


def cancelar_concerto(id_c):
    """Delete: Remove o concerto."""
    if id_c in concertos_db:
        banda = artistas_db[concertos_db[id_c]['id_artista']]['nome']
        del concertos_db[id_c]
        print(f"Concerto de {banda} cancelado.")
    else:
        print("Erro: Concerto não encontrado.")


# --- TESTE DAS BANDAS ---
if __name__ == "__main__":
    # Marcar novas datas da tour
    marcar_concerto(101, 11, "2024-07-10 20:00", "Passeio Marítimo de Algés")
    marcar_concerto(102, 14, "2024-09-20 22:00", "Coliseu Porto")

    # Simular venda massiva
    concertos_db[101]["bilhetes_vendidos"] = 55000
    atualizar_concerto(101, novo_estado="SOLDOUT")

    # Listar tudo
    listar_agenda()

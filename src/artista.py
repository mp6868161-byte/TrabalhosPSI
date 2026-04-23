artistas = []
proximo_id = 1


def criar_artista(nome, genero, nacionalidade, hora_concerto):
    global proximo_id
    novo_artista = {
        "id": proximo_id,
        "nome": nome,
        "genero": genero,
        "nacionalidade": nacionalidade,
        "hora_concerto": hora_concerto
    }
    artistas.append(novo_artista)
    proximo_id += 1
    print(f"'{nome}' adicionado ao lineup das {hora_concerto}!")

    return novo_artista


def listar_apenas_rock():
    print("\n--- LINEUP: PALCO ROCK ---")
    lista_rock = []

    for artista in artistas:
        if "rock" in artista["genero"].lower():
            formato = (f"[{artista['hora_concerto']}] ID: {artista['id']} | "
                       f"{artista['nome'].upper()} ({artista['genero']}) - "
                       f"{artista['nacionalidade']}")
            print(formato)
            lista_rock.append(artista)

    if not lista_rock:
        print("Nenhum artista de Rock escalado ainda.")


    return lista_rock


# --- Execução ---

artista1 = criar_artista("Jorge Ben Jor", "Samba-Rock", "Brasil", "21:00")
criar_artista("Arctic Monkeys", "Indie Rock", "UK", "23:30")
criar_artista("Bon-jovi", "Hard Rock", "EUA", "01:00")
criar_artista("AC/DC", "Hard Rock", "Austrália", "22:00")


apenas_rock = listar_apenas_rock()


print(f"\nTotal de artistas: {len(apenas_rock)}")
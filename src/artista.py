import json
import os

FICHEIRO_DADOS = "artistas.json"

def carregar_dados():
    """Carrega artistas e próximo ID do ficheiro JSON."""
    if os.path.exists(FICHEIRO_DADOS):
        with open(FICHEIRO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return dados.get("artistas", []), dados.get("proximo_id", 1)
    return [], 1

def guardar_dados(artistas, proximo_id):
    """Guarda artistas e próximo ID no ficheiro JSON."""
    with open(FICHEIRO_DADOS, "w", encoding="utf-8") as f:
        json.dump({"artistas": artistas, "proximo_id": proximo_id}, f, ensure_ascii=False, indent=4)

def criar_artista(nome, genero, nacionalidade, hora_concerto):
    global artistas, proximo_id
    novo_artista = {
        "id": proximo_id,
        "nome": nome,
        "genero": genero,
        "nacionalidade": nacionalidade,
        "hora_concerto": hora
    }
    artistas.append(novo_artista)
    proximo_id += 1
    guardar_dados(artistas, proximo_id)
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

# --- Carrega dados persistidos (ou começa do zero) ---
artistas, proximo_id = carregar_dados()

# --- Execução ---
artista1 = criar_artista("Jorge Ben Jor", "Samba-Rock", "Brasil", "21:00")
criar_artista("Arctic Monkeys", "Indie Rock", "UK", "23:30")
criar_artista("Bon-jovi", "Hard Rock", "EUA", "01:00")
criar_artista("AC/DC", "Hard Rock", "Austrália", "22:00")

apenas_rock = listar_apenas_rock()
print(f"\nTotal de artistas rock: {len(apenas_rock)}")
print(f"Total de artistas no lineup: {len(artistas)}")

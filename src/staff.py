staff_db = {
    1: {"nif": "123456789", "nome": "Carlos Silva", "funcao": "Técnico de Som", "telemovel": "912345678"},
    2: {"nif": "987654321", "nome": "Ana Rita", "funcao": "Segurança", "telemovel": "961234567"}
}

artistas_db = {
    10: {"nome": "The Rock Band", "genero": "Rock"},
    11: {"nome": "DJ Sunset", "genero": "Electronic"}
}

concertos_db = {
    100: {
        "id_artista": 10,
        "ids_staff": [1, 2],
        "data": "2024-06-15 21:00",
        "local": "Altice Arena",
        "estado": "Agendado",
        "bilhetes_vendidos": 1500
    }
}


# --- CRUD STAFF ---

def criar_staff(nif, nome, funcao, telemovel):
    id_s = gerar_id_staff()
    if id_s in staff_db:
        print(f"Erro: ID {id_s} já existe.")
        return
    staff_db[id_s] = {
        "nif": nif,
        "nome": nome,
        "funcao": funcao,
        "telemovel": telemovel
    }
    print(f"Staff '{nome}' registado com sucesso.")


def listar_staff_concerto(id_concerto):
    concerto = concertos_db.get(id_concerto)
    if not concerto:
        print("Concerto não encontrado.")
        return

    print(f"\nEquipa alocada ao Concerto {id_concerto} ({concerto['local']}):")
    for id_s in concerto["ids_staff"]:
        s = staff_db.get(id_s)
        if s:
            print(f"- ID: {id_s} | Nome: {s['nome']} | Função: {s['funcao']}")


def atualizar_funcao_staff(id_s, nova_funcao):
    if id_s in staff_db:
        staff_db[id_s]["funcao"] = nova_funcao
        print(f"Função do staff {id_s} atualizada para: {nova_funcao}")
    else:
        print("Staff não encontrado.")


def remover_staff(id_s):
    if id_s in staff_db:
        nome = staff_db[id_s]["nome"]
        del staff_db[id_s]
        # Remove o funcionário de qualquer concerto onde estivesse alocado
        for c_id in concertos_db:
            if id_s in concertos_db[c_id]["ids_staff"]:
                concertos_db[c_id]["ids_staff"].remove(id_s)
        print(f"Staff '{nome}' removido do sistema e de todos os turnos.")
    else:
        print("Staff não encontrado.")


# --- CRUD CONCERTO ---

def criar_concerto(id_c, id_artista, data, local):
    if id_artista not in artistas_db:
        print("Erro: Artista não existe na base de dados.")
        return
    concertos_db[id_c] = {
        "id_artista": id_artista,
        "ids_staff": [],
        "data": data,
        "local": local,
        "estado": "Agendado",
        "bilhetes_vendidos": 0
    }
    print(f"Concerto {id_c} agendado com sucesso.")


def listar_agenda():
    print("\n--- AGENDA DE CONCERTOS ---")
    for id_c, info in concertos_db.items():
        artista = artistas_db[info['id_artista']]['nome']
        print(
            f"ID: {id_c} | Artista: {artista} | Data: {info['data']} | Local: {info['local']} | Estado: {info['estado']}")


# --- EXECUÇÃO DE EXEMPLO ---
if __name__ == "__main__":
    listar_agenda()

    # Adicionar novo staff e alocar ao concerto 100
    criar_staff(3, "111222333", "João Barman", "Barman", "933222111")
    concertos_db[100]["ids_staff"].append(3)

    # Ver equipa atualizada
    listar_staff_concerto(100)

    # Atualizar função
    atualizar_funcao_staff(1, "Chefe de Som")

    # Remover staff e verificar limpeza
    remover_staff(2)
    listar_staff_concerto(100)

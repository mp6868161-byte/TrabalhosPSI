from artista import criar_artista, ler_artistas, atualizar_artista, eliminar_artista
from bilhetes import criar_bilhete, listar_bilhetes
from src.bilhetes import consultar_bilhete, eliminar_bilhete
from staff import criar_staff, listar_staff, atualizar_staff, remover_staff
from concerto import criar_concerto, listar_concertos, atualizar_concerto, eliminar_concerto

import utils


# --- ÁREA DE ARTISTAS ---
def menu_artistas():
    print("\n[1] Adicionar  [2] Listar  [3] Atualizar  [4] Eliminar  [0] Voltar")
    sub = input("Ação: ")

    if sub == "1":
        nome = input("Nome da Banda/Artista: ")
        genero = input("Género Musical: ")
        code, obj = criar_artista(nome, genero)
        if code == 201:
            print(f"Sucesso: Artista {obj['id']} adicionado!")
        else:
            print(f"Erro {code}: {obj}")

    elif sub == "2":
        code, obj = ler_artistas()
        if code == 200:
            print("\n--- LISTA DE ARTISTAS ---")
            for id_a, dados in obj.items():
                print(f"ID: {id_a} | Nome: {dados['nome']} | Género: {dados['genero']}")
        else:
            print(f"Aviso: {obj}")

    elif sub == "3":
        code = atualizar_artista()
        if code == 200:
            print("Artista atualizado com sucesso!")
        elif code == 404:
            print("Artista não encontrado.")

    elif sub == "4":
        code = eliminar_artista()
        if code == 200:
            print("Artista removido com sucesso!")
        elif code == 404:
            print("Artista não encontrado.")


# --- ÁREA DE BILHETES ---
def menu_bilheteira():
    print("\n[1] Emitir  [2] Listar  [3] Consultar  [4] Eliminar  [0] Voltar")
    sub = input("Ação: ")

    if sub == "1":
        id_c = input("ID do Concerto: ")
        preco = input("Preço: ")
        tipo = input("Tipo (VIP/Normal): ")
        lugar = input("Lugar: ")
        fila = input("Fila: ")
        code, obj = criar_bilhete(preco, tipo, lugar, fila, id_c)
        if code == 201:
            print(f"Sucesso: Bilhete {obj['id']} emitido!")
        else:
            print(f"Erro: {obj}")

    elif sub == "2":
        code, obj = listar_bilhetes()
        if code == 200:
            for b in obj.values():
                print(f"ID: {b['id']} | Concerto: {b['id_concerto']} | Tipo: {b['tipo']}")
        else:
            print(f"Aviso: {obj}")

    elif sub == "3":
        id_bilhete = input("ID do bilhete a consultar: ")
        code, obj = consultar_bilhete(id_bilhete)
        if code == 200:
            print(f"ID: {obj['id']} | Concerto: {obj['id_concerto']} | Tipo: {obj['tipo']}")
        else:
            print(f"Aviso: {obj}")

    elif sub == "4":
        id_bilhete = input("ID do bilhete a eliminar: ")
        code, obj = eliminar_bilhete(id_bilhete)
        if code == 200:
            print(f"ID: {obj} removido com sucesso")
        else:
            print(f"Aviso: {obj}")


# --- ÁREA DE STAFF ---
def menu_equipa_staff():
    print("\n[1] Registar  [2] Listar  [3] Atualizar  [4] Remover  [0] Voltar")
    sub = input("Ação: ")

    if sub == "1":
        nif = input("NIF: ")
        nome = input("Nome: ")
        funcao = input("Função: ")
        telemovel = input("Telemóvel: ")
        code, obj = criar_staff(nif, nome, funcao, telemovel)
        if code == 201:
            print(f"Sucesso: Funcionário {obj['id']} registado!")
        elif code == 409:
            print(f"Erro: {obj}")
        else:
            print(f"Erro {code}: {obj}")

    elif sub == "2":
        code, obj = listar_staff()
        if code == 200:
            for s in obj.values():
                print(f"ID: {s['id']} | Nome: {s['nome']} | Função: {s['funcao']}")
        else:
            print(f"Aviso: {obj}")

    elif sub == "3":
        id_staff = input("ID do funcionário a atualizar: ")
        nif = input("Novo NIF (Enter para manter): ") or None
        nome = input("Novo nome (Enter para manter): ") or None
        funcao = input("Nova função (Enter para manter): ") or None
        telemovel = input("Novo telemóvel (Enter para manter): ") or None
        code, obj = atualizar_staff(id_staff, nif, nome, funcao, telemovel)
        if code == 200:
            print(f"Sucesso: Funcionário {obj['id']} atualizado!")
        elif code == 409:
            print(f"Erro: {obj}")
        else:
            print(f"Erro {code}: {obj}")

    elif sub == "4":
        id_staff = input("ID do funcionário a remover: ")
        code, obj = remover_staff(id_staff)
        if code == 200:
            print(f"Funcionário {obj['id']} removido com sucesso")
        else:
            print(f"Aviso: {obj}")


# --- ÁREA DE CONCERTOS ---
def menu_agenda_concertos():
    print("\n[1] Marcar  [2] Ver Agenda  [3] Atualizar  [4] Cancelar  [0] Voltar")
    sub = input("Ação: ")

    if sub == "1":
        id_art = input("ID do Artista: ")
        nome = input("Nome do artista: ")
        data = input("Data e Hora: ")
        local = input("Local: ")
        code, obj = criar_concerto(nome, data, local, id_art)
        if code == 201:
            print(f"Sucesso: Concerto {obj['id']} agendado!")
        else:
            print(f"Erro: {obj}")

    elif sub == "2":
        code, obj = listar_concertos()
        if code == 200:
            print("\n--- AGENDA DE CONCERTOS ---")
            for c in obj.values():
                print(f"ID: {c['id']} | Artista: {c['id_artista']} | Data: {c['data']} | Local: {c['local']}")
        else:
            print(f"Aviso: {obj}")

    elif sub == "3":
        id_concerto = input("ID do concerto a atualizar: ")
        nome = input("Novo nome do artista (Enter para manter): ") or None
        data = input("Nova data e hora (Enter para manter): ") or None
        local = input("Novo local (Enter para manter): ") or None
        code, obj = atualizar_concerto(id_concerto, nome, data, local)
        if code == 200:
            print(f"Sucesso: Concerto {obj['id']} atualizado!")
        else:
            print(f"Erro: {obj}")

    elif sub == "4":
        id_concerto = input("ID do concerto a cancelar: ")
        code, obj = eliminar_concerto(id_concerto)
        if code == 200:
            print(f"Concerto {obj} cancelado com sucesso")
        else:
            print(f"Aviso: {obj}")


# --- LOOP PRINCIPAL ---
def main():
    while True:
        print("\n" + "=" * 30)
        print("   GESTOR DE CONCERTOS  ")
        print("=" * 30)
        print("1. Gerir Artistas")
        print("2. Gerir Bilheteira")
        print("3. Gerir Staff")
        print("4. Gerir Concertos")
        print("0. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            menu_artistas()
        elif opcao == "2":
            menu_bilheteira()
        elif opcao == "3":
            menu_equipa_staff()
        elif opcao == "4":
            menu_agenda_concertos()
        elif opcao == "0":
            print("A encerrar sistema... Adeus!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

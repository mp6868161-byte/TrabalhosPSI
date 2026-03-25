from artista import (
    criar_artista,
    listar_artistas,
    consultar_artista,
    atualizar_artista,
    remover_artista
)

def menu():
    print("\n===== GESTÃO DE ARTISTAS =====")
    print("1 - Criar artista")
    print("2 - Listar artistas")
    print("3 - Consultar artista")
    print("4 - Atualizar artista")
    print("5 - Remover artista")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            genero = input("Género Musical: ")
            bancada = input("Bancada: ")
            setor = input("Setor: ")
            nif = input("NIF: ")
            nacionalidade = input("Nacionalidade: ")
            tipo = input("Tipo (Banda/Solo): ")
            
            criar_artista(nome, genero, bancada, setor, nif, nacionalidade, tipo)

        elif opcao == "2":
            listar_artistas()

        elif opcao == "3":
            id_art = input("ID do artista (ex: A001): ")
            consultar_artista(id_art)

        elif opcao == "4":
            id_art = input("ID do artista a atualizar: ")
            print("(Deixe em branco para manter o valor atual)")
            
            nome = input("Novo nome: ")
            genero = input("Novo género: ")
            bancada = input("Nova bancada: ")
            setor = input("Novo setor: ")
            nif = input("Novo NIF: ")
            nacionalidade = input("Nova nacionalidade: ")
            tipo = input("Novo tipo: ")

            atualizar_artista(
                id_art,
                nome=nome if nome else None,
                genero=genero if genero else None,
                bancada=bancada if bancada else None,
                setor=setor if setor else None,
                nif=nif if nif else None,
                nacionalidade=nacionalidade if nacionalidade else None,
                tipo=tipo if tipo else None
            )

        elif opcao == "5":
            id_art = input("ID do artista a remover: ")
            remover_artista(id_art)

        elif opcao == "0":
            print("A encerrar sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

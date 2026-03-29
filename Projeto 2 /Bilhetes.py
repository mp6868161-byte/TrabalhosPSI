bilheteira = {}


def criar_bilhete(id_bilhete, preco, tipo, lugar, fila, id_concerto):
    if id_bilhete in bilheteira:
        print(f"Erro: O ID {id_bilhete} já existe no sistema.")
        return

    # Adiciona os dados ao dicionário principal
    bilheteira[id_bilhete] = {
        "preco": preco,
        "tipo": tipo,  # Ex: VIP, Plateia, Balcão
        "lugar": lugar,
        "fila": fila,
        "id_concerto": id_concerto
    }
    print(f"Sucesso: Bilhete {id_bilhete} registado com êxito!")


def listar_bilhetes():
    if not bilheteira:
        print("\nA bilheteira está vazia.")
        return

    print("\n--- LISTA DE BILHETES ---")
    for id_b, info in bilheteira.items():
        print(f"ID: {id_b} | Concerto: {info['id_concerto']}")
        print(f"   Tipo: {info['tipo']} | Fila: {info['fila']} | Lugar: {info['lugar']}")
        print(f"   Preço: {info['preco']}€")
        print("-" * 25)


def atualizar_bilhete(id_bilhete):
    if id_bilhete in bilheteira:
        print(f"A atualizar o bilhete {id_bilhete}. Deixe em branco para manter o valor atual.")

        # Exemplo de atualização dinâmica
        novo_preco = input("Novo preço: ")
        if novo_preco:
            bilheteira[id_bilhete]["preco"] = float(novo_preco)

        novo_tipo = input("Novo tipo: ")
        if novo_tipo:
            bilheteira[id_bilhete]["tipo"] = novo_tipo

        print("Bilhete atualizado com sucesso!")
    else:
        print("Erro: Bilhete não encontrado.")


def eliminar_bilhete(id_bilhete):
    if id_bilhete in bilheteira:
        del bilheteira[id_bilhete]
        print(f"O bilhete {id_bilhete} foi eliminado.")
    else:
        print("Erro: ID inexistente.")


# --- Teste do Sistema ---

# 1. CRIAR (Create)
criar_bilhete(1, 45.50, "Plateia A", "12", "F", "CONCERTO_Bon-jovi_2026")
criar_bilhete(2, 120.00, "VIP Premium", "01", "A", "concerto_AC/DC_2026")

# 2. LER (Read)
listar_bilhetes()

# 3. ATUALIZAR (Update)
# Vamos atualizar o preço do bilhete 1
bilheteira[1]["preco"] = 50.00
print("\nPreço do bilhete 1 atualizado manualmente.")

# 4. ELIMINAR (Delete)
eliminar_bilhete(2)

# Resultado Final
listar_bilhetes()

bilheteira = {}

def criar_bilhete(id_bilhete, preco, tipo, lugar, fila, id_concerto):
    if id_bilhete in bilheteira:
        print(f"Erro: O ID {id_bilhete} já existe no sistema.")
        return

    bilheteira[id_bilhete] = {
        "preco": preco,
        "tipo": tipo,
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
    # Verifica primeiro se existe. Se não existir, sai logo.
    if id_bilhete not in bilheteira:
        print("Erro: Bilhete não encontrado.")
        return

    print(f"A atualizar o bilhete {id_bilhete}. Deixe em branco para manter o valor atual.")

    # Atualização dinâmica com input do utilizador
    novo_preco = input(f"Novo preço (Atual: {bilheteira[id_bilhete]['preco']}€): ")
    if novo_preco:
        bilheteira[id_bilhete]["preco"] = float(novo_preco)

    novo_tipo = input(f"Novo tipo (Atual: {bilheteira[id_bilhete]['tipo']}): ")
    if novo_tipo:
        bilheteira[id_bilhete]["tipo"] = novo_tipo

    print("Bilhete atualizado com sucesso!")


def eliminar_bilhete(id_bilhete):
    if id_bilhete in bilheteira:
        del bilheteira[id_bilhete]
        print(f"O bilhete {id_bilhete} foi eliminado.")
    else:
        print("Erro: ID inexistente.")


# --- Teste do Sistema ---

# 1. CRIAR
criar_bilhete(1, 45.50, "Plateia A", "12", "F", "CONCERTO_Bon-jovi_2026")
criar_bilhete(2, 120.00, "VIP Premium", "01", "A", "CONCERTO_ACDC_2026")

# 2. LER
listar_bilhetes()

# 3. ATUALIZAR (Usando a função interativa)
atualizar_bilhete(1)

# 4. ELIMINAR
eliminar_bilhete(2)

# Resultado Final
listar_bilhetes()

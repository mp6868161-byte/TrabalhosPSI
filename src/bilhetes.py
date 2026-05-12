import json
import os

FICHEIRO_DADOS = "bilheteira.json"

def carregar_dados():
    """Carrega bilheteira do ficheiro JSON."""
    if os.path.exists(FICHEIRO_DADOS):
        with open(FICHEIRO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            # As chaves do JSON são sempre strings; converte para int
            return {int(k): v for k, v in dados.items()}
    return {}

def guardar_dados(bilheteira):
    """Guarda bilheteira no ficheiro JSON."""
    with open(FICHEIRO_DADOS, "w", encoding="utf-8") as f:
        json.dump(bilheteira, f, ensure_ascii=False, indent=4)

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
    guardar_dados(bilheteira)
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
    if id_bilhete not in bilheteira:
        print("Erro: Bilhete não encontrado.")
        return
    print(f"A atualizar o bilhete {id_bilhete}. Deixe em branco para manter o valor atual.")
    novo_preco = input(f"Novo preço (Atual: {bilheteira[id_bilhete]['preco']}€): ")
    if novo_preco:
        bilheteira[id_bilhete]["preco"] = float(novo_preco)
    novo_tipo = input(f"Novo tipo (Atual: {bilheteira[id_bilhete]['tipo']}): ")
    if novo_tipo:
        bilheteira[id_bilhete]["tipo"] = novo_tipo
    guardar_dados(bilheteira)
    print("Bilhete atualizado com sucesso!")

def eliminar_bilhete(id_bilhete):
    if id_bilhete in bilheteira:
        del bilheteira[id_bilhete]
        guardar_dados(bilheteira)
        print(f"O bilhete {id_bilhete} foi eliminado.")
    else:
        print("Erro: ID inexistente.")

# --- Carrega dados persistidos (ou começa do zero) ---
bilheteira = carregar_dados()

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

# ==============================
# bilhete.py
# CRUD simples para entidade Bilhete
# SEM utilização de classes
# armazenamento em dicionario
# ==============================

from utils import gerar_id_bilhete # Note: deve criar esta função no utils.py

bilhetes = {}

# CREATE
def criar_bilhete(id_concerto, preco, tipo, lugar, fila):
    # Validação simples de preço (exemplo pedagógico)
    try:
        preco_float = float(preco)
        if preco_float <= 0:
            print("Erro: O preço deve ser superior a 0.")
            return
    except ValueError:
        print("Erro: Preço inválido.")
        return

    id_bilhete = gerar_id_bilhete()

    bilhetes[id_bilhete] = {
        "id_concerto": id_concerto,
        "preco": preco_float,
        "tipo": tipo, # Ex: VIP, Plateia, Bancada
        "lugar": lugar,
        "fila": fila
    }

    print(f"Bilhete emitido com sucesso! ID: {id_bilhete}")


# READ (listar todos)
def listar_bilhetes():
    if not bilhetes:
        print("Não existem bilhetes emitidos.")
        return

    print("\n--- LISTAGEM DE BILHETES ---")
    for id_b, dados in bilhetes.items():
        print(f"ID: {id_b} | Concerto: {dados['id_concerto']} | Tipo: {dados['tipo']} | "
              f"Fila: {dados['fila']} | Lugar: {dados['lugar']} | Preço: {dados['preco']}€")


# READ (consultar individual)
def consultar_bilhete(id_bilhete):
    if id_bilhete not in bilhetes:
        print("Bilhete não encontrado.")
        return

    b = bilhetes[id_bilhete]
    print(f"\nDetalhes do Bilhete {id_bilhete}:")
    print(f"ID Concerto: {b['id_concerto']}")
    print(f"Preço: {b['preco']}€")
    print(f"Tipo: {b['tipo']}")
    print(f"Localização: Fila {b['fila']}, Lugar {b['lugar']}")


# UPDATE
def atualizar_bilhete(id_bilhete, id_concerto=None, preco=None, tipo=None, lugar=None, fila=None):
    if id_bilhete not in bilhetes:
        print("Bilhete não encontrado.")
        return

    # Atualização seletiva
    if id_concerto:
        bilhetes[id_bilhete]["id_concerto"] = id_concerto
    
    if preco:
        try:
            bilhetes[id_bilhete]["preco"] = float(preco)
        except ValueError:
            print("Preço inválido, não atualizado.")

    if tipo:
        bilhetes[id_bilhete]["tipo"] = tipo

    if lugar:
        bilhetes[id_bilhete]["lugar"] = lugar

    if fila:
        bilhetes[id_bilhete]["fila"] = fila

    print(f"Bilhete {id_bilhete} atualizado com sucesso.")


# DELETE
def remover_bilhete(id_bilhete):
    if id_bilhete not in bilhetes:
        print("Bilhete não encontrado.")
        return

    del bilhetes[id_bilhete]
    print(f"Bilhete {id_bilhete} anulado/removido.")

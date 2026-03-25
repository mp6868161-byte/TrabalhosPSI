# ==============================
# utils.py
# Funções auxiliares e validações
# ==============================

from datetime import datetime

# Contador global para gerar IDs automáticos (B001, B002, etc.)
contador_ids = 1

def gerar_id_bilhete():
    """
    Gera um ID único com o prefixo 'B' seguido de 3 dígitos.
    Exemplo: B001, B002...
    """
    global contador_ids
    # :03d garante que o número tenha sempre 3 casas decimais (preenche com zeros)
    novo_id = f"B{contador_ids:03d}"
    contador_ids += 1
    return novo_id

def validar_preco(valor):
    """
    Tenta converter a entrada para float e verifica se é um preço positivo.
    Retorna True se for válido, False caso contrário.
    """
    try:
        preco = float(valor)
        if preco > 0:
            return True
        return False
    except ValueError:
        return False

def validar_data(data_texto):
    """
    Verifica se uma data está no formato correto (YYYY-MM-DD).
    Utilizado caso queiras adicionar data de emissão ou do concerto.
    """
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False

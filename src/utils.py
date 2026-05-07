import datetime
import os

# --- UTILITÁRIOS DE SISTEMA ---

def limpar_terminal():
    """Limpa o ecrã do terminal conforme o Sistema Operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho(titulo):
    """Cria um cabeçalho visual para os menus."""
    print(f"\n{'-' * 30}")
    print(f"{titulo.upper().center(30)}")
    print(f"{'-' * 30}")


# --- VALIDAÇÕES ---

def validar_data(data_texto):
    """Verifica se a data está no formato AAAA-MM-DD e se é válida."""
    try:
        datetime.datetime.strptime(data_texto, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validar_nif(nif):
    """Verifica se o NIF tem exatamente 9 dígitos numéricos."""
    return nif.isdigit() and len(nif) == 9


def validar_telemovel(numero):
    """Verifica se o telemóvel tem 9 dígitos."""
    return numero.isdigit() and len(numero) == 9


# --- GERAÇÃO DE IDS ---

def gerar_id(prefixo, base_dados):
    """
    Gera um ID automático baseado no prefixo e no tamanho da base de dados.
    Ex: gerar_id("S", db_staff) -> "S001"
    """
    proximo_numero = len(base_dados) + 1
    return f"{prefixo}{proximo_numero:03d}"


# --- TRATAMENTO DE INPUTS ---

def ler_obrigatorio(mensagem):
    """Garante que o utilizador não deixa o campo vazio."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Erro: Este campo é obrigatório!")


# --- CÓDIGOS DE STATUS / FEEDBACK ---

def feedback(codigo):
    """Mapeia os códigos de status para mensagens de texto simples."""
    mensagens = {
        200: "Sucesso: Operação realizada.",
        201: "Sucesso: Registo criado.",
        400: "Erro: Dados inválidos (verifique NIF, data ou telemóvel).",
        404: "Erro: Registo não encontrado.",
        409: "Erro: ID já existente no sistema."
    }
    print(mensagens.get(codigo, f"Status {codigo}"))

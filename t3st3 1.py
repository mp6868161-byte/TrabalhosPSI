

# ==============================
# GERADOR DE SIGLAS AVANÇADO
# ==============================

# Mostrar o título do programa
print("=== GERADOR DE SIGLAS ===")

# Ciclo para garantir que o utilizador escreve uma frase válida (não vazia)
while True:
    frase = input("Escreve uma frase: ").strip()  # strip() remove espaços no início e no fim

    # Se a frase não estiver vazia, sai do ciclo
    if frase != "":
        break
    else:
        print("A frase não pode estar vazia.")

# Lista de palavras comuns que vão ser ignoradas na sigla
ignorar = ["de", "da", "do", "das", "dos", "e", "a", "o", "as", "os", "em", "para"]

# Perguntar ao utilizador que tipo de sigla quer
print("\nQue tipo de sigla queres?")
print("1 - Normal (primeira letra de cada palavra)")
print("2 - Só letras (ignora números e símbolos)")

# Ler a opção escolhida
opcao = input("Escolha: ")

# Separar a frase em palavras usando os espaços
palavras = frase.split()

# Variável onde será construída a sigla final
sigla = ""

# Lista para guardar as palavras que realmente foram usadas
usadas = []

# Percorrer todas as palavras da frase
for palavra in palavras:

    # Se a palavra estiver na lista de palavras a ignorar, passa para a próxima
    if palavra.lower() in ignorar:
        continue

    # Se o utilizador escolheu o modo "só letras"
    if opcao == "2":
        letra = ""  # Vai guardar a primeira letra válida da palavra

        # Percorrer cada carácter da palavra
        for c in palavra:
            # Se for uma letra do alfabeto
            if c.isalpha():
                letra = c
                break  # Para no primeiro carácter válido encontrado

        # Se não foi encontrada nenhuma letra, ignora a palavra
        if letra == "":
            continue
    else:
        # Modo normal: usa simplesmente o primeiro carácter da palavra
        letra = palavra[0]

    # Adiciona a letra (em maiúscula) à sigla
    sigla += letra.upper()

    # Guarda a palavra usada na lista
    usadas.append(palavra)

# Mostrar os resultados
print("\n RESULTADO")
print("Frase original:", frase)
print("Palavras utilizadas:", usadas)
print("Total de palavras na frase:", len(palavras))
print("Palavras usadas na sigla:", len(usadas))
print("Sigla gerada:", sigla)

# Mostrar o processo passo a passo
print("\n=== PROCESSO ===")
for p in usadas:
    print("Palavra:", p, "-> letra usada:", p[0].upper())

# Mensagem final
print("\nPrograma terminado.")




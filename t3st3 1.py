# ==============================
# GERADOR DE SIGLAS AVANÇADO
# ==============================

print("=== GERADOR DE SIGLAS ===")

while True:
    frase = input("Escreve uma frase: ").strip()

    if frase != "":
        break
    else:
        print("A frase não pode estar vazia.")

# Lista de palavras a ignorar
ignorar = ["de", "da", "do", "das", "dos", "e", "a", "o", "as", "os", "em", "para"]

# Perguntar tipo de sigla
print("\nQue tipo de sigla queres?")
print("1 - Normal (primeira letra de cada palavra)")
print("2 - Só letras (ignora números e símbolos)")

opcao = input("Escolha: ")

palavras = frase.split()
sigla = ""
usadas = []

for palavra in palavras:

    # Ignorar palavras pequenas comuns
    if palavra.lower() in ignorar:
        continue

    # Modo só letras
    if opcao == "2":
        letra = ""
        for c in palavra:
            if c.isalpha():
                letra = c
                break
        if letra == "":
            continue
    else:
        letra = palavra[0]

    sigla += letra.upper()
    usadas.append(palavra)

# Mostrar resultados
print("\n RESULTADO")
print("Frase original:", frase)
print("Palavras utilisadas:", usadas)
print("Total de palavras na frase:", len(palavras))
print("Palavras usadas na sigla:", len(usadas))
print("Sigla gerada:", sigla)

# Extra: mostrar passo a passo
print("\n=== PROCESSO ==")
for p in usadas:
    print("Palavra:", p, "-> letra usada:", p[0].upper())

print("\nPrograma terminado.")


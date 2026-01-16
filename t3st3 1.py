frase = input("Escreve uma frase: ")

palavras = frase.split()

sigla = ""

for palavra in palavras:

    sigla += palavra[0]

sigla = sigla.upper()

print("Sigla gerada:", sigla)

notas = []

while True:
    try:
        quantidade = int(input("Quantas notas queres inserir? "))
        if quantidade > 0:
            break
        else:
            print("Tem de ser um número maior que 0.")
    except ValueError:
        print("Por favor, escreve um número válido.")

for i in range(quantidade):
    while True:
        try:
            nota = float(input(f"Insere a nota {i+1}: "))
            if 0 <= nota <= 20:
                notas.append(nota)
                break
            else:
                print("A nota deve estar entre 0 e 20.")
        except ValueError:
            print("Escreve um número válido.")

print("\nNotas inseridas:")
for i, n in enumerate(notas, start=1):
    print(f"{i}. {n}")

maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

print("\n--- Estatísticas ---")
print("Nota mais alta:", maior)
print("Nota mais baixa:", menor)
print("Média das notas:", round(media, 2))

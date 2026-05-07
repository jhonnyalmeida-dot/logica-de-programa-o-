
#1:crie um programa que o usuario possa digitar quantos numeros quiser e ao terminar implima a lista em ordem crecente
quantidade = int(input("Digite a quantidade de números: "))

numeros = []

for i in range(quantidade):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

numeros.sort()

print("\nLista em ordem crescente:")
print(numeros)



#2:crie um programa que a usuaria possa digitar a quantidade desejadada de notas em um determinado aluno(nota minima 0 maxima 10) e ao terminar imprima a media do aluno e se ele foi aprovado ou reprovado (media minima 6)
nome = input("Digite o nome do aluno: ")
turma = input("Digite a turma: ")

quantidade = int(input("Digite a quantidade de notas: "))

notas = []

for i in range(quantidade):
    while True:
        nota = float(input(f"Digite a nota {i+1} (0 a 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")

media = sum(notas) / len(notas)

print("\n===== BOLETIM ESCOLAR =====")
print("Nome:", nome)
print("Turma:", turma)

print("\nNotas:")
for i, nota in enumerate(notas, 1):
    print(f"Nota {i}: {nota:.1f}")

print(f"\nMédia final: {media:.2f}")

if media >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")
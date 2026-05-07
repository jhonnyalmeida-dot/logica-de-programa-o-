"""
cauculos e manipulação de variaveis
"""
nome = input("digite seu nome: ")
idade = input("digite a sua idade: ")
peso =input ("digite seu peso: ")
altura =input ("digite sua altura: ")

#tratamento de execeção
try:
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
except ValueError as e:
    print(e)

imc = peso/ altura * 2

print("seu imc é: ", imc)
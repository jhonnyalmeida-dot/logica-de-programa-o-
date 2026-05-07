# NOTE: boletim escolar
# import uma lib 
import os 

os.system("cls")

nome = input("digite o nome do aluno: ").title()
turma = input("digite a turma do aluno: ").upper()
nota1 = input("digite a primeira nota do aluno: ").replace(",",".")
nota2 = input("digite a segunda nota do aluno: ").replace(",",".")
nota3  = input("digite a terceira nota do aluno: ").replace(",",".")
nota4 = input("digite a quarta nota do aluno: ").replace(",",".")
nota5 = input("digite a  quinta nota do aluno: ").replace(",",".")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
nota5 = float(nota5)

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
resultado = None
if media >=70: 
    resultado = ("aprovado")
elif media >=50:
    resultado = ("recuperação")

elif media:
    resultado = ("reprovado") 




os.system("cls")
print(30*"-","boletim escolar", 30*"-")
print("nome do aluno:" , nome," | turma: ",turma)
print("nota1:", nota1)
print("nota2:", nota2)
print("nota3:", nota3)
print("nota4:", nota4)
print("nota5:", nota5)
print(70*"=")
print(f"media: , ({media:.2f})")
print("situação", resultado)
'''
manipulação de arquivos: percorrer meus diretorios, encontrar o arquivo para  o comandso de abertura do arquivo, passar comando de açao.

dados de ação:

- "r" : leitura do arquivo 
- "w" : escrita(sobrescrever o conteudo antigo)
- "a" : adicionar conteudo
- "x" : criar aequivo 
- "t" : texto

'''
arquivo = open('primeiro_arquivo_txt', 'w')
arquivo.write('ola mundo! meu priimeiro arquivo')
arquivo.close() 
# lendo o arquivo

arquivo = open("primeiro_arquivo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# aplicando boa pratica ]
with open("primeiro_asrquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
    # arquivo com multiplas escritas 
    with open('alunos.txt', "a") as arquivo: 
      
      
      
     # lendo linha a linha 
      with open ('aluno.txt', "r") as arquivo:

        for linha in arquivo:
         print(linha)
        
         frutas = ['caju','melao','melancia','limao']

         with open('frutas.txt', "w") as arquivo: 
           for f in frutas: 
             arquivo.write(f + "\n")


# exemplo para cadastro 
while True: 
  nome = input("digite seu nome: ").title()
  with open("cadastro .txt", 'a') as arquivo:
   arquivo.write(nome + "\n")
  sair = input("desejaq sair? s/n").lower()

  if sair =='s':
   break

'''

    Sistema de Veiculos em Json

'''

import os
import time
import json

ARQUIVO = 'carros.json'

# carrega arquivo

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        carros = json.load(arquivo)
else:
    carros = []

# descobrir o ID
if carros:
    proximo_id = max(carro['id'] for carro in carros) + 1
else:
    proximo_id = 1

os.system('cls')

while True:
        print("\n==== Sistema de Carros =====")
        print ('1 - Cadastrar carro')
        print ('2 - Listar carro')
        print ('3 - Atualizar carro')
        print ('4 - Deletar carro')
        print ('0 - Sair')

        opcao = input ('Escolha uma opção: ')

        #register
        if opcao == '1':
            modelo = input("Digite o modelo do carro: ").title()
            preco = float(input('Digite o preço: '))
            marca = input("Digite a marca: ").title()

            carro = {
                "id"    :proximo_id,
                "modelo"    :modelo,
                "preco"     :preco,
                "marca"     :marca
            }

            carros.append(carro)

            with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
                json.dump(carros, arquivo, indent=4, ensure_ascii=False)

            proximo_id += 1

            print ("Carro cadastrado com sucesso.")

        elif opcao == '2':
            os.system('cls')

            if not carros:
                print ("Nenhum carro cadastrado.")
            else:
                print('\n Lista de veiculos: ')
                for carro in carros:
                    print(f'ID: {carro["id"]} | Modelo: {carro["modelo"]} | preço {carro["preco"]} | marca: {carro["marca"]}')

        elif opcao == '3':
            os.system('cls')

            if not carros:
                print ("Nenhum carro cadastrado.")
                continue

            for carro in carros:
                print('\n Lista de veiculos: ')
                for carro in carros:
                    print(f'ID: {carro["id"]} | Modelo: {carro["modelo"]} | preço {carro["preco"]} | marca: {carro["marca"]}')

            id_busca = int(input('Digite o ID do carro para atualizar: '))

            encontrado = False

            for carro in carros:
                if carro ['id'] == id_busca:
                    carro ['modelo'] = input("Novo modelo: ").title()
                    carro ['preco'] = float(input("Novo preco: ")).replace(',', '.')
                    carro ['marca'] = input("Nova marca: ").title()

                    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
                        json.dump(carros, arquivo, indent=4, ensure_ascii=False)

                    print ("Carro atualizado com sucesso.")
                    encontrado = True
                    break

            if not encontrado:
                print ("Carro não encontrado.")

        elif opcao == '4':
            print ("Lista de carros: ")
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | preco {carro['preco']} | marca: {carro['marca']}')
            id_busca = int(input("Digite o ID do carro para poder deletar: "))

            encontrado = False

            for carro in carros:
                if carro['id'] == id_busca:
                    carros.remove(carro)
                    print("Carro deletado com sucesso.")
                    encontrado = True
                break

            if not encontrado:
                print ("Carro não encontrado.")

        elif opcao == '0':
            print ("Saindo do sistema...")
            time.sleep(2)
            break
        else:
            print ("Opção invalida.")
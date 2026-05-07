import os
import time

carros = []
proximo_id = 1

os.system("cls")
while True:
    print("\n======Sistema de Carros======")
    print('1 - Cadastrar carros')
    print('2 - Listar carros')
    print('3 - Atualizar carros')
    print('4 - Deletar carros')
    print('0 - sair')

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        modelo = input ("digite a marca do carro: ").title()
        preco = float(input("Digite o preço: "))
        marca = input("Digite a marca: ").title()

        carro = {
            "id"     : proximo_id,
            "modelo" : modelo,
            "preco"  : preco,
            "marca"  : marca,
        }
        carros.append(carros)
        proximo_id +=1

        print("Carro cadastrado com sucesso!")

    elif opcao == "2":
        if not carros:
            print("Carro não cadastrado")
        else:
            print("lista de carros")
            for carro in carros:
                print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']}')

    elif opcao == '3':
        print("\n lista de carros")
        print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']}')
        id_busca = int(input("Digite o id do carro para deletar"))

        encontrado = False
        for carro in carros:
            if carro['id'] == id_busca:
                novo_modelo = input("Digite o novo  modelo: ").title()
                novo_preco = input("Digite o novo preço: ").replace(',','.')
                nova_marca = input("Digite o novo preço: ").title()

                carro['modelo'] = novo_modelo
                carro['preco'] = novo_preco
                carro['marca'] = nova_marca

                print("Carro atualizado com sucesso")
                encontrado = True
                break
        if not encontrado:
            print('Carro não encontrado')

    elif opcao == '4':
        print("\n lista de carros")
        print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']}')
        id_busca = int(input("Digite o id do carro para deletar"))

        encontrado = False

        for carro in carros:
            if carro['id'] == id_busca:
                carros.remove(carro)
                print("Carro deletado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Carro não encontrado!")

    elif opcao == '0':
        total = 20
        barra = ""
        print("saindo do sistema...")
        for i in range(1,total +1):
            barra +="°"
            porcentagem = int((i/total) *100)
            vazio ="-" * (total -1)
            print(f'\r[{barra}] {porcentagem}%', end="")
        time.sleep(0.2)
        break 
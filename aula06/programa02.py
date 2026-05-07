carros = []
proximo_id = 1
while True:
    print("============ MENU ===========")
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. editar carro")
    print("4. Excluir carro")
    print("0. Sair")
    input_usuario = int(input("Digite a opção desejada: "))
   
    opcao = int(input("Digite a opção desejada: "))
    #CRIAR
    if input_usuario == "1":
        marca = input("Digite a marca do carro: ").title()
        preço = float(input("Digite o preço do carro: "))
        modelo = input("Digite o modelo do carro: ").title()

        carro = {
            "id": proximo_id,
            "marca": marca,
            "preço": preço,
            "modelo": modelo
        }
        carros.append(carro)
        proximo_id += 1
        print("Carro cadastrado com sucesso!")

    # READ
    elif input_usuario == "2":
        if not carros:
            print("Nenhum carro cadastrado.")
        else:
            print("Carros cadastrados:")
            for carro in carros:
                print(f"ID: {carro['id']}, Marca: {carro['marca']}, Preço: R${carro['preço']:.2f}, Modelo: {carro['modelo']}")
    
    # ATUALIZAR
    elif opcao == '3':
        ...

    # DELETE
    elif opcao == '4':
        print('\n Lista de carros')
        print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')
    
    # SAIR
    elif input_usuario == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opcção Invalida ")
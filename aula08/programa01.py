import modulo as ma

if __name__=="__main__": 
 
 import modulo as ma

def main():
    while True:
        print("calculadora")
        print("1, somar")
        print("2, subtrair")
        print("3, multiplicar")
        print("4, dividir")
        print("5, limpar terminal")

        opcao = input('digite a opçao desejada ')
        match opcao:
            case '1':
                print ('----soma----')
                num1 = int(input('digite um numero para somar: '))
                num2 = int(input('digite outro numero para somar'))
                result = ma.divisao(num1,num2)
                print(f'resultado: {result}')
                break
            case '2':
                print ('----soma----')
                num1 = int(input('digite um numero para subtrair: '))
                num2 = int(input('digite outro numero para subtrair'))
                result = ma.divisao(num1,num2)
                print(f'resultado: {result}')
                break
            case '3':
                print ('----soma----')
                num1 = int(input('digite um numero para : multiplicar '))
                num2 = int(input('digite outro numero para: multiplicar '))
                result = ma.divisao(num1,num2)
                print(f'resultado: {result}')
                break
            case '4':
                print ('----soma----')
                num1 = int(input('digite um numero para: dividir '))
                num2 = int(input('digite outro numero para: dividir '))
                result = ma.divisao(num1,num2)
                print(f'resultado: {result}')
                break
            case '5':
                ma.limppar_terminal
                break
            case _:
                print('Opção invalida')

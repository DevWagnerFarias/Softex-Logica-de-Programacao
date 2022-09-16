from asyncio import exceptions


def calculadora():
    valor1 = int(input("Digite o primeiro valor"))
    valor2 = int(input("Digite o segundo valor"))

    try:
        divisao = valor1 / valor2
        ("A divisão desses dois números é: ", divisao)

    except ZeroDivisionError:
        print("Não existe divisão por zero, digite um número inteiro diferente de zero nos valores pedidos")
        calculadora()
    except ValueError:
        print("Digite apenas números")
        calculadora()

calculadora()
import sys 

def calculadora(num1, num2, operacao):
  if operacao == 1:
    numfinal = num1 + num2
    return numfinal
    print("Resultado: ", str(numfinal))
  elif operacao == 2:
    numfinal = num1 - num2
    return numfinal
    print("Resultado: ", str(numfinal))
  elif operacao == 3:
    numfinal = num1 * num2
    return numfinal
    print("Resultado: ", str(numfinal))
  elif operacao == 4:
    numfinal = num1 / num2
    return numfinal
    print("Resultado: ", str(numfinal))
  elif operacao == 0:
    print("Volte logo!")
    sys.exit()
  else:
    print("Operação inválida")



a = float(input("DIgite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print("Operações:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("0. Sair")
c = float(input("Qual das operações acima você deseja realizar com os dois números digitados anteiormente? "))

print(calculadora (a, b, c))



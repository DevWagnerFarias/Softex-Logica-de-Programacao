nome = str(input("Qual o seu nome?"))
nome = nome.title()
print("A primeira letra do seu nome é ", nome[0])

sobrenome1 = str(input("Qual o seu primeiro sobrenome?"))
sobrenome1 = sobrenome1.title()
sobrenome2 = str(input("Qual o seu segundo sobrenome?"))
sobrenome2 = sobrenome2.title()

print("Olá ", nome, sobrenome1, sobrenome2)
print("O seu nome possui ", len(nome), "caracteres")
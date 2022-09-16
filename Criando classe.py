class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

nome = str(input("Qual seu nome?"))
sexo = str(input("Qual gênero você se considera?"))
cpf = int(input("Digite o número de seu CPF:"))

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123456")
    print(pessoa1.nome)
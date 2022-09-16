import sys

def idade_atual():

    name = str(input("Qual o seu nome? "))
    yearbirth = int(input("Qual o ano do seu nascimento? "))
    age = 2022 - yearbirth
    
    if yearbirth >= 1922 and yearbirth <= 2021:
        print(str(name) + " tem, ou irá completar, ", str(age), "anos em 2022!")
        sys.exit()
    else:
        print("Digite um ano de nascimento válido, entre 1992 e 2021")

        idade_atual()
        
idade_atual()
    
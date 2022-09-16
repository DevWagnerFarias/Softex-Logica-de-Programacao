from enum import Enum

class candidatos(Enum):
    candidato_x = 889 
    candidato_y = 847
    candidato_z = 515
    branco = 0

def eleicao():

    #variáveis contadoras
    votos_x = 0
    votos_y = 0
    votos_z = 0
    brancos_nulos = 0
    continua = True

    while continua == True:

        print("Candidato X = 889")
        print("Candidato Y = 847")
        print("Candidato Z = 515")
        print("Votar em branco = 0")
        voto = int(input("Digite o número correspondente ao candidato que deseja votar: "))

        try:
            if voto == candidatos.candidato_x.value:
                votos_x += 1
            elif voto == candidatos.candidato_y.value:
                votos_y += 1
            elif voto == candidatos.candidato_z.value:
                votos_z += 1
            else:
                brancos_nulos += 1
        except:                          #Tratando o erro caso o usuário não digite um número
            print("Digite apenas o número do candidato em que deseja votar ou 0 para votar em branco")
            eleicao()                  

        fim = int(input("Digite 0 para finalizar a votação, ou então digite qualquer outra tecla para continuar votando: "))

        if fim == 0:
            continua = False    #Finaliza a votação pois muda a condição True do Loop While
        else:
            continua = True

    

    print("VOTAÇÃO FINALIZADA")
    print("Candidato X: ", votos_x, "votos")            #Mostrando a contagem dos votos
    print("Candidato Y: ", votos_y, "votos")
    print("Candidato Z: ", votos_z, "votos")
    print("Brancos e Nulos: ", brancos_nulos, "votos")

    if votos_x > votos_y and votos_x > votos_z:         #Contabilizando o candidato eleito
        print("O Candidato X ganhou a eleição!")
    elif votos_y > votos_x and votos_y > votos_z:
        print("O Candidato Y ganhou a eleição!")
    elif votos_z > votos_x and votos_z > votos_y:
        print("O Candidato Z ganhou a eleição!")
    elif votos_x > votos_z and votos_x == votos_y:
        print("Os Candidatos X e Y empataram em números de votos e vão para o segundo turno")
    elif votos_x > votos_y and votos_x == votos_z:
        print("Os Candidatos X e Z empataram em números de votos e vão para o segundo turno")
    elif votos_y > votos_x and votos_y == votos_z:
        print("Os Candidatos Y e Z empataram em números de votos e vão para o segundo turno")
    else:
        print("Os Candidatos tiveram o mesmo número de votos e vão decidir no zerinho ou um")


eleicao()
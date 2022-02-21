import random #importando a função random

print ("**********************************************")
print ("**Bem-vindo ao gerador de nomes de digimons**")
print ("**********************************************")

print("Quandos nomes de digimons desejas gerar?")
numero_de_nomes = int(input("Digite o número de nomes de 1 a 50: "))

if (numero_de_nomes < 1 or numero_de_nomes > 50):
    print ("Você não digitou um número válido, o programa será reiniciado")
    exit()

print(f"Eis a lista com o nome de {numero_de_nomes} digimons: ")
for k in range (1, numero_de_nomes + 1):

    ###Função para gerar as letras aleatórias###

    comprimento_do_nome =  random.randrange(1,7) #comprimento do nome gerado aleatóriamente
    print(">", sep="",end="")

    for i in range(1, comprimento_do_nome + 1):

        letra = random.randrange(1,27)
        if letra == 1:
            letras_geradas = 'A'
        elif letra == 2:
            letras_geradas = 'B'
        elif letra == 3:
            letras_geradas = 'C'
        elif letra == 4:
            letras_geradas = 'D'
        elif letra == 5:
            letras_geradas = 'E'
        elif letra == 6:
            letras_geradas = 'F'
        elif letra == 7:
            letras_geradas = 'G'
        elif letra == 8:
            letras_geradas = 'H'
        elif letra == 9:
            letras_geradas = 'I'
        elif letra == 10:
            letras_geradas = 'J'
        elif letra == 11:
            letras_geradas = 'K'
        elif letra == 12:
            letras_geradas = 'L'
        elif letra == 13:
            letras_geradas = 'M'
        elif letra == 14:
            letras_geradas = 'N'
        elif letra == 15:
            letras_geradas = 'O'
        elif letra == 16:
            letras_geradas = 'P'
        elif letra == 17:
            letras_geradas = 'Q'
        elif letra == 18:
            letras_geradas = 'R'
        elif letra == 19:
            letras_geradas = 'S'
        elif letra == 20:
            letras_geradas = 'T'
        elif letra == 21:
            letras_geradas = 'U'
        elif letra == 22:
            letras_geradas = 'V'
        elif letra == 23:
            letras_geradas = 'W'
        elif letra == 24:
            letras_geradas = 'X'
        elif letra == 25:
            letras_geradas = 'Y'
        else:
            letras_geradas = 'Z'

        vetor_dos_nomes = [letras_geradas]
        for j in vetor_dos_nomes:
            print(f'{j}', sep="",end="")
    print("MON")




#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

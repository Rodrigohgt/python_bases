import base_binaria
import base_octal
import base_hexadecimal
#Grupo: #Alvaro Alves Araujo/RGM:30040124
        #Kleber Moura Bezerra/RGM:29366488
        #Raquel de Lima Souza/RGM:25158201      
        #Rodrigo Henrique G Teixeira /RGM:7224821985
        #Samuel Sampaio da Silva/RGM:28977688

#Projeto interdisciplinar: conversor de bases numéricas

#Primeiro o usuario entra com a opção de conversão de decimal, para a outra base desejada(1 binária, 2 octal, 3 hexadecimal)

def iniciar():

    tente_novamente = True
    #laço de repetição responsavel para se enquanto o usuario digitar um numero invalido, ele voltar para o laço.
    while(tente_novamente):
        print( '''opções:
[1] Base Binária
[2] Base Octal
[3] Base Hexadecimal
[4] Digite um novo valor
[5] Finalizar Conversões''')

        opcao = int(input('selecione uma das opções: '))
        #tomada de decisão responsavel por iniciar a função "iniciar"
        if(opcao == 1):
            print("Iniciando base binária")
            base_binaria.iniciar()
            break
        elif(opcao == 2):
            print("iniciando base Octal 2")
            base_octal.iniciar()
            break
        elif(opcao == 3):
            print("Iniciando base hexadecimal")
            base_hexadecimal.iniciar()
            break
        elif(opcao == 4):
            print("Digite novamente")
            continue
        elif(opcao == 5):
            print("finalizando app")
            break
        else:
            print("Erro, Tente novamente")
            continue

if(__name__ == "__main__"):
    iniciar()
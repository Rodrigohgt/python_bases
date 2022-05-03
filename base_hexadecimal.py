from tqdm import tqdm

#Projeto interdisciplinar: conversor para base hexadecimal
# função responsavel por iniciar o codigo abaixo 
def iniciar():
    #Primeiro o usuario entra com a opção de conversão de decimal, para a outra base desejada(1 binária, 2 octal, 3 hexadecimal)
    num = int(input('Digite um número inteiro para base Hexadecimal: '))
    opcao = 1
    while opcao != 5:
    
    #Barra de progresso da conversão de bases; O for i in tqdm range, indica quantas partes a barra de progresso sera dividida ate a sua conclusao; "result =" ao valor total da barra, neste caso i = 100
        result = 0
        for i in tqdm(range(100)):
            result += 1
        #agora vamos para as condições de cada opção
        #para a opção 1) Base hexadecimal
        if opcao == 1:
            print('{} Convertido para base Hexadecimal é igual a: {}' .format(num, hex(num)[2:]))
            break
            #os {} indica o numero escolhido pelo usuário, e o resultado
            #.format indica uma conversão a ser realizada
       
        #caso a opção seja invalida pelo usuario sera necessario digitar novamente
        else:
            print("Opção inválida, digite novamente: ")
            continue
            
print('Obrigado por ultilizar nosso sistema de conversão de bases numéricas; Volte Sempre!')

if(__name__ == "__main__"):
    iniciar()
from os import system, name #importa biblioteca do sistema operacional  e o nome do sistema operacional              
#if ternario (if escrito em uma linha so, nao pode ter elif)
system('cls') if (name == 'nt') else system('clear')
print(" faça seu pedido: \n")   
print('1- Hamburguer ')
print('2- Batata Fritas')
print('3- Salada ')
print('4- Refri')
print(' X - Para finalizar')
item=''
pedido=''
while (item != 'X'):
    print('\nEscolha o item pelo numero')
    item= input('-> ').lower()
    if (item== '1'or item=='2'or item=='3'or item=='4'):
        pedido+= item + ','
    elif(item=='X'):
        print('pedido finalizado ',pedido)
    else:
        print('Voce escolheu um intem fora do cardapio')
print(pedido)
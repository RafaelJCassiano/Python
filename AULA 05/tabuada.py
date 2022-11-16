from os import system, name #importa biblioteca do sistema operacional  e o nome do sistema operacional              
#if ternario (if escrito em uma linha so, nao pode ter elif)
system('cls') if (name == 'nt') else system('clear')
tabuada = 4
for i in range(11):
   # print('{} X {} = {}'.format(tabuada,i,tabuada*i))
   print(f"{tabuada:>3} X {i:>3} = {tabuada*i:>3}")# : inicia uma formatação * > a direita

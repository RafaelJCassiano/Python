from os import system, name#importa biblioteca do  sistema operacional  e o nome do sistema operacional              
#if ternario (if escrito em uma linha so, nao pode ter elif)
import random
jogo = 's'
while (jogo.lower() == "s"):
    system('cls') if (name == 'nt') else system('clear')
    print('Jogo: Papel, Pedra e Tesoura '.center(80,'*'))
    print('\nEscolha a Opção para Iniciar')
    print('[0]Palpel\n[1]Pedra\n[2]Tesoura\n')
    jogada = input (' -> ')
    jogada = int(jogada)
    computador = random.randint(0,2)
    opcoes = ["Papel","Pedra","Tesoura"]
    resultado = [["Deu empate","Você Ganhou","Você Perdeu"],
                 ["Você Perdeu","Deu Empate","Você Ganhou"],
                ["Você Ganhou","Você Perdeu","Deu Empate"]]
    
    
    
    
    
    print(resultado[jogada][computador])
    print(f'Você -> {opcoes[jogada]} X {opcoes[computador]} <- Computador')
    jogo = input('\n deseja Jogar novmente ? Aperta S para continuar')
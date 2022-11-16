from os import system #importa biblioteca do sistema operacional                
system('cls')

#criaçãoi de variavel de texto

nomeCompleto = 'rafael de jesus cassiano'
print(len(nomeCompleto))    
print(nomeCompleto.count('e'))
print(nomeCompleto.upper())
print(nomeCompleto.lower())   
print(nomeCompleto.capitalize())
print(nomeCompleto.find(' '))
espaco = nomeCompleto.find(' ')
nome = nomeCompleto[0:espaco]
print (nome)
print(nomeCompleto.replace(' ','_'))
print (nomeCompleto.center(40,"*"))
print(nomeCompleto.split(' '))



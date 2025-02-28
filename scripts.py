# print('Convertendo para inteiros ')
# n1=int(input('Digite um numero'))
# n2=int(input('Digite outro numero'))
# s=n1+n2

# print(type(s))
# print('A soma entre',n1,'e',n2,'vale',s)
# print('ou')
# print('A soma entre {} e {} vale {}'.format(n1, n2, s))#usar {} para substituir as variaveis
# print('verificar se o valor pode ser convertido para numero')
# n='5'
# print(n.isnumeric())
#
# print('verificar se o valor é numerico')
# sdgfsfgr='a'
# print(sdgfsfgr.isalpha())
#
# print('verificar se o valor é alfanumerico')
# dsamaskd='5a'
# print(dsamaskd.isalnum())

# print('Operadores aritméticos')
# print('O que python tem de diferente é o uso de // para fazer uma divisão inteira, em que da o resultado da divisão sem o resto')
# print('A ordem de precedência é primeiro parenteses, depois potenciação, depois multiplicações, divisões, divisão inteira e resto')
# print('Outra forma de fazer potênciação, é usando pow(a, b), veja:')
# print('5 elevado a 3 é:', pow(5,3))
# print('O problema de usar pow(n1, n2) é que se perde a ordem de precedência.')
# print('Raiz quadrada')
# print('Pra calcular a raiz quadrada de um número, se faz o número elevado a 1/2. Se for raiz cúbica, se faz o número elevado a 1/3, veja:')
# print(int(15**(1/2)), 'raiz quadrada de 15 (aqui foi usado int para envelopar a conta para que o resultado de inteiro, sendo que ele sempre é arredondado para baixo.)')
# print(int(16**(1/2)),'raiz quadrada de 15, como numero real')
# print(16**(1/2),'raiz quadrada de 15, como numero real')
# print(125**(1/3), 'raiz cubica de 125')
# print('Para definir a quantidade de casas decimais, se usa o :.nf, onde n é a quantidade de casas decimais, veja:')
# print('{:.2f}'.format(3.1415), 'aqui foi usado "{:.2f}" para definir 2 casas decimais')
# print('Para nao quebrar a linha ao usar print, colocar end="" no final do print, como aqui...', end="")
# print('...nesse exemplo')
# print('Para pular linha, se usa \n DENTRO DA STRING, veja:')
# print('linha 1\nlinha 2')

# lskdsd = int(input('Digite um numero de 10 a 99: '))
# print(lskdsd + 1)

# print('Outra forma de usar .format é colocar f antes das aspas, veja:')
# print(f'A soma entre {n1} e {n2} vale {s}')
# n = 1000
# print(f'O valor de n é {n}')

# print('Para importar bibliotecas, se usa import:')
# import math
# print('Para importar funções especificas de uma biblioteca, se usa from:')
# from math import sqrt, factorial
# print('para usar a biblioteca importada depois e só digitar o nome dela com um ponto e depois a função que quer (como math.fatorial)')
#
#importando apenas uma função de uma biblioteca, não precisa acessar a biblioteca(biblioteca.xxx) para declarar a função
#ceil arredonda pra cima

# from math import ceil, sqrt
# n = int(input('Digite um numero para ver sua raiz quadrada: '))
# n2 = sqrt(n)
# print(f'A raiz quadrada de {n} usando :.0f para ter 2 casas decimais é {n2:.2f}')
# print(f'A raiz quadrada de {n} usando ceil pra arredondar pra cima é {ceil(n2)}')

#para ver a lista de bibliotecas https://docs.python.org/3/library/index.html

# #Package index: instalar pacotes adicionais indo no site python.org, depois em PyPi, aí
# import emoji
# print(emoji.emojize(":grinning_face:!")) # lembrar de usar aspas
# print('Pra ver os modulos instalados, vá em interpretadores python de projeto dentro das preferencias do pycharm')

# import random
# print('lista de variaveis, usar colchetes pra envolver a variavel')
# n1 = str(input('digite um nome'))
# n2 = str(input('digite um nome'))
# n3 = str(input('digite um nome'))
# lista = [n1, n2, n3]
# escolhido = random.choice(lista)
# print(escolhido)
# random.shuffle(lista)
# print(lista)

# frase = 'Curso em Video Python'
# print(len(frase))
# print('caso a variavel tenha apenas um objeto, len retorna o numero de caracteres')
# print('caso a variavel tenha mais de um objeto, len retorna o numero de objetos')
# print('Usar variável.find() pra indicar a posição em que acha uma parte do texto: \n', f'Nesse caso, a palavra Video esta na posição {frase.find('Video')}')
# print(f'O numero de vezes que V aparece: \n{frase.count('V')}')
# print('Se ele não achar o valor especificado, irá retornar -1')
#
# print('Cada caractere dentro de uma string entra em um espaço de memória, numerado a partir do 0, para saber os valores dentro de cada espaço de memória usar a notação:')
# print('frase(5:13), em que ele conta as variaveis na posição 5 até a 12(o ultimo numero deixa de fora)')
#
# print('pra saber se um valor está dentro da variável na forma de verdadeiro ou falso, usar "in", por exemplo:')
# print('Resultado de Android in frase}', f'{'Android' in frase}')

# frase = 'Curso em Video Python'
# print('.replace(): Usar replace() para trocar palavras: ', f'{frase.replace('Python', 'Android')}')
# print('.upper(): usar upper() para fazer letras maiusculas: ', f'{frase.upper()}')
# print('Outros comandos: .lower(), .capitalize(), .title()')
# print('.strip(), usar para remover espaços em branco no começo e fim das strings')
# print('Pode-se usar .lstrip() ou .rstrip() para remover os espaços apenas na esquerda ou na direita')

# frase = 'Curso em Video Python'
# print('.split(), divide a string dentro da variavel em outras strings, separando pelo espaço em branco, e ao mesmo tempo cria uma lista de objetos dentro da variavel')
# print('use ''.join(variavel) para concatenar uma sequencia de strings usando o separados indicado no ''')
# print(f'{'-'.join(frase.split())}')
#
# print('Outro exemplo é:')
# palavras = ["Olá", "mundo", "Python"]
# frase = ' '.join(palavras)  # Junta as palavras com espaço entre elas
# print(frase)

# frase = 'Curso em Video Python'
# frase = frase.split()
# quantidade_de_palavras = len(frase)
# print(frase[quantidade_de_palavras-1])

# frase = 'Curso em Video Python'
# quantidade_de_palavras = len(frase)
# print(frase[quantidade_de_palavras-1])

# print('Condicionais')
# nota = float(input('qual sua nota?'))
# if nota >= 6:
#     print('Você esta aprovado')
# else:
#     print('Você está reprovado')

# import random
# from time import sleep
# print('Vamos jogar o jogo da advinhação!!!')
# print(f'Primeiro, você escolhe um número de 1 a 10, então, eu lhe digo que número eu pensei. Vamos ver quem é melhor!')
# print('Agora, vou te deixar pensar em um número...')
# sleep(3)
# palpite = int(input('Vamos lá, acabou o tempo, diga qual número que eu pensei: '))
# numeroPensado = int(random.choice(range(1, 11)))#até 11 pra selecionar 10
# if palpite == numeroPensado:
#     print('O que??? Como? Vc sabia? ')
# else:
#     print(f'MUHAHAHA MERO MORTAL, COMO OUSA ME DESAFIAR?!?!?! EU HAVIA PENSADO NO {numeroPensado}')
# input("Pressione Enter para sair...")

#CORES NO TERMINAL

# #FORMATAÇÃO DE LETRAS
# letra_branca = '\033[0m'
# letra_negrito = '\033[1m'
# letra_sublinhada = '\033[4m'
# letra_invertida = '\033[7m'

# preto = '\033[30;40m'
# vermelho = '\033[31;41m'
# verde = '\033[32;42m'
# amarelo = '\033[33;43m'
# azul = '\033[34;44m'
# magenta = '\033[35;45m'
# ciano = '\033[36;46m'
# cinza = '\033[37;47m'
# branco = '\033[97;107m'
# limpa = \033[m

# cores = {
#     'preto' : '\033[30m',
#     'vermelho' : '\033[31m',
#     'verde' : '\033[32m',
#     'amarelo' : '\033[33m',
#     'azul' : '\033[34m',
#     'magenta' : '\033[35m',
#     'ciano' : '\033[36m',
#     'cinza' : '\033[37m',
#     'branco' : '\033[97m',
#     'limpa' : '\033[m'
# }
# print('Para colocar cores no terminal, se usa um código: \033m[estilo; cor da letra; cor do fundo m')
# print(f'Exemplo: Este PC irá {cores['vermelho']}EXPLODIR{cores['limpa']} MUHAHAHA')

#CONVERSÕES PARA BINÁRIO, OCTAL E HEXADECIMAL.
#               +
#ESTRUTURAS IF, ELIF E ELSE
# n= int(input('Digite um número: '))
# base = int(input('Escolha para qual base converter:'
#       '\n1 pra binário'
#       '\n2 pra Octal'
#       '\n3 pra Hexadecimal'
#       '\n'))
# if base == 1:
#     print(f'O número {n} em binário é: {bin(n)}')
# elif base == 2:
#     print(f'O número {n} em octal é: {oct(n)}')
# elif base == 3:
#     print(f'O número {n} em hexadecimal é: {hex(n)}')
# else:
#     print('Digite um número válido.')

# #IF DENTRO DE OUTRO IF
# n = int(input('Digite um número: '))
# if n > 0:
#     print(f'{n} é um número positivo.')
#     if n % 2 == 0:
#         print(f'{n} é um número par.')
#     else:
#         print(f'{n} é um número ímpar.')
# elif n == 0:
#     print(f'{n} é um número neutro.')
# else:
#     print(f'{n} é um número negativo.')

# ESTRUTURAS DE REPETIÇÃO

#SINTAXE: for variavel in range(início, fim, passo):
# for c in range(0, 4, 2):#vai do 0 ao 3, termina no 4, pulando de 2 em 2.
#     print(c)
# print('fim')

#PROGRAMA DE CONTAGEM REGRESSIVA
# from time import sleep
# for c in range(10, 0, -1):
#     print(c)
#     sleep(1)
# print('Vaaaaai!!!')

#DE 1 A 50 APENAS PARES
# for c in range(1, 51):
#     if c % 2 == 0 and c != 50:
#         print(f'{c}, ', end='')
#     elif c == 50:
#         print(f'{c}.')

#Numeros primos
# n = int(input('Digite um número: '))
# vermelho = '\033[31m'
# amarelo = '\033[33m'
# h = 0
# for c in range(1, 11):
#     if n%c == 0:
#         h += 1
#         print(f'{vermelho}{c}', end='')
#     else:
#         print(f'{amarelo}{c}', end='')
#     if c == 10:
#         print('')#pra quebrar a linha
# if h != 0:
#     print(f'O número {n} foi divisível {h} vezes. Por isso, ele não é primo.')
# else:
#     print(f'O número {n} não é divisível por nenhum número. Por isso, ele é primo.')



#python -m PyInstaller --onefile seu_script.py

#24/02 manhã - aula 6 - https://youtu.be/hdDHg1p3YVc?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=108
#24/02 meio-dia - aula 7 - https://youtu.be/Vw6gLypRKmY?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1676
#25/02 manhã - aula 8 - https://youtu.be/oOUyhGNib2Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=429
#25/02 manhã - aula 8 - https://youtu.be/oOUyhGNib2Q?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1524
#25/02 tarde - aula 9 min 19:00 - https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1157
#26/02 meio-dia - aula 9 min 30:13 - https://youtu.be/a7DH88vk2Sk?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t=1813
#26/02 tarde - terminei aula 9 e exercícios, ir pra aula 10 https://youtu.be/K10u3XIf1-Qlist=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
#27/02 meio-dia - terminei aula 10, fazendo exercício 28 https://youtu.be/kchC5KLZSZ4?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
#27/02 tarde/noite - terminei exercícios aula 10, ir pra 11 https://www.youtube.com/watch?v=0hBIhkcA8O8&t=1425s
#28/02 manhã - vi aula 11, cores no terminal, ir pra aula 12 - https://www.youtube.com/watch?v=j9bYDjaAYzw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=2
#28/02 meio-dia - vi aula 12, condições aninhadas, continuar aula 13 em 8:32min - https://youtu.be/cL4YDtFnCt4?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&t=512
#28/02 tarde - terminei aula 13, ir pra aula 14 https://youtu.be/LH6OIn2lBaI?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye
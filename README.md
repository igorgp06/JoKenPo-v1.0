![3027818-pedra-papel-tesoura-gesto-com-a-mao-gratis-vetor](https://github.com/igorgp06/JoKenPo-v1.0/assets/166974033/bd43c3a2-323e-4bfc-ad80-ce8cf1e6c589)

### Um simples jogo de Jo Ken Pô criado em python

#### Um jogo que usa como pricipal forma de sorteio o termo RANDINT da biblioteca RANDOM.

> Nova versão 2.0 em breve

## Como funciona?

+ __O jogo funciona de uma maneira bem simples. Os únicos termos que usaremos que é necassário dar import são:__
~~~~python
from random import randint
from time import sleep
~~~~
Usaremos o RANDIT para fazer a máquina escolher um item aleatório dentro da lista que mostrarei a seguir. O termo SLEEP serve como uma decoração, dando uma certa imersão ao jogo, apenas. 

+ __A próxima função usamos para facilitar na hora de atribuir cores ao nosso jogo, deixando o mesmo mais bonito e intuitivo.__
~~~python
cor = {'nocolor': '\033[m',
       'preto': '\033[30m',
       'vermlho': '\033[31m',
       'azul': '\033[34m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'branco': '\033[97m',
       'roxo': '\033[35m'}
~~~~

+ __A seguir definimos as funções básicas, sendo elas:__
~~~~python
opcoes = ('Pedra', 'Papel', 'Tesoura')
escolhas = randint(0, 2)
~~~~
Atribuimos as __opções__ a uma __lista__ e em seguida fazemos com que as __escolhas__ escolham aleatóriamente um item dentro desta mesma lista.

+ __Aqui apresentamos funções que ajudam para que o cógido não fique cumprido:__
~~~~python
empate = f'\033[1m{cor["amarelo"]}EMPATE{cor["nocolor"]}'
vitplayer = f'\033[1m{cor["verde"]}Você ganhou!{cor["nocolor"]}'
derrota = f'\033[1m{cor["vermlho"]}Você perdeu!{cor["nocolor"]}'
joginva = f'\033[1m{cor["vermlho"]}JOGADA INVÁLIDA!{cor["nocolor"]}'
~~~~
Atribuimos diversas váriaveis a palavras que vamos usar mais para frente. Fazemos isto para que nosso código não tenha tanta poluição visual quando formos inserir cores em nosso algoritimo.

+ __Apresente as escolhas que o jogador tem:__
~~~~python
print(f"""\033[1mEscolha alguma destas opções para jogar:
[0] Pedra
[1] Papel
[2] Tesoura{cor['nocolor']}""")
player = int(input(f'Escreva aqui {cor["azul"]}sua escolha: {cor["nocolor"]}'))
~~~~
Aqui atribuimos a váriavel __PLAYER__ a um número que o jogador deverá escolher para jogar, ou seja, o número que o jogador escolher ficara salva dentro da veriável __player__.

+ __Decoração usando o SLEEP:__
~~~python
print(f'\033[1mJO{cor["nocolor"]}')
sleep(0.7)
print(f'\033[1mKEN{cor["nocolor"]}')
sleep(0.7)
print(f'\033[1mPÔ{cor["nocolor"]}')
~~~
Parte decorativa que irá escrever o que foi designado no __PRINT__ dentro de 0.7 segundos, isto ocorrerá duas vezes.

+ __Apresente o que a máquina escolheu e o que o jogador escolheu:__
~~~python
print(f'{cor["roxo"]}-----{cor["nocolor"]}' * 10)
print(f'\033[1mO computador {cor["amarelo"]}escolheu {opcoes[escolhas]}{cor["nocolor"]}')
print(f'\033[1mO jogador {cor["azul"]}escolheu {opcoes[player]}{cor["nocolor"]}')
print(f'{cor["roxo"]}-----{cor["nocolor"]}' * 10)
~~~
Esta parte mostra o que o jogador e a máquina escolheram anteriormente, a função a seguir que será responsáve por apresentar quem perdeu, quem ganhou ou sed ouve um empate.

+ __Sistema de escolhas usando IF, ELIF E ELSE:__
~~~python
if escolhas == 0:                # pedra
    if player == 0:
        print(empate)
    elif player == 1:
        print(vitplayer)
    elif player == 2:
        print(derrota)
    else:
        print(joginva)
elif escolhas == 1:              # papel
    if player == 0:
        print(derrota)
    elif player == 1:
        print(empate)
    elif player == 2:
        print(vitplayer)
    else:
        print(joginva)
elif escolhas == 2:              # tesoura
    if player == 0:
        print(vitplayer)
    elif player == 1:
        print(derrota)
    elif player == 2:
        print(empate)
    else:
        print(joginva)
else:
    print(joginva)
~~~
Chegamos a parte chata. Aqui fuciona assim, a máquina escolheu um número, caso tenha sido o número __1__ o segundo __ELIF__ irá entrar em ação, comparando a escolha do jogador com as da máquina. 
Se o jogador tiver escolhido o número __0__ ele irá perder, pois o número __0__ tem a equivalência a __PEDRA__ e como a máquina escolheu o número __1__ que equivale ao __PAPEL__ ela sairá vitoriosa. 
Agora se o jogador tivesse escolhido o número __2__ que equivale a __TESOURA__ ele teroa gamhado da máquina. Esta explicação vale para todo o resto do __Sistema de escolhas__.

## O que foi usado: 

  <table>
    <tr>
      <td><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"</td> 
      <td><img src="https://img.shields.io/badge/vscode-4285F4?style=for-the-badge&logo=vscode&logoColor=white"</td>
    </tr>
    <tr>
      <td>VER 3.12.4</td>
      <td>VER 1.99.0</td>
    </tr>
  </table>




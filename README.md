### Um simples jogo de Jo Ken Pô criado em python.

![3027818-pedra-papel-tesoura-gesto-com-a-mao-gratis-vetor](https://github.com/igorgp06/JoKenPo-v1.0/assets/166974033/bd43c3a2-323e-4bfc-ad80-ce8cf1e6c589)


#### Um jogo que usa como pricipal forma de sorteio o termo __RANDINT__ da biblioteca __RANDOM__. E as funções __IF__, __ELIF__ e __ELSE__ para comparar as escolhas e decidir um vencedor.
> #### __Desenvoldido por [Iorgp06](https://github.com/igorgp06).__
> #### __Nova versão 2.0 em breve.__

## Como funciona?

+ ### __Importe os termos básicos da biblioteca:__
~~~~python
from random import randint
from time import sleep
~~~~
Usaremos o __RANDIT__ para fazer a máquina escolher um item aleatório dentro da __lista__ que mostrarei a seguir. O termo __SLEEP__ serve como uma decoração, dando uma certa imersão ao jogo, isto o torna um elemento opcional ao nosso código, fica ao seu críterio alterá-lo ou não.


+ ### __Defina uma váriavel para cores:__
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
Aqui atribuimos uma váriavel __COR__, ela será responsável por fazer com que nosso programa fique mais organizado e visualmente bonito.


+ ### __Definina as funções básicas, sendo elas:__
~~~~python
opcoes = ('Pedra', 'Papel', 'Tesoura')
escolhas = randint(0, 2)
~~~~
Atribuimos as __opções__ a uma __lista__ e em seguida fazemos com que as __escolhas__ escolham aleatóriamente um item dentro desta mesma lista.


+ ### __Atribua váriaveis para encurtar o código:__
~~~~python
empate = f'\033[1m{cor["amarelo"]}EMPATE{cor["nocolor"]}'
vitplayer = f'\033[1m{cor["verde"]}Você ganhou!{cor["nocolor"]}'
derrota = f'\033[1m{cor["vermlho"]}Você perdeu!{cor["nocolor"]}'
joginva = f'\033[1m{cor["vermlho"]}JOGADA INVÁLIDA!{cor["nocolor"]}'
~~~~
Atribuimos diversas váriaveis a palavras que vamos usar mais para frente. Fazemos isto para que nosso código não tenha tanta poluição visual quando formos inserir cores em nosso algoritimo.


+ ### __Apresente as escolhas que o jogador tem:__
~~~~python
print(f"""\033[1mEscolha alguma destas opções para jogar:
[0] Pedra
[1] Papel
[2] Tesoura{cor['nocolor']}""")
player = int(input(f'Escreva aqui {cor["azul"]}sua escolha: {cor["nocolor"]}'))
~~~~
Aqui atribuimos a váriavel __PLAYER__ a um número que o jogador deverá escolher para jogar, ou seja, o número que o jogador escolher ficara salva dentro da veriável __PLAYER__.


+ ### __Decoração usando o SLEEP:__
~~~python
print(f'\033[1mJO{cor["nocolor"]}')
sleep(0.7)
print(f'\033[1mKEN{cor["nocolor"]}')
sleep(0.7)
print(f'\033[1mPÔ{cor["nocolor"]}')
~~~
Parte decorativa que irá escrever o que foi designado no __PRINT__ dentro de 0.7 segundos, isto ocorrerá duas vezes.


+ ### __Apresente o que a máquina escolheu e o que o jogador escolheu:__
~~~python
print(f'{cor["roxo"]}-----{cor["nocolor"]}' * 10)
print(f'\033[1mO computador {cor["amarelo"]}escolheu {opcoes[escolhas]}{cor["nocolor"]}')
print(f'\033[1mO jogador {cor["azul"]}escolheu {opcoes[player]}{cor["nocolor"]}')
print(f'{cor["roxo"]}-----{cor["nocolor"]}' * 10)
~~~
Esta parte apresenta o que o jogador e a máquina escolheram em forma de __Pedra__, __Papel__ ou __Tesoura__, isto só é possível se as __váriaveis__ __OPCOES__ e __ESCOLHAS__ forem definidas corretamente. Caso contrário, o código não funcionária. 


+ ### __Sistema de escolhas usando IF, ELIF E ELSE:__
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
Aqui fuciona da seguinte maneira, a máquina escolheu um número, caso tenha sido o número __1__ o segundo __ELIF__ irá entrar em ação, comparando a escolha do jogador com as da máquina. 
Se o jogador tiver escolhido o número __0__ ele irá perder, pois o número __0__ tem a equivalência a __PEDRA__ e como a máquina escolheu o número __1__ que equivale ao __PAPEL__ ela sairá vitoriosa. 
Agora se o jogador tivesse escolhido o número __2__ que equivale a __TESOURA__ ele teria ganhado da máquina, o mesmo se aplica para o resto do __Sistemas de escolhas__. 
Resumidamente, ele pega a jogada da máquina e compara com as do jogador, decidindo assim, quem ganhou e quem perdeu.


## Como iniciar o programa:
##### Infelizmente a versão 1.0 do jogo __não possui__ uma tela dedicada, ou seja, o jogo deve ser iniciado num executor de códigos capaz de rodar a linguagem __Python__. Para isto devemos copiar e colar o código num executor para rodarmos o jogo no terminal do executor.

##### Estou trabalhando em alguns ajustes, em algum tempo uma nova atualização deverá surgir com melhorias e correções de bugs, então aguarde pequenas alterações no código até o lançamento da versão 2.0.


## O que foi usado: 

<div>
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
</div>

## Minhas redes sociais:

 <div align="left">
  <a href="https://www.instagram.com/igorgp.06/" target="_blank"> <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="instagram logo"/></a>
  <a href="https://discord.com/channels/@me" target="_blank"> <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="discord logo"></a>
  <a href="https://www.youtube.com/channel/UCka20SjP7fwABfHGbt_xwjg" target="_blank"> <img src="https://img.shields.io/static/v1?message=Youtube&logo=youtube&label=&color=FF0000&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="youtube logo"/></a>
  <a href="https://twitter.com/igorgp06" target="_blank"> <img src="https://img.shields.io/static/v1?message=Twitter&logo=twitter&label=&color=1DA1F2&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="twitter logo"  /></a>
</div>


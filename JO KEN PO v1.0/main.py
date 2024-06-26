from random import randint
from time import sleep

# --------------------------------------------------------------------------------------------- #

# cores

cor = {'nocolor': '\033[m',
       'preto': '\033[30m',
       'vermlho': '\033[31m',
       'azul': '\033[34m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'branco': '\033[97m',
       'roxo': '\033[35m'}

# --------------------------------------------------------------------------------------------- #

# funções básicas

opcoes = ('Pedra', 'Papel', 'Tesoura')
escolhas = randint(0, 2)

# funções para decoração

empate = f'\033[1m{cor["amarelo"]}EMPATE{cor["nocolor"]}'
vitplayer = f'\033[1m{cor["verde"]}Você ganhou!{cor["nocolor"]}'
derrota = f'\033[1m{cor["vermlho"]}Você perdeu!{cor["nocolor"]}'
joginva = f'\033[1m{cor["vermlho"]}JOGADA INVÁLIDA!{cor["nocolor"]}'


# começo do game e escolha do jogador

print(f"""\033[1mEscolha alguma destas opções para jogar:
[0] Pedra
[1] Papel
[2] Tesoura{cor['nocolor']}""")
player = int(input(f'Escreva aqui {cor["azul"]}sua escolha: {cor["nocolor"]}'))

# decoração jo ken po

print(f'\033[1mJO{cor["nocolor"]}')
sleep(0.7)
print(f'\033[1mKEN{cor["nocolor"]}')
sleep(0.7)
print(f'\033[1mPÔ{cor["nocolor"]}')

# resultados

print(f'{cor["roxo"]}-----{cor["nocolor"]}' * 10)
print(f'\033[1mO computador {cor["amarelo"]}escolheu {opcoes[escolhas]}{cor["nocolor"]}')
print(f'\033[1mO jogador {cor["azul"]}escolheu {opcoes[player]}{cor["nocolor"]}')
print(f'{cor["roxo"]}-----{cor["nocolor"]}' * 10)

# sistema de escolhas

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

# --------------------------------------------------------------------------------------------- #
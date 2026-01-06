# importando bibliotecas
import random
from time import sleep

# realizando a escolha do computador
computador = random.randint(1, 3)

# interface
print('\033[1;33m-=-\033[m' * 10)
print('\033[1;34mJOKENPÔ, ME VENÇA SE PUDER\033[m')
print('\033[1;33m-=-\033[m' * 10)

# menu
usuario = int(input('''\033[1;35m*****ESCOLHA SUA OPÇÃO*****
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA
opção: '''))

# interface
print('\033[1;34mJO\033[m')
sleep(1)
print('\033[1;34mKEN\033[m')
sleep(1)
print('\033[1;34mPÕ\033[m')

# resposta
if computador == 1 and usuario == 3:
    print(f'Escolhi pedra! GANHEI DE VOCÊ!')
elif computador == 1 and usuario == 2:
    print(f'PARABÉNS! Escolhi pedra, você ganhou de mim!')
elif computador == 2 and usuario == 1:
    print(f'Escolhi papel! GENHEI DE VOCÊ!')
elif computador == 2 and usuario == 3:
    print(f'PARABÉNS! Escolhi papel, você ganhou de mim!')
elif computador == 3 and usuario == 1:
    print(f'PARABÉNS! Escolhi tesoura, você ganhou de mim!')
elif computador == 3 and usuario == 2:
    print(f'Escolhi tesoura! GANHEI DE VOCÊ!')
elif computador == usuario:
    print('EMPATE!')
else:
    print('\033[1;31mOPÇÃO INVALIDA!')


# importando bibliotecas
import pygame as py
from pygame.locals import *
import random


# tamanho da janela
window_size = (600, 600)

pixel_size = 10


def colision(pos1, pos2):
    return pos1 == pos2

def off_limits(pos):
    if 0 <= pos[0] < window_size[0] and 0 <= pos[1] < window_size[1]:
        return False
    else:
        return True

def random_on_grid():
    x = random.randint(0, window_size[0])
    y = random.randint(0, window_size[1])
    return x // pixel_size * pixel_size, y // pixel_size * pixel_size


# iniciando janela
py.init()

# definindo o tamanho e o título da janela
screen = py.display.set_mode(window_size)
py.display.set_caption('Snake')


# criando a cobra
snake_pos = [(250, 50), (260, 50), (270, 50)]



# criando a superficie da cobra
snake_surface = py.Surface((pixel_size, pixel_size))
snake_surface.fill((40, 237, 231))
snake_direction = K_LEFT

# criando a superficie da maçã
apple_surface = py.Surface((pixel_size, pixel_size))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()


def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()

# deixando a janela aberta
while True:
    py.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)

    if colision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()

    for pos in snake_pos:
        screen.blit(snake_surface, pos)



    for i in range(len(snake_pos) - 1, 0, -1):
        if colision(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i - 1]

    if off_limits(snake_pos[0]):
        restart_game()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - pixel_size)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + pixel_size)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - pixel_size, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + pixel_size, snake_pos[0][1])

    py.display.update()

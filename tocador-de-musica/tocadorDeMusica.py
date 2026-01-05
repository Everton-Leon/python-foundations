# importando biblioteca
import pygame

# utilizando as funções da biblioteca para tocar a música
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(input('Qual música você quer ouvir? ')) # o nome do documento da música
pygame.mixer.music.play()
pygame.event.wait()

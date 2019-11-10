import pygame
import cores
import os
cores = cores.cores()

pygame.init()

tamanho = pygame.display.set_mode([800,600])


def janela(background,x,y):  
    os.environ['SDL_VIDEO_CENTERED'] = '1' #Centralizar a janela do game
    pygame.display.set_caption("Jogo Da Forca")
    tamanho.fill(cores.branco)
    tamanho.blit(background,(x,y))
    pygame.display.update()

def redraw(img,x,y):
    os.environ['SDL_VIDEO_CENTERED'] = '1' #Centralizar a janela do game
    tamanho.blit(img,(x,y))
    pygame.display.update()





    


import pygame

class imagens(object):                                    #Imagem de fundo do menu
    def __init__(self):
        self.menu = pygame.image.load("imagens/menu.jpg") # Pegar imagem do diretorio
        self.game = pygame.image.load("imagens/game_back.png")

import pygame

class imagens():                                    #Imagem de fundo do menu
    def __init__(self):
        self.menu = pygame.image.load("imagens/menu.jpg") # Pegar imagem do diretorio
        self.game = pygame.image.load("imagens/game_back.png")

'''def imagensMenu():
     # Pegar imagem do diretorio
    return(pygame.image.load("imagens/menu.jpg"))
def imagensGame():    
    return(pygame.image.load("imagens/game_back.png"))'''

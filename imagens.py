import pygame

class imagens():                                    #Imagem de fundo do menu
    def __init__(self):
        self.menu = pygame.image.load("imagens/menu.jpg") # Pegar imagem do diretorio
        self.game = pygame.image.load("imagens/Ngame_back.png")
        self.traco = pygame.image.load("imagens/traços3.png")

import pygame
import os
import cores

cores = cores.cores()

class windows():
    def __init__(self,xwindow,ywindow,title,background,music,music_status,music_img,img_pos):
        os.environ['SDL_VIDEO_CENTERED'] = '1' #Centralizar a janela do game
        pygame.init()                         #Inicializa o PyGame 
        #Cria tudo dentro da tela        
        self.xwindow = xwindow
        self.ywindow = ywindow
        self.title = title
        self.background = background
        self.music = music
        self.music_status = music_status    # Ativa e desativa a musica
        self.music_img = music_img          # Imagem da musica ativada e desativada
        self.img_pos = img_pos              # Posicionamento da imagem 
        self.window = pygame.display.set_mode([self.xwindow,self.ywindow])
        pygame.display.set_caption(self.title)
        self.window.blit(self.background,self.img_pos) # Pra imagem ser colocada na tela (PREENCHER) blit é imagem, fill é cor
    def get_background(self):
        return(self.background)
    def set_background(self,background):
        self.background = background
        self.window.blit(self.background,self.img_pos) # Pra imagem ser colocada na tela (PREENCHER) blit é imagem, fill é cor
        
    def get_musica(self,music):
        return(self.music)
    def set_musica(self,music):
        self.music = music


        
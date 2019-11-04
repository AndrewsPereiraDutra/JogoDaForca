import pygame
import window
import imagens
import cores
import game
imagens = imagens.imagens()
cores = cores.cores()
class menu(object):
    def __init__(self):
        self.xwindow = 800
        self.ywindow = 600
        self.title = "Jogo"
        self.background = imagens.menu       #diretorio da imagem (imagens.menu)
        self.music = 0                       #diretorio da musica
        self.music_status = 0                #True or false
        self.music_img = 0                   #imagens.musica
        self.img_pos = (0,0)                 # Estenda a imagem da posição zero X e zero Y
        self.frames = pygame.time.Clock()    #fps (cria um objeto para ajudar a controlar o tempo)
        self.window = window.window(self.xwindow,self.ywindow,self.title,self.background,self.music,self.music_status,self.music_img,self.img_pos)
    
        self.RunOn = True 
        #Main Loop
        while self.RunOn:
            self.frames.tick(27)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): #Sair
                    self.RunOn = False
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    (self.xMouse,self.yMouse) = event.pos #Posiçao do mouse eixo X e Y
                    print("x: "+str(self.xMouse))
                    print("y: "+str(self.yMouse))
                    if (self.xMouse >= 251 and self.xMouse <= 548):
                        if (self.yMouse >= 179 and self.yMouse <= 244):
                           verificacao.get_ok()
                           self.RunOn = False 


                        if (self.yMouse >= 299 and self.yMouse <= 369):
                           print("ok") 

                        if (self.yMouse >= 421 and self.yMouse <= 489):
                            self.RunOn = False

            pygame.display.update()

menu()

        


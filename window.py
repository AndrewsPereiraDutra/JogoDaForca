import pygame 
import os
import superficie
sup = superficie.superficie()



class window:
    def __init__(self,xwindow,ywindow,title,background,music,statusMusic):
        os.environ["SDL_VIDEO_CENTERED"]="1"
        pygame.init()
        self.xwindow = xwindow
        self.ywindow = ywindow
        self.title = title 
        self.background = background 
        self.music = music 
        self.statusMusic = statusMusic 
        self.window = pygame.display.set_mode([self.xwindow,self.ywindow])
        pygame.display.set_caption(self.title)
        pygame.display.update()
    def setBack(self,fundo,back_pos):
        self.window.fill((255,255,255))
        self.window.blit(fundo,back_pos)
    def superficie(self,sup_nome,sup_pos):
        self.window.blit(sup_nome,sup_pos)
 
    def setBackSup(self,sup_nome,sup_back,sup_back_pos):
        sup_nome.fill((255,255,255))
        sup_nome.blit(sup_back,sup_back_pos)
    
    def music_on(self,music_stats,music):
        if music_stats:
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()
        
    def redraw(self,img,imgSound,window):
        window.setBack(img,(0,0))
        window.setBackSup(sup.sound,imgSound,(0,0)) #posição da imagem dentro da superficie
        window.superficie(sup.sound,(750,0))
    
    #def redraw_texto(self,texto,window):
        #window.setBack(texto,(200,50))
    
    def desenharTexto(self,texto,window,x,y):
        self.window.blit(texto,(x,y))
        

    def desenha(self, img,x,y):
        self.window.blit(img,(x,y))
        
        
    





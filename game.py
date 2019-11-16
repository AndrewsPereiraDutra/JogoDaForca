import pygame
import window
import images
import music
import superficie
import time
imagens = images.images()
sup = superficie.superficie()
musica = music.music()

class game():
    def __init__(self):
        self.window = window.window(800,600,"Jogo",imagens.back,musica.menu,0)
        self.window.setBack(imagens.back,(0,0))
        self.main()
    def main(self):
        RunOn = True 
        frames = pygame.time.Clock()
        esta_tocando = True
        sound = imagens.soundOn 
        esc_down = True
        desenharp = True
        x = 350
        self.window.music_on(esta_tocando,musica.menu)
        while RunOn:
            frames.tick(30)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    RunOn = False
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    (mouseX,mouseY) = event.pos
                    if ((mouseX >= 750) and (mouseX <= 800)) and ((mouseY>= 0) and (mouseY <= 50)):
                        if esta_tocando:
                            esta_tocando = False
                            sound = imagens.soundOff
                        else:
                            esta_tocando = True 
                            sound = imagens.soundOn
                        self.window.music_on(esta_tocando,musica.menu)
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):                        
                        while esc_down:
                            self.window.setBackSup(sup.menuEsc,imagens.menuEsc,(0,0)) #posição da imagem dentro da superficie
                            self.window.superficie(sup.menuEsc,(266,200)) 
                            for event in pygame.event.get():
                                if (event.type == pygame.QUIT):  #Para o Esc funcionar 
                                    esc_down = False
                                    RunOn = False
                                if (event.type == pygame.MOUSEBUTTONDOWN):
                                    (mouseX,mouseY) = event.pos 
                                    print(mouseX)
                                    print(mouseY)
                                    if (mouseX >= 345) and (mouseX <= 450):
                                        if (mouseY >= 262) and (mouseY <= 292):
                                            esc_down = False
                                            print("ta certo")
                                        elif (mouseY >= 317) and (mouseY <= 347):
                                            RunOn = False
                                            esc_down = False
                                                    
                                if (event.type == pygame.KEYDOWN):
                                    if (event.key == pygame.K_ESCAPE):
                                        esc_down = False
                            pygame.display.update()
                        esc_down = True
                   
            self.window.redraw(imagens.back,sound,self.window)
            if desenharp:
                for i in range(0, 5):       
                    self.window.desenha_traco(imagens.traco, x, self.window)
                    x += 60
                desenharp = False  
            else:
                x = 350
                desenharp = True
            pygame.display.update()
            
            


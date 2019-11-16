import pygame
import window
import images 
import superficie
import music
import game
imagens = images.images()
sup = superficie.superficie()
musica = music.music()


class menu():
    def __init__(self):
        self.window = window.window(800,600,"jogo",imagens.menu,0,0)
        self.window.setBack(imagens.menu,(0,0))
        self.window.setBackSup(sup.sound,imagens.soundOn,(0,0)) #posição da imagem dentro da superficie
        self.window.superficie(sup.sound,(750,0))        
        self.menu()
    def redraw(self,img,imgSound):
        self.window.setBack(img,(0,0))
        self.window.setBackSup(sup.sound,imgSound,(0,0)) #posição da imagem dentro da superficie
        self.window.superficie(sup.sound,(750,0)) 
    def menu(self):
        RunOn = True 
        frames = pygame.time.Clock()
        esta_tocando = True
        sound = imagens.soundOn 
        self.window.music_on(esta_tocando,musica.menu)
        while RunOn:
            frames.tick(30)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    RunOn = False
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    (mouseX,mouseY) = event.pos
                    if (mouseX >= 251) and (mouseX <= 548):
                        if (mouseY >= 179) and (mouseY <= 244):
                            RunOn = False
                            game.game()
                        elif (mouseY >= 299 ) and (mouseY <= 369):
                            print("sobre")
                        elif (mouseY >= 421) and (mouseY <= 489):
                            RunOn = False
                    elif ((mouseX >= 750) and (mouseX <= 800)) and ((mouseY>= 0) and (mouseY <= 50)):
                        if esta_tocando:
                            esta_tocando = False
                            sound = imagens.soundOff
                        else:
                            esta_tocando = True 
                            sound = imagens.soundOn
                        self.window.music_on(esta_tocando,musica.menu)
            if RunOn:
                self.window.redraw(imagens.menu,sound,self.window)
                
            pygame.display.update()
                            

                        

                        


menu()
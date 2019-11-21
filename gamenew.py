import pygame
import window
import images
import music
import superficie
import time
import random
imagens = images.images()
sup = superficie.superficie()
musica = music.music()


class gamenew():
    def __init__(self):
        self.window = window.window(800,600,"Jogo",imagens.back,musica.menu,0)
        self.window.setBack(imagens.back,(0,0))
        self.fonte = pygame.font.SysFont("comicsans",24,True)
        self.main()
    def main(self):
        RunOn = True 
        frames = pygame.time.Clock()
        esta_tocando = True
        sound = imagens.soundOn 
        esc_down = True
        desenharp = True
        x = 350
        pos_letra_certa = []
        self.window.music_on(esta_tocando,musica.menu)
        restart = True
        letra = []
        letra.append(self.fonte.render("",1,(255,0,0)))
        cont = 13
        text1 = self.fonte.render('',1,(255,0,0))
        a = 1
        dig = []
        existe = False
        let = ''
        full = []
        letras_digitadas_palavra = []
        letras_certas = []
        while RunOn:
            if restart:
                lista=[]
                arquivo=open("palavras.txt", "r") #arquivo com as palavras para escolher
                for i in arquivo:
                    i=i.strip()
                    lista.append(i)
                palavra_escolhida = random.choice(lista) #método para escolha aleatória na lista
                arquivo.close()
                restart = False
                text = self.fonte.render(palavra_escolhida,1,(255,0,0))

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
                                        elif (mouseY >= 317) and (mouseY <= 347):
                                            RunOn = False
                                            esc_down = False
                                                    
                                if (event.type == pygame.KEYDOWN):
                                    if (event.key == pygame.K_ESCAPE):
                                        esc_down = False

                            pygame.display.update()
                        esc_down = True
                    else:
                        letra.append(self.fonte.render(chr(event.key),1,(255,0,0)))
                        let = chr(event.key)
                        # EXATAMENTE AQUI: verificar  se chr(event.key) existe dentro da palavra escolhida, se sim, existe == True
                        if (chr(event.key) in palavra_escolhida):
                            existe = True
                        else:
                            existe = False
                        a =+ 1
                        #self.window.desenharTexto(letra,self.window,500,50)
                        pygame.display.update()
                       
                   
            self.window.redraw(imagens.back,sound,self.window)
            self.window.desenharTexto(text,self.window,200,50) #mostrando a palavra escolhida
            for i in range(a-1, len(letra)): #letras digitadas
                self.window.desenharTexto(letra[i],self.window,500 + cont,50)
                cont += 26
            if (cont != (26*(len(palavra_escolhida)))):
                cont = 1

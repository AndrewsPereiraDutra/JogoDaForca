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


class game():
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
        letras_certas_palavra = []
        con = 0
        cont_erro = 0
        while RunOn:
            if restart:
                lista=[]
                arquivo=open("palavras.txt", "r") #arquivo com as palavras para escolher
                for i in arquivo:
                    i=i.strip()
                    lista.append(i)
                palavra_escolhida = random.choice(lista) #método para escolha aleatória na lista
                for i in range (0,len(palavra_escolhida)):
                    pos_letra_certa.append(0)
                arquivo.close()
                restart = False
                text = self.fonte.render(palavra_escolhida,1,(255,0,0))
                for z in range(0, len(palavra_escolhida)):
                    letras_certas_palavra.append("___")
            frames.tick(30)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    RunOn = False
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    (mouseX,mouseY) = event.pos
                    print(mouseX,mouseY)
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
                        for i in range(0, len(palavra_escolhida)):
                            if (let in palavra_escolhida[i]):
                                existe = True
                                maius = let.upper()
                                letras_certas_palavra[i] = maius
                                
                        if (let not in palavra_escolhida):
                            cont_erro = cont_erro + 1
                            
                        '''if not(existe):
                            cont_erro += 1
                            print(cont_erro)'''
                        


                        #self.window.desenharTexto(letra,self.window,500,50)
                        pygame.display.update()
                       
                   
            self.window.redraw(imagens.back,sound,self.window)
            self.window.desenharTexto(text,self.window,200,50) #mostrando a palavra escolhida
            #  COLOCAR OS RESPECTIVOS CONTS, E PARA CADA UM DELES IMAGEM, MUDANDO SO O NOME NA HORA DE CHAMAR ELA
            if (cont_erro >= 1):
                self.window.desenha(imagens.cabeca, 213 - 65,312)
                #pygame.display.update()
            for i in range(0, len(letra)): #letras digitadas
                self.window.desenharTexto(letra[i],self.window,500 + cont,50)
                cont += 26
            if (cont != (26*(len(palavra_escolhida)))):
                cont = 1
            
            for y in letras_certas_palavra:
                t = self.fonte.render(y,1,(255,0,0))
                self.window.desenharTexto(t,self.window, 300 + con, 400)
                con += 60
            con = 0
 
            pygame.display.update()
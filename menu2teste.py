import pygame 
import menu
import window
import imagens
import musicas
import random #biblioteca randômica



class jogador():
    def __init__(self,letras_chutadas):
        self.letras_chutadas = letras_chutadas
    
    def getletras_chutadas(self):
        return self.letras_chutadas

    def setletras_chute(self,letras_chutadas):
        self.letras_chutadas = letras_chutadas
    
    def chute_letras(self):
        self.setletras_chute(str(input("Qual letra existe nesta palavra? ")))
    
    def chute_letras_repetido(self):
        self.setletras_chute(str(input("Letra repetida - Digite outra? ")))

class palavra():
    def __init__(self,descobrir):
        self.descobrir = descobrir

    def getpalavras_descobrir(self):
        return self.descobrir
    
class boneco():
    def __init__(self,partes_corpo_forca):
        self.partes_corpo = partes_corpo_forca

    def getcorpo_boneco(self):
        return self.partes_corpo
    
    def setcorpo_boneco(self,corpo):
        self.partes_corpo = corpo

def main_game():
    print("Entrou")
    lista=[]
    arquivo=open("palavras.txt", "r") #arquivo com as palavras para escolher
    for i in arquivo:
        i=i.strip()
        lista.append(i)
    palavra_escolhida = palavra(random.choice(lista))#objeto palavra escolhida
    arquivo.close()

    word=[]
    for i in palavra_escolhida.getpalavras_descobrir():
        i=i.upper()
        word.append(i)
    print(word)#print provisório para ver a palavra escolhida pela biblioteca random

    boneco_atual = boneco("")
    partes_boneco = ["Cabeça","Tronco","Braço direito", "Braço esquerdo","Perna direita","Perna esquerda"] #lista das partes do corpo para eliminação


    print("")
    print("*_____Jogo da Forca_____*")
    print("")

    descoberta = []
    for i in range (0,len(word)):
        descoberta.append("__ ")

    digitadas = []
    letras_chutadas_jogo = jogador("")
    acertou = False #condição booleana para terminar o jogo
    while acertou == False:
        print("")
        letras_chutadas_jogo.chute_letras()
        letras_chute = letras_chutadas_jogo.getletras_chutadas().upper()
        if letras_chute not in digitadas:
            digitadas.append(letras_chute)
        else:
            while letras_chute in digitadas:
                letras_chutadas_jogo.chute_letras_repetido()
                letras_chute = letras_chutadas_jogo.getletras_chutadas().upper()
            digitadas.append(letras_chute)   
        print("")
        print("Letras Digitadas")
        for i in range(0,len(digitadas)):
            print(digitadas[i], end=" ")
        print("\n")
        cont=0
        for i in range (0,len(word)):
            if letras_chute == word[i]:
                descoberta[i] = letras_chute
                cont=cont+1
            print(descoberta[i], end="")
        print("")
        acertou = True
        
        for i in range (0,len(descoberta)):
            if descoberta[i] == "__ ":
                acertou = False

        if cont == 0:
            boneco_atual.setcorpo_boneco(partes_boneco[0])
            print("Você errou!!! Coloca a "+boneco_atual.getcorpo_boneco()+" na forca")
            cont=0
            partes_boneco.pop(0)
            if len(partes_boneco) == 0:
                print("GameOver!!!")
                acertou = True
        
        if "__ " not in descoberta:
            print("Parabéns Você Ganhou!!! ")

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
                           main_game()                           
                           self.RunOn = False 


                        if (self.yMouse >= 299 and self.yMouse <= 369):
                           print("ok") 

                        if (self.yMouse >= 421 and self.yMouse <= 489):
                            self.RunOn = False

            pygame.display.update()

menu()

        


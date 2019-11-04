import pygame
import window
import imagens
import cores
import jogo

imagens = imagens.imagens()
cores = cores.cores()

def menu():
    xwindow = 800
    ywindow = 600
    title = "Jogo"
    background = imagens.menu       #diretorio da imagem (imagens.menu)
    music = 0                       #diretorio da musica
    music_status = 0                #True or false
    music_img = 0                   #imagens.musica
    img_pos = (0,0)                 # Estenda a imagem da posição zero X e zero Y
    frames = pygame.time.Clock()    #fps (cria um objeto para ajudar a controlar o tempo)
    window_menu = window.windows(xwindow,ywindow,title,background,music,music_status,music_img,img_pos)

    RunOn = True 
    #Main Loop
    while RunOn:
        frames.tick(27)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): #Sair
                RunOn = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                (xMouse,yMouse) = event.pos #Posiçao do mouse eixo X e Y
                print("x: "+str(xMouse))
                print("y: "+str(yMouse))
                if (xMouse >= 251 and xMouse <= 548):
                    if (yMouse >= 179 and yMouse <= 244):
                        jogo.main_game()                         
                        RunOn = False 


                    if (yMouse >= 299 and yMouse <= 369):
                        print("ok") 

                    if (yMouse >= 421 and yMouse <= 489):
                        RunOn = False

        pygame.display.update()

menu()

        


import pygame
import janela
import imagens
import cores
import jogo
imagens = imagens.imagens()
cores = cores.cores()
pygame.init()

def menu():    
    RunOn = True 
    #Main Loop
    frames = pygame.time.Clock()
    while RunOn:      
        frames.tick(27)
        janela.janela(imagens.menu,0,0)
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

        


import random #biblioteca randômica
lista=[]
arquivo=open("palavras.txt", "r") #arquivo com as palavras para escolher
for i in arquivo:
    i=i.strip()
    lista.append(i)
palavra_escolhida = random.choice(lista) #método para escolha aleatória na lista
arquivo.close()

palavra=[]
for i in palavra_escolhida:
    i=i.upper()
    palavra.append(i)
print(palavra)#print provisório para ver a palavra escolhida pela biblioteca random

descoberta = []
boneco = ["Perna direita","Perna esquerda","Braço direito", "Braço esquerdo", "Cabeça"] #lista das partes do corpo para eliminação
digitadas = []

print("")
print("*_____Jogo da Forca_____*")
print("")

for i in range (0,len(palavra)):
    descoberta.append("__ ")

acertou = False #condição booleana para terminar o jogo
while acertou == False:
    print("")
    letra = input("Qual letra existe nesta palavra? ")
    letra = letra.upper()
    if letra not in digitadas:
        digitadas.append(letra)
    else:
        while letra in digitadas:
            letra = input("Letra já informada - Digite outra... ")
            letra = letra.upper()
        digitadas.append(letra)   
    print("")
    print("Letras Digitadas")
    for i in range(0,len(digitadas)):
        print(digitadas[i], end=" ")
    print("\n")
    cont=0
    for i in range (0,len(palavra)):
        if letra == palavra[i]:
            descoberta[i] = letra
            cont=cont+1
        print(descoberta[i], end="")
    print("")
    acertou = True
    
    for i in range (0,len(descoberta)):
        if descoberta[i] == "__ ":
            acertou = False

    if cont == 0:
        print("Você errou!!! corta a "+boneco[0])
        cont=0
        boneco.pop(0)
        if len(boneco) == 0:
            print("GameOver!!!")
            acertou = True
    
    if "__ " not in descoberta:
        print("Parabéns Você Ganhou!!! ")

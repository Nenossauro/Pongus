from ast import Return, Try
from cmath import rect
from operator import truediv
from random import randint
from re import I
import mysql.connector
import pygame,sys
from pygame.locals import *
from pygame.rect import *
import time


#mydb = mysql.connector.connect(host = "localhost",user = "root",password = "",database="pongus")
#mycursor = mydb.cursor()
  

def main():
    pygame.init()
    
    fre = randint(1,3)

    acc = 2
    acy = 2
    p = 0
    x = 5
    y = 150
    velocity = 10
    
    xc = 250
    yc = 200
    velocitycx = 10
    velocitycy = randint(-5,5) #3 

    acc2 = 1.5
    p2 = 0
    x2 = 471
    y2 = 140
    velocity2 = 10

    
    i = 1 
    while i < 3:
        chave = randint(0,1)
        if chave == 0:
                ballsd = True #randint(0,1)
        elif chave ==1:
                ballsd = False
        lsd = randint(0,1)
        
        i += i
    

    bgsong = pygame.mixer.Sound('sound/bgmusic.mp3')
    bgsong.play()
    screen = pygame.display.set_mode((500,400),0,32)
    pygame.display.set_caption("Pongus")
    myfont = pygame.font.SysFont("monospace", 15)
    white = (0,0,0)
    black = (0,0,0)
    
    colisionsound = pygame.mixer.Sound('sound/colision.mp3')


    colis = 0
    rodas = 1
    

    rodar = True
    
    while rodar == True:
        
        cafe = pygame.image.load("img/cafe.jpg")
        area = pygame.Rect(200,250,400,500)
        screen.blit(cafe,(0,0))

        #inicio/restar do jogo
        if ballsd == False:
            
            xc += velocitycx*-1

        if ballsd == True:
           
            xc += velocitycx*-1
        if xc > 500:
            sql = "INSERT INTO tb_dados2(rodada,pontol,pontor,colisoes,vl,vr,vcx,vcy) VALUES("+str(rodadas)+","+str(pontos1)+","+str(pontos2)+","+str(colisoes)+","+str(velocidadeesque)+","+str(velocidadedirei)+","+str(velocidadebolax)+","+str(velocidadebolay)+")"
        
            #mycursor.execute(sql)
            #mydb.commit()
            velocity *= -1
            y +=velocity 
            lsd = randint(0,1)
            rodas = rodas+1
            p = p+1
            xc = 250
            yc = 200
            x = 5
            y = 150 
            if velocity > 0:
                velocity = velocity+acc
            if velocity < 0:
                velocity = (velocity*(-1))+acc
            if velocity2 > 0 and velocity2 <= 6 and velocity2 <= -6:
                velocity2 = velocity2-fre
            if velocity2 < 0 and velocity2 <= 6 and velocity2 <= -6:
                velocity2 = (velocity2*(-1))-fre
            if velocity2 == 0:
                velocity2 = 10
            velocitycy = randint(-5,5)  #3 
            x2 = 471
            y2 = 150
            velocitycx = velocitycx*-1
            
        if xc < 0:
            sql = "INSERT INTO tb_dados2(rodada,pontol,pontor,colisoes,vl,vr,vcx,vcy) VALUES("+str(rodadas)+","+str(pontos1)+","+str(pontos2)+","+str(colisoes)+","+str(velocidadeesque)+","+str(velocidadedirei)+","+str(velocidadebolax)+","+str(velocidadebolay)+")"
        
            #mycursor.execute(sql)
            #mydb.commit()
            rodas = rodas+1
            velocity2 *= -1
            y2 +=velocity2
            lsd = randint(0,1)
            p2 = p2+1
            xc = 250
            yc = 200
            x = 5
            y = 150
            if velocity2 > 0:
                velocity2 = velocity2+acc2
            if velocity2 < 0:
                velocity2 = (velocity2*(-1))+acc2
            if velocity > 0:
                velocity = velocity-fre
            if velocity < 0:
                velocity = (velocity*(-1))-fre
            if velocity == 0:
                velocity = 10
            velocitycy = randint(-5,5) #3 
            x2 = 471
            y2 = 150
            velocitycx = velocitycx*-1


        #só sobre os objetos na tela
        rect1 =  pygame.Rect(x,y,24,100)
        rect2 =  pygame.Rect(x2,y2,24,100)
        
        pygame.draw.circle(screen,white,(xc,yc),10,10)
       
        
        amogus = pygame.image.load("img/amogus.png")
        sprite = pygame.Surface((500,400))
        
        pygame.draw.rect(screen,white,rect1)
        pygame.draw.rect(screen,white,rect2)
        screen.blit(amogus,(xc,yc))
        

        #colisão
        collidel = Rect.collidepoint(rect1,xc,yc)
        collider = Rect.collidepoint(rect2,xc,yc)
        collidel2 = Rect.collidepoint(rect1,xc,yc)
        collider2 = Rect.collidepoint(rect2,xc,yc)

        #y += velocity
        #y2 += velocity2
        
        yc += velocitycy


        #só sobre os textos na tela


        #pontos
        labelp = myfont.render("Pontos do L: "+str(p), 1, (white)) 
        labelp2 = myfont.render("Pontos do R: "+str(p2), 1, (white))
        #screen.blit(labelp,(30,65))
        #screen.blit(labelp2,(307,65))

        #posição
        label = myfont.render("Y do L: "+str(int(y)), 1, (white))
        labelxc = myfont.render("Y do C: "+str(int(yc)),1,(white))
        labelc = myfont.render("X do C: "+str(int(xc)), 1, (white))     
        label2 = myfont.render("Y do R: "+str(int(y2)), 1, (white))
        #screen.blit(labelxc,(150,265))
        #screen.blit(label,(30,85))
        #screen.blit(label2,(307,85))
        #screen.blit(labelc,(150,285))

        #velocidade
        labelv = myfont.render("Velocidade do L: {0:.1f}".format(velocity), 1, (white)) 
        labelv2 = myfont.render("Velocidade do R: {0:.1f}".format(velocity2), 1, (white)) 
        labelvc = myfont.render("Velocidade do X do C: {0:.1f}".format(velocitycx),1,(white))
        labelvcy = myfont.render("Velocidade de Y do C {0:.1f}".format(velocitycy),1,(white))
        #screen.blit(labelv,(30,105))
        #screen.blit(labelv2,(307,105))
        #screen.blit(labelvc,(150,300))
        #screen.blit(labelvcy,(150,315))

        #eu vou me matar
        labelrod = myfont.render("Rodada: "+str(rodas),1,(white))
        labelcol = myfont.render("Colisões: "+str(colis),1,(white))
        labelsd = myfont.render("Sd da rodada: "+str(lsd), 1, (white)) 
        labelsdc = myfont.render("Sd do C: "+str(ballsd),1,(white))
        
        #screen.blit(labelrod,(180,45))
        #screen.blit(labelsd,(180,10))
        #screen.blit(labelcol,(180,30))
        #screen.blit(labelsdc,(150,335))
        


        #só sobre a bola
       
        
        
        
        if collidel or collidel2:
                colisionsound.play()
                
                colis = colis +1 
                velocitycx = -10
                velocitycy += acy
                velocitycx += acc
               
                
                
        
        if collider or collider2:
                colisionsound.play()
                
                colis = colis +1
                velocitycx = 10
                velocitycy += acy*-1
                velocitycx += acc
                
        if yc < 10 or yc > 390:            
            velocitycy *= -1
        #if pygame.key.get_pressed()[K_y] and yc >=10:
            #yc -= velocitycy   
        #if pygame.key.get_pressed()[K_h] and yc <=390:
            #yc += velocitycy
       
            
        

        #só sobre o movimento das barras
        
        if lsd == 1:
            velocity == 10
            velocity2 == -10
        elif lsd == 0:
            velocity == -10
            velocity2 == 10

        #if y <=10:
        if pygame.key.get_pressed()[K_w] and y >=10:
                      
            #velocity *= -1
            y -= velocity
            
        #if y >= 300:
        if pygame.key.get_pressed()[K_s] and y <=300: 
            #velocity *= -1
            y += velocity
            
        #if y2 <= 10:
        if pygame.key.get_pressed()[K_UP] and y2 >=10:             
            #velocity2 *= -1
            y2 -= velocity2
        #if y2 >= 300:
        if pygame.key.get_pressed()[K_DOWN] and y2 <=300: 
            #velocity2 *= -1
            y2 += velocity2
            
        
        #nada de importante

        pontos1 = p
        pontos2 = p2
        rodadas = rodas
        colisoes = colis
        velocidadeesque = velocity
        velocidadedirei = velocity2
        velocidadebolax = velocitycx
        velocidadebolay = velocitycy

        


        pygame.display.update()
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
                
    
    





main()

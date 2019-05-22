from pygame import*
from random import*
from pprint import*

size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

board=[[randint(1,2) for i in range(7)] for j in range(7)]

backPic=image.load("images/background 1.png")
screen.blit(backPic,(0,0))

def checkHor(b,val):
    for r in range(7):#there are 7 rows
        for c in range(4):#start at c 0,1,2,3
            if b[r][c]==b[r][c+1]==b[r][c+2]==b[r][c+3]==val:
                return True
    return False

def checkVer(b,val):
    
    for r in range(4):#start at row 0,1,2,3
        for c in range(7):#columns 0-6
            if b[r][c]==b[r+1][c]==b[r+2][c]==b[r+3][c]==val:
                return True
    return False

def checkD1(b,val):
    for r in range(4):#start at row 0,1,2,3
        for c in range(4):#columns 0-3
            if b[r][c]==b[r+1][c+1]==b[r+2][c+2]==b[r+3][c+3]==val:
                return True
    return False

def checkD2(b,val):
    for r in range(4):#start at row 0,1,2,3
        for c in range(3,7):#columns 3,4,5,6
            if b[r][c]==b[r+1][c-1]==b[r+2][c-2]==b[r+3][c-3]==val:
                return True
    return False



def connect4(b,val):
    return checkHor(b,val) or checkVer(b,val) or checkD1(b,val) or checkD2(b,val)

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    pprint(board)
    print(connect4(board,1))
    print(connect4(board,2))
    display.flip() 

quit()



'''#sideShooter.py
from pygame import *
from math import *
screen=display.set_mode((800,600))
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)
WHITE=(255,255,255)

MAXRAPID=6

rapid=MAXRAPID

enemies=[[600,400,10],[700,300,7],[650,450,15]]

shooter=[50,300]
        # x   y  hs  vs
bullets=[]

 #hs vs
v=[5,0]

def drawScene(screen,p,bull,targ):
    screen.fill(BLACK)
    draw.circle(screen,GREEN,p,20)
    #drawing the bullets here
    for b in bull:
        draw.circle(screen,GREEN,(b[0],b[1]),4)
    for t in targ:
        draw.circle(screen,RED,(t[0],t[1]),t[2])
    display.flip()

def moveBullets(bull):
    for b in bull:
        b[0]+=b[2]#horiz movement
        b[1]+=b[3]#vert movement
        if b[0]>800:
            bull.remove(b)#removing "off-screen" bullets


def checkHits(bull,targ):
    for b in bull:
        for t in targ:
            d=sqrt((b[0]-t[0])**2+(b[1]-t[1])**2)
            if d<4+t[2]:
                bull.remove(b)
                targ.remove(t)
                
        
myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    mx,my=mouse.get_pos()
    shooter[1]=my#vertical movement (shooter)

    

    keys=key.get_pressed()
    if keys[32] and rapid==MAXRAPID:
        rapid=0
        bullets.append([shooter[0]+20,shooter[1],v[0],v[1]])

    if rapid<MAXRAPID:
        rapid+=1
    
    
    moveBullets(bullets)
    checkHits(bullets,enemies)
    drawScene(screen,shooter,bullets,enemies)
    myclock.tick(60)
quit()


'''

















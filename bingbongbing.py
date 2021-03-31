import pygame, sys
from pygame.locals import *
import random
WHITE=(255,255,255)
BLUE=(0,0,255) # rectangle
RED=(255,0,0) # circle
GREEN=(0,255,0) # triangle
CYAN=(0,255,255) # square
PREVIOUSPOS=[]
def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption("Work...")


    DISPLAY.fill(WHITE)


    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                drawRandom(DISPLAY)
            if event.type==KEYUP:
                if event.key==pygame.K_BACKSPACE:
                    DISPLAY.fill(WHITE)
                    PREVIOUSPOS.clear()
                elif event.key==pygame.K_RETURN:
                    pygame.image.save(DISPLAY, "output.jpg")
                else:
                    drawRandom(DISPLAY)
        pygame.display.update()

def bingbongrect(surfcae):
    pygame.draw.rect(surfcae,BLUE,(random.randrange(0, 500),random.randrange(0, 400),random.randrange(100, 250), random.randrange(50, 150)))
def bingbongcircle(surface):
    size = random.randrange(50, 100)
    pygame.draw.circle(surface,RED, (random.randrange(0, 500),random.randrange(0, 400)), size,size)
def bingbongsquare(surface):
    size = random.randrange(100, 200)
    pygame.draw.rect(surface,CYAN,(random.randrange(0, 500),random.randrange(0, 400),size,size))
def bingbongtriangle(surface):
    original = random.randrange(0, 400)
    originalx = random.randrange(0, 500)
    for i in range(len(PREVIOUSPOS)):
        if original >= i + 15 and original <= i - 15:
            return bingbongtriangle(surface)
    pygame.draw.polygon(surface, GREEN, ((originalx+100,original+100), (originalx,original+50), (originalx+100,original)))
    PREVIOUSPOS.append(original)
    print(PREVIOUSPOS)
def drawRandom(poo):
    wackydacky = random.randrange(0, 4)
    if wackydacky == 1:
        bingbongrect(poo)
    elif wackydacky == 2:
        bingbongcircle(poo)
    elif wackydacky == 3:
        bingbongtriangle(poo)
    else:
        bingbongsquare(poo)
    
main()
#Required packages: time, threading, pygame (sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python-pygame)
#----Imports----
from time import sleep
import pygame.surface
import pygame.camera
import pygame.display
import threading as th
#----End Imports----
#---Setup----
pygame.init()
pygame.camera.init()
Draw = pygame.Surface([160, 120])
Display = pygame.display.set_mode((160, 120))
cam = pygame.camera.Camera("/dev/video0",(160, 120))
cam.start()
#----End Setup----
minOrange = (20, 70, 85)
maxOrange = (30, 100, 100)
#----4 Threads (= TopLeft, TopRight, BottomL, BottomR) (= Faster)----
def FindTL(Img):
    for y in range(0, 60, 5):
        for x in range(0, 80, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):  
                Draw.set_at((x, y), maxOrange)

def FindTR(Img):
    for y in range(0, 60, 5):
        for x in range(80, 160, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):
                Draw.set_at((x, y), maxOrange)

def FindBL(Img):
    for y in range(60 , 120, 5): 
        for x in range(0 , 80, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):  
                Draw.set_at((x, y), maxOrange)

def FindBR(Img):
    for y in range(60, 120, 5):
        for x in range(80, 160, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):
                Draw.set_at((x, y), maxOrange)
#----End 4 Threads----
#----Clear The Pixels from the Img----
def Clear():
    Draw.fill([0, 0, 0])
#----End Clear The Pixels from the Img----
#----Show the Img----
def Show(Img):
    Display.blit(Img, (0, 0))
    pygame.display.update()
#----End Show the Img----
#----Start the 4 Threads----
def Thread(Img):
    import threading as th
    tTL = th.Thread(target = FindTL, args = (Img,))
    tTR = th.Thread(target = FindTR, args = (Img,))
    tBL = th.Thread(target = FindBL, args = (Img,))
    tBR = th.Thread(target = FindBR, args = (Img,))
    tTL.start()
    tTR.start()
    tBL.start()
    tBR.start()
#----End Start the 4 Threads----
#----Take a picture and return it----
def Pic():
    return cam.get_image()
#----End Take a picture and return it----
#----Calibrate the Ball Color----
def Calibrate():
    import pygame.key
    import pygame.event
    import pygame.color
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p = Pic()
                r = pygame.draw.rect(p, (255, 0, 0), [65, 45, 30, 30], 3)
                Show(p)
                sleep(3)
                Col = pygame.transform.average_color(p, r)
                minOrange = pygame.Color(Col[0] - 15, Col[1] - 20, Col[2] - 20).hsva
                maxOrange = pygame.Color(Col[0] + 15, Col[1] + 20, Col[2] + 20).hsva
                print "new min. Orange: " + str(minOrange)
                print "new max. Orange: " + str(maxOrange)
#----End Calibrate the Ball Color----
#----The Actual Program----
if(__name__ == "__main__"):
    while True:
        Calibrate()
        Clear()
        Thread(Pic())
        Show(Draw)
#----End The Actual Program----

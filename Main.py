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
gameDisplay = pygame.display.set_mode((160, 120))
cam = pygame.camera.Camera("/dev/video0",(160, 120))
cam.start()
#----End Setup----
#----Start User Parametes----
minOrange = (20, 70, 85)
maxOrange = (30, 100, 100)
#----End User Parameters-----
#----4 Threads (= TopLeft, TopRight, BottomL, BottomR) (= Faster)----
def FindTL(Img):
    for y in range(60):
        for x in range(80):
            if(y % 2 ==  x % 2 and minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):  
                Draw.set_at((x, y), (255, 124, 0))

def FindTR(Img):
    for y in range(60):
        for x in range(80):
            x_new = x + 80
            if(y % 2 == x_new % 2 and minOrange[0] <= Img.get_at((x_new, y)).hsva[0] and maxOrange[0] >= Img.get_at((x_new, y)).hsva[0]):
                Draw.set_at((x_new, y), (255, 124, 0))

def FindBL(Img):
    for y in range(60):
        y_new = y + 60
        for x in range(80):
            if(y_new % 2 == x % 2 and minOrange[0] <= Img.get_at((x, y_new)).hsva[0] and maxOrange[0] >= Img.get_at((x, y_new)).hsva[0]):  
                Draw.set_at((x, y_new), (255, 124, 0))

def FindBR(Img):
    for y in range(60):
        y_new = y + 60
        for x in range(80):
            x_new = x + 80
            if(y_new % 2 == x_new % 2 and minOrange[0] <= Img.get_at((x_new, y_new)).hsva[0] and maxOrange[0] >= Img.get_at((x_new, y_new)).hsva[0]):
                Draw.set_at((x_new, y_new), (255, 124, 0))
#----End 4 Threads----
#----Clear The Pixels from the Img----
def Clear():
    Draw.fill([0, 0, 0])
#----End Clear The Pixels from the Img----
#----Show the Img----
def Show(Img):
    gameDisplay.blit(Draw, (0, 0))
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
#----The Actual Program----
if(__name__ == "__main__"):
    while True:
        Clear()
        Thread(Pic())
        Show(Draw)
#----End The Actual Program----

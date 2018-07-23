#Required packages: time, threading, pygame (sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python-pygame)
#----Use GUI?----
GUI = True
#----End Use GUI?----
#----Imports----
import pygame.surface
import pygame.camera
import pygame.display
import threading as th
#----End Imports----
#---Setup----
pygame.init()
pygame.camera.init()
if(GUI):
    Draw = pygame.Surface([160, 120])
    Display = pygame.display.set_mode((160, 120))
cam = pygame.camera.Camera("/dev/video0",(160, 120))
cam.start()
minOrange = (20, 70, 85)
maxOrange = (30, 100, 100)
Found = []
#----End Setup----
#----4 Threads (= TopLeft, TopRight, BottomL, BottomR) (= Faster)----
def FindTL(Img):
    for y in range(0, 60, 5):
        for x in range(0, 80, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):  
                if(GUI):
                    Draw.set_at((x, y), maxOrange)
                Found.append((x, y))

def FindTR(Img):
    for y in range(0, 60, 5):
        for x in range(80, 160, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):
                if(GUI):
                    Draw.set_at((x, y), maxOrange)
                Found.append((x, y))

def FindBL(Img):
    for y in range(60 , 120, 5): 
        for x in range(0 , 80, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):  
                if(GUI):
                    Draw.set_at((x, y), maxOrange)
                Found.append((x, y))

def FindBR(Img):
    for y in range(60, 120, 5):
        for x in range(80, 160, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):
                if(GUI):
                    Draw.set_at((x, y), maxOrange)
                Found.append((x, y))

#----End 4 Threads----
#----Clear The Pixels from the Img----
def Clear():
    if(GUI):
        Draw.fill([0, 0, 0])
    Found = []
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
#----The Actual Program----
if(__name__ == "__main__"):
    while True:
        if(GUI):
            Clear()
        Thread(Pic())
        if(GUI):
            Show(Draw)
        else:
            print(Found)
#----End of The Actual Program----

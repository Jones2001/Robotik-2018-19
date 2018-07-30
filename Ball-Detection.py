
GUI = True

import pygame.surface
import pygame.camera


pygame.init()
pygame.camera.init()
if(GUI):
    import pygame.display
    Draw = pygame.Surface([160, 120])
    Display = pygame.display.set_mode((160, 120))
cam = pygame.camera.Camera("/dev/video0",(160, 120))
cam.start()
minOrange = (20, 70, 85)
maxOrange = (30, 100, 100)
Found = []

def FindTL(Img):
    for y in range(0, 60, 5):
        for x in range(0, 80, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):  
                Found.append((x, y))

def FindTR(Img):
    for y in range(0, 60, 5):
        for x in range(80, 160, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):
                Found.append((x, y))

def FindBL(Img):
    for y in range(60 , 120, 5): 
        for x in range(0 , 80, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):  
                Found.append((x, y))

def FindBR(Img):
    for y in range(60, 120, 5):
        for x in range(80, 160, 5):
            if(minOrange[0] <= Img.get_at((x, y)).hsva[0] and maxOrange[0] >= Img.get_at((x, y)).hsva[0]):
                Found.append((x, y))


def Clear():
    if(GUI):
        Draw.fill([0, 0, 0])
    

def Show(Img):
    Display.blit(Img, (0, 0))
    pygame.display.update()

def Thread(Img):
    import threading as th
    if(Img is not None):
        tTL = th.Thread(target = FindTL, args = (Img,))
        tTR = th.Thread(target = FindTR, args = (Img,))
        tBL = th.Thread(target = FindBL, args = (Img,))
        tBR = th.Thread(target = FindBR, args = (Img,))
    else:
        raise ValueError
    try:
        tTL.start()
        tTR.start()
        tBL.start()
        tBR.start()
    except th.ThreadError:
        raise th.ThreadError

def Pic():
    if(cam.get_image() is not None):
        return cam.get_image()
    else:
        raise ValueError 

def Edit(Img, Found):
    try:    
        for i in range(len(Found)):
            pygame.draw.line(Img, (209, 109, 33), Found[i], Found[i + 1])
    except IndexError, ValueError:
        pass

if(__name__ == "__main__"):
    while True:
        Found = []    
        if(GUI):
            Clear()
        Thread(Pic())
        Edit(Draw, Found)
        if(GUI):
            Show(Draw)
        else:
            print(Found)


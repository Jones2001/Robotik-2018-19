
GUI = True

import pygame.surface
import pygame.camera

pygame.init()
pygame.camera.init()
if(GUI):
	import pygame.display
	Draw = pygame.Surface([160, 120])
	Display = pygame.display.set_mode((160, 120))
	Overlay = pygame.image.load("overlay.png")
cam = pygame.camera.Camera("/dev/video0",(160, 120))
cam.start()

Threshold = 10
minOrange = (20, 70, 85)
maxOrange = (30, 100, 100)
Found = []
LastPosition = None

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

def Show(Img, Ovl):
	Display.blit(Img, (0, 0))
	Display.blit(Ovl, (0, 0))
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
	if(GUI):
		try:    
			if(len(Found) > Threshold):
				for i in range(len(Found)):
					pygame.draw.line(Img, (209, 109, 33), Found[i], Found[i + 1])
		except IndexError:
			pass

def Eval(Found):
	try:
		x = int(round(Found[len(Found) / 2][0] / 1.6))
		if(GUI):
			print "| " + str(x) + "% | " + str(100 - x) + "% |"
		return (x, 100 - x)
	except IndexError:
		pass
	except ValueError as V:
		raise V("Variable is a " + type(Found[len(Found) / 2]) + ", not a touple!")

def GetLastPos(Found):
	if(len(Found) > Threshold):
		try:
			LastPosition = (Found(len(Found) / 2)[0], Found(len(Found / 2))[1])
		except IndexError:
			pass
		except ValueError as V:
			raise V("Variable is a " + type(Found[len(Found) / 2]) + ", not a touple!")

def FindAgain(LastPos):
	if(LastPos[0] > 10):
		return "L"
	elif(LastPos[0] < 150):
		return "R"
	elif(LastPos[1] > 10):
		return "T"
	elif(LastPos[1] < 110):
		return "B"
	


def GPIO():
	pass
		
if(__name__ == "__main__"):
	while True:
		Found = []    
		Clear()
		Thread(Pic())
		GetLastPos(Found)
		if(GUI):
			Edit(Draw, Found)
		Eval(Found)
		if(GUI):
			Show(Draw, Overlay)
			print(Found)
			print(LastPosition)


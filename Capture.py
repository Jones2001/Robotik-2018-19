# -*- coding: utf-8 -*-
#@author Jonas Mohr

import pygame.camera, Errors 



def CaptureFrame(cam):
    if(cam.getImage() is not None):
        return cam.getImage()
    else:
        raise Errors.EmptyCaptureException


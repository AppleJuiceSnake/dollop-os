import pygame
import os
import sys

#To add more colors, go to www.colorschemer.com/online.html or another color palette
# with the ability to see the RGB values. Then fork the Github Repo and modify 
# this file and johnnyw3 or I will decide on whether your changes are acceptable.

# Colors
black = (0,0,0)
white = (255,255,255)
brown = (100,42,42)
gray = (128,128,128)
darkdarkred = (64,0,0)
rhubarb = (128,0,0)
red = (255,0,0)
redorange = (255,64,0)
orange = (255,128,0)
orangeyellow = (255,192,0)
yellow = (255,255,0)
limegreen = (192,255,0)
screengreen = (128,255,0)
lightgreen = (64,255,0)
green = (0,255,0)
mehgreen = (0,255,64)
greenblue = (0,255,128)
aqua = (0,255,192)
lightblue = (0,255,255)
turquoise = (0,192,255)
teal = (0,128,255)
lightdarkblue = (0,64,255)
blue = (0,0,255)
darkblue = (64,0,255)
purple = (128,0,255)
violet = (192,0,255)
magenta = (255,0,255)
darklightmagenta = (255,0,192)
pink = (255,0,128)
lightred = (255,0,64)

#Constants
logo = pygame.image.load('res/logo.png')
bg = pygame.image.load('res/placeholder.png')
menu = pygame.image.load('res/menu_icon.png')
tskbar = pygame.image.load('res/taskbar.png')
scr_width = 320
scr_height = 480
fullscr = False

# Text Functions
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def display_text(text,size,xloc,yloc):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (xloc,yloc)
    gameDisplay.blit(TextSurf, TextRect)

#Speed Control
clock = pygame.time.Clock()
defaultSpeed = 60
currentSpeed = defaultSpeed
def setSpeed(speed):
    try:
        speed += 0
        currentSpeed = speed
    except TypeError:
        print "HEY! THE SPEED IN setSpeed() IS SUPPOSED TO BE A NUMBER!"
def getSpeed():
    return currentSpeed

x = 440
y = 1

#Main Loop
def mainLoop():
    while True:
        for event in pygame.event.get():
	    if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
   		if mouse[0] < 40:
                    if mouse[0] > 0:
                        if mouse[1] < 480:
                            if mouse[1] > 440:
                                print "Button Pressed"
	    if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    pygame.display.flip()
    clock.tick(currentSpeed)
    pygame.draw.rect(gameDisplay, red,(550,450,100,50))

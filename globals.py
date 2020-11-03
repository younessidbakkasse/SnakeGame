# external modules
import pygame, random, sys
from pygame.math import Vector2


# Global variables 
# The display is a grid with 10px cell size
cellWidth = 15
cellNumber = 34
displayWidth = cellNumber/2 * cellWidth
displayHeight = cellNumber * cellWidth

# Color Palette
objectColor = (245, 245, 245)
backgroundColor = (0, 190, 105)
foodColor = (200, 30, 30)

# init all pygame modules 
pygame.init()
frameRates = pygame.time.Clock()
display = pygame.display.set_mode((int(displayWidth), int(displayHeight)))

# Game font
mainFont = pygame.font.Font("./assets/Minecraft.ttf", 21)

# Naming the game
pygame.display.set_caption("Snake Game")

# Time event
timeEvent = pygame.USEREVENT
pygame.time.set_timer(timeEvent, 100)
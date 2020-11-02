import pygame, sys
from menu import *

class Game:
    def __init__(self, cellWidth = 15, cellNumber = 34):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.frame_rates = pygame.time.Clock()
        self.running, self.playing = True, False
        self.START_KEY = False
        self.displayWidth = cellNumber/2 * cellWidth
        self.displayHeight = cellNumber * cellWidth
        self.display = pygame.Surface((int(self.displayWidth), int(self.displayHeight)))
        self.window = pygame.display.set_mode((int(self.displayWidth), int(self.displayHeight)))
        self.gameColors = {
            "objectColor" : (245, 245, 245),
            "backgroundColor" : (0, 190, 105),
            "foodColor" : (200, 30, 30),
            "textColor" : (250, 250, 250)
        }

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.START_KEY = True
            if event.type == pygame.KEYUP:
                self.START_KEY = False

    def gameLoop(self):
        while self.playing:
            self.getEvent()
            if self.START_KEY:
                self.playing = False
                self.display.fill(self.gameColors["foodColor"])
                self.window.blit(self.display, (0, 0))
                pygame.display.update()
            else:
                self.display.fill(self.gameColors["backgroundColor"])
                self.drawText("Click to start", self.displayWidth/2, self.displayHeight/2)
                self.window.blit(self.display, (0, 0))
                pygame.display.update()

    def drawText(self, text, x, y ,size = 20):
        gameFont = pygame.font.Font("./assets/Minecraft.ttf", size)
        textSurface = gameFont.render(text, False, self.gameColors["textColor"])
        textRect = textSurface.get_rect(center = (int(x), int(y)))
        self.display.blit(textSurface, textRect)

game = Game()


while game.running:
    game.playing = True
    game.gameLoop()

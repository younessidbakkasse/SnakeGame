# Modules 
import pygame, sys, random
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

class Snake:
    def __init__(self):
        self.snakeBody = [Vector2(5, 10), Vector2(4,10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.newBodyPart = False
    
    def draw(self):
        for part in self.snakeBody:
            bodyRect = pygame.Rect(int(part.x * cellWidth), int(part.y * cellWidth), cellWidth, cellWidth)
            pygame.draw.rect(display, objectColor, bodyRect)

    def move(self):
        if self.newBodyPart == True:
            newSnakeBody = self.snakeBody[:]
            newSnakeBody.insert(0, self.snakeBody[0] + self.direction)
            self.snakeBody = newSnakeBody[:]
            self.newBodyPart = False
        else:
            newSnakeBody = self.snakeBody[:-1]
            newSnakeBody.insert(0, self.snakeBody[0] + self.direction)
            self.snakeBody = newSnakeBody[:]

    def isGrowing(self):
        self.newBodyPart = True
    
    def reset(self):
        self.snakeBody = [Vector2(5, 10), Vector2(4,10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

class Food:
    def __init__(self):
        self.randomize()

    def draw(self):
        foodRect = pygame.Rect(int(self.pos.x * cellWidth), int(self.pos.y * cellWidth), cellWidth, cellWidth)
        pygame.draw.rect(display, foodColor, foodRect)

    def randomize(self):
        self.x = random.randint(0, cellNumber - 1)
        self.y = random.randint(0, cellNumber - 11)
        self.pos = pygame.Vector2(self.x, self.y)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
    
    def isCollide(self):
        if self.food.pos == self.snake.snakeBody[0]:
            self.food.randomize()
            self.snake.isGrowing()
            # avoiding food overlap snake
            for part in self.snake.snakeBody[1:]:
                while part == self.food.pos:
                    self.food.randomize()

    def update(self):
        self.snake.move()
        self.isCollide()
        self.isOutside()
        self.isEatenSelf()

    def draw(self):
        self.drawBackground()
        self.food.draw()
        self.snake.draw()
        self.score()

    def isOutside(self):
        if not 0 <= self.snake.snakeBody[0].x < cellNumber or not 0 <= self.snake.snakeBody[0].y < cellNumber - 10: 
            self.gameOver()
    
    def isEatenSelf(self):
        for part in self.snake.snakeBody[1:]:
            if part == self.snake.snakeBody[0]:
                self.gameOver()

    def gameOver(self):
        self.snake.reset()
    
    def score(self):
        score = str(len(self.snake.snakeBody) - 3)
        scoreSurface = mainFont.render(score, False, objectColor)
        scoreSurfaceRect = scoreSurface.get_rect(center = (int(cellWidth/2 + 5), int(cellWidth/2 + 5)))
        display.blit(scoreSurface, scoreSurfaceRect)

    def drawBackground(self):
        display.fill(backgroundColor)

# Naming the game
pygame.display.set_caption("Snake Game")

# Time event
timeEvent = pygame.USEREVENT
pygame.time.set_timer(timeEvent, 100)

# Declaring game
game = Game()

# Snake game loop
while True:
    # Game control and user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == timeEvent:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0, -1) 
            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)  
    
    # Display updating the game
    game.draw()
    pygame.display.flip()
    frameRates.tick(60)
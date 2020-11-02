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
        self.snakeBody = [Vector2(0, 0), Vector2(23, 5), Vector2(0, 0)]
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
        self.snakeBody = [Vector2(8, 18), Vector2(8,19), Vector2(8, 20)]
        self.direction = Vector2(0, 0)

class Food:
    def __init__(self):
        self.randomize()

    def draw(self):
        foodRect = pygame.Rect(int(self.pos.x * cellWidth), int(self.pos.y * cellWidth), cellWidth, cellWidth)
        pygame.draw.rect(display, foodColor, foodRect)

    def randomize(self):
        self.x = random.randint(0, cellNumber/2 - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = pygame.Vector2(self.x, self.y)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.running, self.playing = True, False
        self.START_KEY = False
    
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
        display.fill(backgroundColor)        
        self.food.draw()
        self.snake.draw()
        self.drawText(str(len(self.snake.snakeBody) - 3), 10, 10)

    def isOutside(self):
        if not 0 <= self.snake.snakeBody[0].x < cellNumber/2 or not 0 <= self.snake.snakeBody[0].y < cellNumber: 
            self.snake.reset()
    
    def isEatenSelf(self):
        for part in self.snake.snakeBody[1:]:
            if part == self.snake.snakeBody[0]:
                self.snake.reset()        
    
    def drawText(self, text, x, y ,size = 20):
        gameFont = pygame.font.Font("./assets/Minecraft.ttf", size)
        textSurface = gameFont.render(text, False, objectColor)
        textRect = textSurface.get_rect(center = (int(x), int(y)))
        display.blit(textSurface, textRect)  


# Naming the game
pygame.display.set_caption("Snake Game")

# Time event
timeEvent = pygame.USEREVENT
pygame.time.set_timer(timeEvent, 100)

# Declaring game
game = Game()

# Snake game loop
while game.running:
    display.fill(backgroundColor)
    game.drawText("Click to start", displayWidth/2, displayHeight/2)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.playing = True

    while game.playing:
        # Game control and user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == timeEvent:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.playing = False
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
# Importing Modules 
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
        """ Initialising the snake"""
        self.snakeBody = [Vector2(0, 0), Vector2(23, 5), Vector2(0, 0)]
        self.direction = Vector2(0, 0)
        self.newBodyPart = False
    
    def draw(self):
        """ Drawing snake parts since its made of squares so looping throw them """
        for part in self.snakeBody:
            bodyRect = pygame.Rect(int(part.x * cellWidth), int(part.y * cellWidth), cellWidth, cellWidth)
            pygame.draw.rect(display, objectColor, bodyRect)

    def move(self):
        """ Moves snake by inserting new square to the head """
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
        """ resets the snake to the initial position when game over """
        self.snakeBody = [Vector2(8, 28), Vector2(8,29), Vector2(8, 30)]
        self.direction = Vector2(0, 0)

class Food:
    def __init__(self):
        """ initialise food by calling randomize function """
        self.randomize()

    def draw(self):
        """ draws the food red square to the screen """
        foodRect = pygame.Rect(int(self.pos.x * cellWidth), int(self.pos.y * cellWidth), cellWidth, cellWidth)
        pygame.draw.rect(display, foodColor, foodRect)

    def randomize(self):
        """ randomize the next food position after its been eated by snake """
        self.x = random.randint(0, cellNumber/2 - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = pygame.Vector2(self.x, self.y)


class Game:
    def __init__(self):
        """ creates game object instances """
        self.snake = Snake()
        self.food = Food()
        self.running, self.playing = True, False
    
    def isCollide(self):
        """ checks if snake eats food """
        if self.food.pos == self.snake.snakeBody[0]:
            self.food.randomize()
            self.snake.isGrowing()
            # avoiding food overlap snake
            for part in self.snake.snakeBody[1:]:
                while part == self.food.pos:
                    self.food.randomize()

    def update(self):
        """ update and checks all game collisions """
        self.snake.move()
        self.isCollide()
        self.isOutside()
        self.isEatenSelf()

    def draw(self):
        """ draws everything to the screen """
        display.fill(backgroundColor)        
        self.food.draw()
        self.snake.draw()
        self.drawText(str(len(self.snake.snakeBody) - 3), 10, 15)
        if not self.playing:
            self.drawText("Click to start", displayWidth/2, displayHeight/2)
        

    def isOutside(self):
        """ checks snake collision with borders """
        if not 0 <= self.snake.snakeBody[0].x < cellNumber/2 or not 0 <= self.snake.snakeBody[0].y < cellNumber: 
            self.gameOver()

    def isEatenSelf(self):
        """ check the function name """
        for part in self.snake.snakeBody[1:]:
            if part == self.snake.snakeBody[0]:
                self.gameOver() 

    def gameOver(self):
        """ game over function : well its just for better rganisation """
        self.snake.reset()
        self.playing = False     
    
    def drawText(self, text, x, y ,size = 20):
        """ draws any text i want to the screen """
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
                    game.playing = True
            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)
                    game.playing = True
            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)
                    game.playing = True
            if event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)
                    game.playing = True  
    
    # Display updating the game
    game.draw()
    pygame.display.update()

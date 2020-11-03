from globals import *

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
from globals import *

class Snake:
    """ snake class blueprint """
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
from globals import *

class Food:
    """ apples blueprint methodes and attributes """
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
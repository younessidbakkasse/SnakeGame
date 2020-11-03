from globals import *
from snake import Snake
from food import Food

# game manager class
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

    
    # The next three functions are for better code organisation ------------#
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
    
    def drawText(self, text, x, y ,size = 20):
        """ draws any text i want to the screen """
        gameFont = pygame.font.Font("./assets/Minecraft.ttf", size)
        textSurface = gameFont.render(text, False, objectColor)
        textRect = textSurface.get_rect(center = (int(x), int(y)))
        display.blit(textSurface, textRect) 

    def getEvents(self):
        """ checks all keyboard events and clicks """ 
        # Game control and user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == timeEvent:
                self.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.snake.direction.y != 1:
                        self.snake.direction = Vector2(0, -1) 
                        self.playing = True
                if event.key == pygame.K_DOWN:
                    if self.snake.direction.y != -1:
                        self.snake.direction = Vector2(0, 1)
                        self.playing = True
                if event.key == pygame.K_RIGHT:
                    if self.snake.direction.x != -1:
                        self.snake.direction = Vector2(1, 0)
                        self.playing = True
                if event.key == pygame.K_LEFT:
                    if self.snake.direction.x != 1:
                        self.snake.direction = Vector2(-1, 0)
                        self.playing = True
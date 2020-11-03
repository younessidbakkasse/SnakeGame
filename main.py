# Importing Modules 
from manager import * 

# Declaring game
game = Game()


# Snake game loop
while game.running:
    # Game control and user input
    game.getEvents()
    # Display updating the game
    game.draw()
    pygame.display.update()

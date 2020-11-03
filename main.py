""" This gaame was made by Youness Id Bakkasse : https://github.com/younessidbakkasse
this is my first python oop project, made from a to z, I learned a lot to be honnest
it's was a fantastic experience the game is made for mobile devices if we use kivy framework,
nevertheless I hope u enjoye the build"""


# Importing Modules 
from manager import * 

# Declaring game instance
game = Game()

# Snake game loop
while game.running:
    # Game control and user input
    game.getEvents()
    # Display updating the game
    game.draw()
    pygame.display.update()

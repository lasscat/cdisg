import pygame
import sys

pygame.init()

class Window():

    def __init__(self):

        #screen stuff
        self.w_width = 500
        self.w_height = 500

        #color stuff
        self.color_dark = (54, 57, 63)
        self.light_dark = (64, 68, 75)
        self.color_dark_dark = (32, 34, 37)
        pygame.draw.rect(w)



    def startup(self):
        win = pygame.display.set_mode((self.w_width, self.w_height), pygame.RESIZABLE)
        win.fill(self.color_dark)
        pygame.display.flip()



test = Window()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    test.startup()

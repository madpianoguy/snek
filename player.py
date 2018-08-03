import pygame



class Player:

    def __init__(self,char,colour,keys=[pygame.K_UP,
                                        pygame.K_LEFT,
                                        pygame.K_DOWN,
                                        pygame.K_RIGHT]):
        self.char = char
        self.colour = colour

    def getChar(self):
        return self.char

    def getColour(self):
        return self.colour

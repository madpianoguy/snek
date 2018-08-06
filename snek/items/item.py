import pygame

class Item:

    def __init__(self):
        self.xPos = None
        self.yPos = None
        self.xSize = None
        self.ySize = None
        self.colour = (255,255,255)
        self.screen = None
        self.actual = None

    def __str__(self):
        string = str(self.colour) + ' ' + str(self.getDimensions())
        return string

    def __repr__(self):
        return self.__str__()

    def on_event(self,event):
        pass

    def setPos(self,pos):
        self.xPos,self.yPos = pos

    def setSize(self,size):
        self.xSize,self.ySize = size

    def setColour(self,colour):
        self.colour = colour

    def setScreen(self,screen):
        self.screen = screen
        
    def getDimensions(self):
        return (self.xPos,self.yPos,self.xSize,self.ySize)

    def getColour(self):
        return self.colour

    def draw(self):
        if self.screen is not None:
            if self.actual is None:
                self.actual = pygame.Rect(self.xPos,
                                      self.yPos,
                                      self.xSize,
                                      self.ySize)

            pygame.draw.rect(self.screen,
                             self.colour,
                             self.actual)

    

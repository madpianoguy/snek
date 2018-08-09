from items import Item

import pygame

class Label(Item):

    def __init__(self):
        super().__init__()
        self.text =''
        self.fontType = 'Times New Roman'
        self.fontSize = 30
        self.fontColour = (255,255,255)
        self.font = pygame.font.SysFont(self.fontType,self.fontSize)
        self.textSurface = None
        self.textWidth = None
        self.textHeight = None
        self.textXPos = None
        self.textYPos = None
        self.isText = False
        self.colour = (0,0,0)

    def setTextColour(self,colour):
        self.fontColour = colour

    def autoSetTextColour(self):
        col = []
        for x in range(3):
            val = self.colour[x]
            diff = val - 127
            if diff > 0:
                val = 0
            else:
                val = 255
            col.append(val)
        self.fontColour = (col[0],col[1],col[2])
                

    def setText(self,text):
        self.text = text
        self.textSurface = self.font.render(text,True,self.fontColour)
        self.textWidth,self.textHeight = self.font.size(text)
        #self.calculateFontPosition()
        self.isText = True

    def calculateFontPosition(self):
        self.textXPos = int((self.xSize-self.textWidth) / 2) + self.xPos
        self.textYPos = int((self.ySize-self.textHeight) / 2) + self.yPos

    def draw(self):
        super().draw()
        if self.isText and self.screen is not None:
            self.calculateFontPosition()
            self.screen.blit(self.textSurface,(self.textXPos,self.textYPos))
        

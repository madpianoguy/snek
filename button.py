import pygame


class Button:

    def __init__(self,coords,size,screen,colour=(255,0,0)):
        self.xPos = coords[0]
        self.yPos = coords[1]
        self.xSize = size[0]
        self.ySize = size[1]
        self.screen = screen
        self.button = None
        self.rect = None
        self.colour = colour
        self.font = None
        self.text = ''
        self.textSurface = None
        self.fontType = None
        self.fontSize = None
        self.fontColour = None
        self.isText = False

    def draw(self,args=None):
        
        self.button = pygame.Rect(self.xPos,
                                self.yPos,
                                self.xSize,
                                self.ySize)
        
        self.rect = pygame.draw.rect(self.screen,
                                     self.colour,
                                     self.button)

        if self.isText:
            self.screen.blit(self.textSurface,self.textPos)
            

    def addText(self,text,fontType,fontSize,fontColour):
        self.text = text
        self.fontType = fontType
        self.fontSize = fontSize
        self.fontColour = fontColour
        self.font = pygame.font.SysFont(fontType,fontSize)
        self.textSurface = self.font.render(text,True,fontColour)
        width,height = self.font.size(text)
        self.textPos = self.calculateFontPos(width,height)
        self.isText = True

    def calculateFontPos(self,width,height):
        #x = (width-self.xSize) / 2 + self.xPos
        #y = (height-self.ySize) / 2 + self.ySize
        x = self.xPos + ((self.xSize - width) / 2)
        y = self.yPos + ((self.ySize - height) / 2)
        return (x,y)

    def collidepoint(self,mousePos):
        return (mousePos[0] > self.xPos and
                mousePos[0] < self.xPos + self.xSize and
                mousePos[1] > self.yPos and
                mousePos[1] < self.yPos + self.ySize)


        

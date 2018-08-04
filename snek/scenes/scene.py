import pygame

class Scene:

    def __init__(self,director):
        self.director = director
        self.isTextToWrite = False
        self.textSurface = None
        self.middleText = (0,0)    

    def on_update(self):
        pass

    def on_event(self,event):
        pass

    def on_draw(self):
        if self.isTextToWrite:
            self.director.screen.blit(self.textSurface,self.middleText)

    def on_reset(self):
        pass

    def on_startup(self):
        pass

    def writeText(self,text,font,size,colour):
        self.isTextToWrite = True
        font = pygame.font.SysFont(font,size)
        self.textSurface = font.render(text,True,colour)
        widthAndHeight = font.size(text)
        self.middleText = self.calculateMiddleScreen(widthAndHeight)
        #self.director.screen.blit(self.textSurface,self.middle)

    def calculateMiddle(self,widthAndHeight,screenDimensions):
        wLoc = int(screenDimensions[0]/2 - widthAndHeight[0]/2)
        hLoc = int(screenDimensions[1]/2 - widthAndHeight[1]/2)
        return (wLoc,hLoc)

    def calculateMiddleScreen(self,widthAndHeight):
        return self.calculateMiddle(widthAndHeight,
                                    (self.director.dWidth,
                                     self.director.dHeight))

    

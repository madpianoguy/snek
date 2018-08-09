from items.label import Label

import pygame

class Button(Label):

    def __init__(self):
        super().__init__()
        self.method = None
        self.hoverColour = self.getHoverColour(self.colour)
        self.originalColour = self.colour

    def bind(self,method):
        self.method = method

    def on_event(self,event):
        self.do_hover()
        self.do_click(event)

    def do_click(self,event):
        if (self.method is not None and
            event.type == pygame.MOUSEBUTTONDOWN and
            self.mouseIsOver(event.pos)):
            self.method()

    def do_hover(self):
        if self.mouseIsOver(pygame.mouse.get_pos()):
            self.colour = self.hoverColour
        else:
            self.colour = self.originalColour
            
    def getHoverColour(self,colour):
        new = []
        for val in colour:
            if val > 20:
                val -= 20
                if val < 0:
                    val = 0
            else:
                val += 20
                if val > 255:
                    val = 255
            new.append(val)
        return (new[0],new[1],new[2])

    def mouseIsOver(self,mousePos):
        return (mousePos[0] > self.xPos and
                mousePos[0] < self.xPos + self.xSize and
                mousePos[1] > self.yPos and
                mousePos[1] < self.yPos + self.ySize)

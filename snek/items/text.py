from items.button import Button

import pygame

class Text(Button):

    def __init__(self):
        super().__init__()
        self.colour = (255,255,255)
        self.originalColour = self.colour
        self.autoSetTextColour()
        self.hoverColour = self.getHoverColour(self.colour)
        self.active = False
        
    def on_event(self,event):
        #self.do_hover()
        self.do_active()
        if event.type == pygame.KEYDOWN and self.active:
            self.handleKeys(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.mouseIsOver(event.pos):
                self.active = True
            else:
                self.active = False

    def do_active(self):
        if self.active:
            self.colour = self.hoverColour
        else:
            self.colour = self.originalColour

    def handleKeys(self,event):
        if event.key == pygame.K_RETURN:
            print(self.text)
        elif event.key == pygame.K_BACKSPACE:
            if len(self.text) > 0:
                self.text = self.text[:-1]
        else:
            self.text += event.unicode

        self.setText(self.text)

    def getText(self):
        return self.text
        

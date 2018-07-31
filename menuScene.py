from scene import Scene
from settings import Settings as S

import pygame

class MenuScene(Scene):

    def __init__(self,director):
        super().__init__(director)
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS',200)
        self.button = None

    def on_update(self):
        pass

    def on_event(self,event):
        if (event.type == pygame.MOUSEBUTTONDOWN and
            self.button.collidepoint(event.pos)):
            self.director.change_scene('game')

    def on_draw(self):
        self.director.screen.fill(S.white)

        #Text
        textSurface = self.font.render('Snek',True,(0,0,0))
        width,height = self.font.size('Snek')
        self.director.screen.blit(textSurface,self.calculateMiddle((width,height)))

        #Button
        buttonSize = (300,100)
        buttonMiddle = self.calculateMiddle(buttonSize)
        buttonWidth, buttonHeight = (buttonMiddle[0],buttonMiddle[1]+200)
        
        self.button = pygame.Rect(buttonWidth,
                                  buttonHeight,
                                  buttonSize[0],
                                  buttonSize[1])
        
        myRec = pygame.draw.rect(self.director.screen,
                         S.red,
                         self.button)

        
        pygame.display.update()

    def calculateMiddle(self,widthAndHeight):
        return super().calculateMiddle(widthAndHeight,
                                                     (self.director.dWidth,
                                                      self.director.dHeight))
                         


from scene import Scene
from settings import Settings as S


from button import Button

import pygame

class MenuScene(Scene):

    def __init__(self,director):
        super().__init__(director)
        pygame.font.init()
        self.font = pygame.font.SysFont(S.font,200)
        self.button = None

        self.textSurface = None
        self.textWidth = None
        self.textHeight = None

        self.buttonSize = (300,100)
        self.buttonMiddle = None
        

        self.background = pygame.image.load('media/menu.JPG')

    def on_startup(self):
        print('Setting up menu')
        self.textSurface = self.font.render('Snek',True,(0,0,0))
        self.textWidth, self.textHeight = self.font.size('Snek')

        
        buttonMiddle = self.calculateMiddle(self.buttonSize)
        buttonWidth, buttonHeight = (buttonMiddle[0],buttonMiddle[1]+200)
        self.buttonMiddle = (buttonWidth,buttonHeight)
        self.button = Button(self.buttonMiddle,
                             self.buttonSize,
                             self.director.screen)
        self.button.addText('Play',S.font,60,S.black)

    def on_update(self):
        pass

    def on_event(self,event):
        if (event.type == pygame.MOUSEBUTTONDOWN and
            self.button.collidepoint(event.pos)):
            self.director.change_scene('game')

    def on_draw(self):
        self.director.screen.fill(S.white)

        self.director.screen.blit(self.background,(0,0))

        #Text
        self.director.screen.blit(self.textSurface,
                                self.calculateMiddle((self.textWidth,
                                                      self.textHeight)))

        #Button
        self.button.draw(S.red)

    def calculateMiddle(self,widthAndHeight):
        return super().calculateMiddle(widthAndHeight,
                                                     (self.director.dWidth,
                                                      self.director.dHeight))
                         


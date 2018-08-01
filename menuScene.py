from scene import Scene
from buttonManager import ButtonManager
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

        self.buttonManager = None
        

        self.background = pygame.image.load('media/menu.JPG')

    def on_startup(self):
        print('Setting up menu')
        self.textSurface = self.font.render('Snek',True,(0,0,0))
        self.textWidth, self.textHeight = self.font.size('Snek')

        self.buttonManager = ButtonManager(self.director,(0,500),height=100)

        print('First button')
        self.buttonManager.addButton(S.cyan,'Play - No Rules')
        print('Second button')
        self.buttonManager.addButton(S.cyan,'Play - Standard Rules')

    def on_update(self):
        pass

    def on_event(self,event):
        return
        if (event.type == pygame.MOUSEBUTTONDOWN and
            self.button.collidepoint(event.pos)):
            self.director.change_scene('standardGame')

    def on_draw(self):
        self.director.screen.fill(S.white)

        self.director.screen.blit(self.background,(0,0))

        #Text
        self.director.screen.blit(self.textSurface,
                                self.calculateMiddle((self.textWidth,
                                                      self.textHeight)))

        #Button
        self.buttonManager.draw()

    def calculateMiddle(self,widthAndHeight):
        return super().calculateMiddle(widthAndHeight,
                                                     (self.director.dWidth,
                                                      self.director.dHeight))
                         


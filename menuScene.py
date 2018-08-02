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
        self.textSurface = self.font.render('Snek',True,(0,0,0))
        self.textWidth, self.textHeight = self.font.size('Snek')

        self.buttonManager = ButtonManager(self.director,(0,500),height=100)

        self.buttonManager.addButton(S.cyan,'Play - No Rules',
                                     bind=self.playNoRules)

        self.buttonManager.addButton(S.cyan,'Play - Standard Rules',
                                     bind=self.playRules)

        self.buttonManager.addButton(S.cyan,'Reset Games',
                                     bind=self.resetGames)

    def on_update(self):
        pass

    def on_event(self,event):
        self.buttonManager.on_event(event)

    def on_draw(self):
        self.director.screen.fill(S.white)

        self.director.screen.blit(self.background,(0,0))

        #Text
        self.director.screen.blit(self.textSurface,
                                self.calculateMiddle((self.textWidth,
                                                      self.textHeight)))

        #Button
        self.buttonManager.draw()

    def playNoRules(self):
        self.director.change_scene('game')

    def playRules(self):
        self.director.change_scene('standardGame')

    def resetGames(self):
        self.director.reset_scene('game')
        self.director.reset_scene('standardGame')

    def calculateMiddle(self,widthAndHeight):
        return super().calculateMiddle(widthAndHeight,
                                                     (self.director.dWidth,
                                                      self.director.dHeight))
                         


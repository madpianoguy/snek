from scenes import Scene
from buttons import Button,ButtonManager
from settings import Settings as S




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
        

        self.background = pygame.image.load('../media/menu.JPG')

    def on_startup(self):
        self.textSurface = self.font.render('Snek',True,(0,0,0))
        self.textWidth, self.textHeight = self.font.size('Snek')

        self.buttonManager = ButtonManager(self.director,(0,500),height=100,
                                           fontType=S.font,
                                           fontSize=S.buttonFontSize)

        self.buttonManager.addButton(S.cyan,
                                     'Practice',
                                     bind=self.playNoRules,
                                     fontSize=S.buttonFontSize)

        self.buttonManager.addButton(S.cyan,
                                     'Singleplayer',
                                     bind=self.playRules,
                                     fontSize=S.buttonFontSize)

        self.buttonManager.addButton(S.cyan,
                                     'Multiplayer',
                                     bind=self.playMultiplayer,
                                     fontSize=S.buttonFontSize)

        self.buttonManager.addButton(S.cyan,
                                     'Reset',
                                     bind=self.resetGames,
                                     fontSize=S.buttonFontSize)

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

    def playMultiplayer(self):
        self.director.change_scene('multiplayerGame')

    def resetGames(self):
        self.director.reset_scene('game')
        self.director.reset_scene('standardGame')
        self.director.reset_scene('multiplayerGame')

    def calculateMiddle(self,widthAndHeight):
        return super().calculateMiddle(widthAndHeight,
                                                     (self.director.dWidth,
                                                      self.director.dHeight))
                         


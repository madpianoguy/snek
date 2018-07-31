import pygame
from random import randint
from time import sleep


from gameScene import GameScene

from settings import Settings as S


DWIDTH = 1000
DHEIGHT = 600

FPS = 20

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

P1CHAR = 'p1'
P1COLOUR = RED
EMPTY = 'e'
FOOD = 'f'
FOODCOLOUR = GREEN

NUMOFFOOD = 3

SIZE = 10

class Director:

    def __init__(self):
        pygame.init()
        self.dWidth = S.dWidth
        self.dHeight = S.dHeight
        self.screen = pygame.display.set_mode((self.dWidth,self.dHeight))
        pygame.display.set_caption('Snek')
        self.clock = pygame.time.Clock()
        self.quitFlag = False
        self.scene = None

    def quit(self):
        self.quitFlag = True

    def run(self):

        while not self.quitFlag:

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    self.quit()

                self.scene.on_event(event)

            self.scene.on_update()

            self.scene.on_draw()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

    def change_scene(self,scene):
        self.scene = scene
            



if __name__=='__main__':
    D = Director()
    GS = GameScene(D)
    D.change_scene(GS)
    D.run()




    

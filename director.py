import pygame
from random import randint

from settings import Settings as S


class Director:

    def __init__(self):
        pygame.init()
        self.dWidth = S.dWidth
        self.dHeight = S.dHeight
        self.screen = pygame.display.set_mode((self.dWidth,self.dHeight))
        pygame.display.set_caption('Snek')
        self.clock = pygame.time.Clock()
        self.quitFlag = False
        self.scenes = {}
        self.scene = None

        pygame.mixer.music.load('media/brownEyedGirl.mp3')
        pygame.mixer.music.play()

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
            self.clock.tick(S.fps)

        pygame.quit()

    def change_scene(self,sceneKey):
        self.scene = self.scenes[sceneKey]
        self.scene.on_startup()

    def add_scene(self,scene,key):
        self.scenes[key] = scene

    def reset_scene(self,scene_key):
        self.scenes[scene_key].on_reset()


        

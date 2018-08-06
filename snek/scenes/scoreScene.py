from scenes import Scene#,GridScene
from scenes.gridScene import GridScene
from basic import Scores
from items import Label
from settings import Settings as S

import pygame

class ScoreScene(Scene):

    def __init__(self,director):
        super().__init__(director)
        self.gridScene = GridScene(director,cols=1)
        self.scores = Scores()
        self.scores.load(S.media+'snek.scores')

        self.writeScores()

    def formatScore(self,score):
        return "{:10s} {:3d}".format(score[1],score[0])

    def writeScores(self):
        for score in self.scores.getScores():
            print(self.formatScore(score))
            l = Label()
            l.setText(self.formatScore(score))
            self.gridScene.addItem(l)

    def on_draw(self):
        self.gridScene.on_draw()

    def on_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                self.director.reset_scene('standardGame')
                self.director.change_scene('menu')

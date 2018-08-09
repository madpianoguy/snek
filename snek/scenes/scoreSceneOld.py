from scenes import Scene#,GridScene
from scenes.gridScene import GridScene
from basic import Scores
from items import Label,Button,Text
from settings import Settings as S

import pygame

class ScoreScene(Scene):

    def __init__(self,director):
        super().__init__(director)
        self.gridScene = GridScene(director,cols=1)
        self.scores = Scores()
        self.scores.load(S.media+'snek.scores')

        self.numOfScores = 10
        self.writeScores()

    def formatScore(self,score):
        return "{:10s} {:3d}".format(score[1],score[0])

    def writeScores(self):
        for i,score in enumerate(self.scores.getScores()):
            if i > self.numOfScores:
                break
            print(self.formatScore(score))
            l = Label()
            l.setText(self.formatScore(score))
            self.gridScene.addItem(l)

        scoreInput = Text()
        self.gridScene.addItem(scoreInput)
    
    def on_draw(self):
        self.gridScene.on_draw()

    def on_reset(self):
        self.__init__(self.director)

    def on_startup(self):
        self.__init__(self.director)

    def on_event(self,event):
        self.gridScene.on_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                self.director.reset_scene('standardGame')
                self.director.change_scene('menu')

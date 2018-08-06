from scenes import GameScene
from settings import Settings as S

import pygame

from random import randint


class StandardGameScene(GameScene):

    def __init__(self,director):
        super().__init__(director)
        self.walls = []
        self.stopped = False

    def on_startup(self):
        self.createWalls()
        
    def on_draw(self):
        super().on_draw()

        for coord in self.walls:
            self.drawSquare(S.blue,self.grid.getCoords(coord[0],coord[1]),0)

    def on_update(self):
        if not self.stopped:
            self.move()
            self.eatFood()
            self.checkIfCrashed()
            if self.checkIfGameOver():
                self.stop()

    def on_reset(self):
        self.__init__(self.director)

    def getScoreString(self):
        scores = ''
        for snek in self.sneks:
            print(snek.char,'scored',len(snek.getBody(True)))
            scores += snek.char + ' scored ' + str(len(snek.getBody(True))) + '\n'
        scores = scores[:-1]
        return scores

    def stop(self):
        self.stopped = True
        scores = self.getScoreString()
        #scores = scores[:-2]
        self.director.change_scene('scoreScene')
        #self.writeText(scores,S.font,S.scoreFontSize,S.white)

    def checkIfCrashed(self):
        for snek in self.sneks:
            for i,loc in enumerate(snek.body):
                if loc in self.walls:
                    snek.setDead()
                for val in range(len(snek.body)):
                    if val != i and snek.body[val] == loc:
                        snek.setDead()
        return False

    def checkIfGameOver(self):
        for snek in self.sneks:
            if not snek.isDead():
                return False
        return True

    def createWalls(self):
        for x in range(self.grid.cols):
            self.walls.append((x,0))
            self.walls.append((x,self.grid.rows-1))
        for y in range(self.grid.rows):
            self.walls.append((0,y))
            self.walls.append((self.grid.cols-1,y))

    def updateFood(self):
        while len(self.food) < S.numOfFood:
            cols,rows = self.grid.getSize()
            val = (randint(1,cols-2),randint(1,rows-2))
            self.food.append(val)
        

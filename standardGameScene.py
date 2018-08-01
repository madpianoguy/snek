from gameScene import GameScene
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
            if self.checkIfCrashed():
                self.stop()

    def stop(self):
        self.stopped = True
        for player in self.players:
            print('Game Over! You scored',len(player.body))

    def checkIfCrashed(self):
        for player in self.players:
            for i,loc in enumerate(player.body):
                if loc in self.walls:
                    return True
                for val in range(len(player.body)):
                    if val != i and player.body[val] == loc:
                        return True
        return False

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
        

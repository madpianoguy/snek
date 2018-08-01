from snek import Snek
from grid import Grid
from scene import Scene
from settings import Settings as S

from random import randint
import pygame

class GameScene(Scene):

    def __init__(self,director):
        super().__init__(director)

        

        #GRID INFO
        self.empty = S.empty
        self.size = S.size
        self.grid = Grid(self.director.dWidth,
                         self.director.dHeight,
                         self.size,
                         self.empty)

        #PLAYER INFO
        self.p1 = Snek((int(self.grid.cols/2),int(self.grid.rows/2)),S.p1Char)
        self.players = [self.p1]

        #OTHER INFO
        self.food = []
        self.updateFood()

    def on_update(self):
        self.move()
        self.eatFood()

    def on_event(self,event):
        if event.type == pygame.KEYDOWN:
            self.handleKey(event)

    def on_draw(self):
        self.director.screen.fill(S.black)
        self.draw()

    def updateFood(self):
        while len(self.food) < S.numOfFood:
            cols,rows = self.grid.getSize()
            val = (randint(0,cols-1),randint(0,rows-1))
            self.food.append(val)
            #print(self.food)

    def eatFood(self):
        if self.p1.head in self.food:
            self.p1.eaten = True
            self.food.remove(self.p1.head)
            self.updateFood()

    def handleKey(self,event):
        val = (0,0)
        if event.key == pygame.K_LEFT:
            val = (-1,0)
        elif event.key == pygame.K_RIGHT:
            val = (1,0)
        elif event.key == pygame.K_UP:
            val = (0,-1)
        elif event.key == pygame.K_DOWN:
            val = (0,1)
        elif event.key == 27:
            self.director.change_scene('menu')
            return
        self.p1.changeDirection(val)

    def drawSquare(self,colour,coords,fill=3):
        if len(coords) == 2:
            coords = (coords[0],coords[1],self.size,self.size)
        pygame.draw.rect(self.director.screen,colour,coords,fill)

    def move(self):
        self.p1.update()
        for coord in self.p1.body:
            self.grid.setValue(coord[0],coord[1],self.p1.char)
            
        if not self.p1.eaten:
            old = self.p1.old
            self.grid.setValue(old[0],old[1],S.empty)
            
        for coord in self.food:
            self.grid.setValue(coord[0],coord[1],S.food)

    def draw(self):
        for coord in self.p1.getCoords():
            self.drawSquare(S.p1Colour,self.grid.getCoords(coord[0],coord[1]))
        for coord in self.food:
            self.drawSquare(S.foodColour,self.grid.getCoords(coord[0],coord[1]))

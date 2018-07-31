from snek import Snek
from grid import Grid
from settings import Settings as S

from random import randint
import pygame

class GameScene:

    def __init__(self,director):
        self.director = director

        #PLAYER INFO
        self.p1 = Snek((5,0),S.p1Char)
        self.players = [self.p1]

        #GRID INFO
        self.empty = S.empty
        self.size = S.size
        self.grid = Grid(self.director.dWidth,
                         self.director.dHeight,
                         self.size,
                         self.empty)

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
        self.p1.changeDirection(val)

    def drawSquare(self,colour,coords):
        pygame.draw.rect(self.director.screen,colour,coords,3)

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
        self.director.screen.fill(S.black)
        for coord in self.p1.getCoords():
            self.drawSquare(S.p1Colour,self.grid.getCoords(coord[0],coord[1]))
        for coord in self.food:
            self.drawSquare(S.foodColour,self.grid.getCoords(coord[0],coord[1]))

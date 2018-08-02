from snek import Snek
from grid import Grid
from scene import Scene
from settings import Settings as S

from random import randint
import pygame

class GameScene(Scene):

    def __init__(self,director,sneks=[Snek(char=S.p1Char)]):
        super().__init__(director)

        

        #GRID INFO
        self.empty = S.empty
        self.size = S.size
        self.grid = Grid(self.director.dWidth,
                         self.director.dHeight,
                         self.size,
                         self.empty)

        #PLAYER INFO
        self.sneks = sneks
        self.setStartingPositions()

        #OTHER INFO
        self.food = []
        self.updateFood()

    def setStartingPositions(self):
        xPos = int(self.grid.rows/3)
        for i,snek in enumerate(self.sneks):
            yPos = int(self.grid.rows/(len(self.sneks)+1))* (i+1)
            snek.setStartCoords((xPos,yPos))

    def setSneks(self,sneks):
        self.sneks = sneks
        self.setStartingPositions()

    def on_update(self):
        self.move()
        self.eatFood()

    def on_event(self,event):
        self.isEscape(event)
        if event.type == pygame.KEYDOWN:
            self.handleKey(event)

    def on_draw(self):
        self.director.screen.fill(S.black)
        self.draw()

    def on_reset(self):
        self.__init__(self.director)

    def isEscape(self,event):
        if (event.type == pygame.KEYDOWN and
            event.key == 27):
            self.director.change_scene('menu')

    def updateFood(self):
        while len(self.food) < S.numOfFood:
            cols,rows = self.grid.getSize()
            val = (randint(0,cols-1),randint(0,rows-1))
            self.food.append(val)
            #print(self.food)

    def eatFood(self):
        for snek in self.sneks:
            if snek.head in self.food:
                snek.eaten = True
                self.food.remove(snek.head)
                self.updateFood()

    def handleKey(self,event):
        for snek in self.sneks:
            snek.on_event(event)

    def drawSquare(self,colour,coords,fill=3):
        if len(coords) == 2:
            coords = (coords[0],coords[1],self.size,self.size)
        pygame.draw.rect(self.director.screen,colour,coords,fill)

    def move(self):
        for snek in self.sneks:
            snek.update()
            for coord in snek.body:
                self.grid.setValue(coord[0],coord[1],snek.char)
                
            if not snek.eaten:
                old = snek.old
                self.grid.setValue(old[0],old[1],S.empty)
            
        for coord in self.food:
            self.grid.setValue(coord[0],coord[1],S.food)

    def draw(self):
        for snek in self.sneks:
            for coord in snek.getCoords():
                self.drawSquare(snek.colour,
                                self.grid.getCoords(coord[0],coord[1]))
        for coord in self.food:
            self.drawSquare(S.foodColour,self.grid.getCoords(coord[0],coord[1]))

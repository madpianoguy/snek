import pygame
from random import randint
from time import sleep

from snek import Snek
from grid import Grid

dWidth = 1000
dHeight = 600

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



class SnekGame:

    def __init__(self,dWidth,dHeight,size):
        pygame.init()
        self.p1 = Snek((5,0),P1CHAR)
        self.dWidth = dWidth
        self.dHeight = dHeight
        self.size = size
        self.screen = pygame.display.set_mode((dWidth,dHeight))
        pygame.display.set_caption('Snek')
        self.clock = pygame.time.Clock()
        self.grid = Grid(dWidth,dHeight,size,EMPTY)
        self.food = []
        self.updateFood()

    def run(self):
        run = True


        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    self.handleKey(event)

            self.move()
            #self.grid.printGrid()
            self.eatFood()
            self.draw()
            
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

    def updateFood(self):
        while len(self.food) < NUMOFFOOD:
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
        

    def move(self):
        self.p1.update()
        for coord in self.p1.body:
            self.grid.setValue(coord[0],coord[1],self.p1.char)
            
        if not self.p1.eaten:
            old = self.p1.old
            self.grid.setValue(old[0],old[1],EMPTY)
            
        for coord in self.food:
            self.grid.setValue(coord[0],coord[1],FOOD)

    def drawSquare(self,colour,coords):
        pygame.draw.rect(self.screen,colour,coords,3)

    def draw(self):
        self.screen.fill(BLACK)
        for coord in self.p1.getCoords():
            self.drawSquare(P1COLOUR,self.grid.getCoords(coord[0],coord[1]))
        for coord in self.food:
            self.drawSquare(FOODCOLOUR,self.grid.getCoords(coord[0],coord[1]))
                    

if __name__=='__main__':
    SG = SnekGame(dWidth,dHeight,10)
    SG.run()
    quit()

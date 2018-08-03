import pygame

class Snek:

    def __init__(self,char='s',colour=(255,0,0),startCoord=(10,10),
                 keys=[pygame.K_UP,
                       pygame.K_LEFT,
                       pygame.K_DOWN,
                       pygame.K_RIGHT]):
        self.startCoord = startCoord
        self.head = startCoord
        self.body = []
        self.redrawBody()
        self.direction = (1,0)
        self.char = char
        self.colour = colour
        self.old = (20,20)
        self.eaten = False
        self.keys = keys
        self.bindings = [(0,-1),(-1,0),(0,1),(1,0)]
        self.isAlive = True

    def setDead(self):
        self.isAlive = False

    def isDead(self):
        return not self.isAlive

    def on_event(self,event):
        for x in range(len(self.keys)):
            if event.key == self.keys[x]:
                if self.isValidDirection(self.bindings[x]):
                    self.direction = self.bindings[x]

    def getBody(self,head=False):
        if head:
            return self.body
        return self.body[1:]

    def getHead(self):
        return self.head

    def isValidDirection(self,newDirection):
        return not (self.direction[0] == newDirection[0] or
                self.direction[1] == newDirection[1])

    def redrawBody(self):
        self.body = [(int(self.startCoord[0])-x,
                      int(self.startCoord[1])) for x in range(5)]
        self.head = self.body[0]

    def setStartCoords(self,coords):
        self.startCoord = coords
        self.redrawBody()

    def getCoords(self):
        return self.body

    def getColour(self):
        return self.colour

    def update(self):
        if self.isAlive:
            head = self.body[0]
            new = (head[0]+self.direction[0],head[1]+self.direction[1])
            self.body.insert(0,new)
            self.head = self.body[0]
            if not self.eaten and len(self.body) > 0:
                self.old = self.body.pop()
            else:
                self.eaten = False

    def changeDirection(self,direction):
        if direction[0] != self.direction[0] and direction[1] != self.direction[1]:
            self.direction = direction

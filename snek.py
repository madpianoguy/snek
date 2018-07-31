class Snek:

    def __init__(self,startCoord,char):
        self.head = startCoord
        self.body = [(startCoord[0]-x,startCoord[1]) for x in range(5)]
        self.direction = (1,0)
        self.char = char
        self.old = (20,20)
        self.eaten = False

    def getCoords(self):
        return self.body

    def update(self):
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

class Grid:

    def __init__(self,dWidth,dHeight,size,emptyChar):
        self.dWidth = dWidth
        self.dHeight = dHeight
        self.size = size
        self.rows = int(self.dHeight/self.size)
        self.cols = int(self.dWidth/self.size)
        self.grid = [[emptyChar for y in range(0,dWidth,size)]
                     for x in range(0,dHeight,size)]

    def getValue(self,xVal,yVal):
        if xVal >= 0 and xVal < self.cols:
            if yVal >= 0 and yVal < self.rows:
                return self.grid[yVal][xVal]
        return None

    def setValue(self,xVal,yVal,value):
        if xVal > 0 and xVal < self.cols:
            if yVal > 0 and yVal < self.rows:
                self.grid[yVal][xVal] = value
                return True
        return False

    def getCoords(self,xVal,yVal):
        return (xVal*self.size,yVal*self.size,self.size,self.size)

    def getSize(self):
        return self.cols,self.rows

    def printGrid(self):
        for row in self.grid:
            vals = ''
            for val in row:
                vals += val
            print(vals)
        print('\n\n\n\n\n')
        
        

    

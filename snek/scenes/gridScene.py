from scenes import Scene


class GridScene(Scene):

    def __init__(self,director,width=None,height=None,
                 orientation='horizontal',cols=0):
        
        super().__init__(director)
        
        self.sections = []
        self.numOfSections = 0
        
        if width is None:
            width = self.director.dWidth
        if height is None:
            height = self.director.dHeight
        if cols == 0:
            self.expand = True
        else:
            self.expand = False
        self.width = width
        self.height = height
        self.orientation = orientation
        self.cols = cols

    def on_draw(self):
        for item in self.sections:
            item.draw()

    def on_event(self,event):
        for item in self.sections:
            item.on_event(event)

    def addItem(self,item):
        self.addSection(item)
        
    def addSection(self,item):
        self.numOfSections += 1
        sections = self.sections
        self.sections = []
        if self.expand:
            self.cols = self.numOfSections
        #print('Adding:',item)
        #print('Sections:',self.numOfSections)
        for section in sections:
            size = self.getNextSize()
            coords = self.getNextCoords()
            section.setSize(size)
            section.setPos(coords)
            self.sections.append(section)
            #print(self.sections)
        size = self.getNextSize()
        coords = self.getNextCoords()
        #print(coords,size)
        item.setSize(size)
        item.setPos(coords)
        item.setScreen(self.director.screen)
        self.sections.append(item)
        #print(self.sections)

    def getNextSize(self):
        numOfSections = self.numOfSections
        columns = self.cols

        rows = (numOfSections//columns)
        if numOfSections % columns > 0:
            rows += 1
        
        # 1 // 1 = 1 1
        # 2 // 1 = 2 2
        # 3 // 1 = 3 3
        
        # 1 // 2 = 0 1
        # 2 // 2 = 1 1
        # 3 // 2 = 1 2
        
        # 1 // 3 = 0 1
        # 2 // 3 = 0 1
        # 3 // 3 = 1 1
        
        widthPerItem = int(self.width / columns)
        heightPerItem = int(self.height / rows)
        
        return (widthPerItem,heightPerItem)

    def getNextCoords(self):
        currentSectionCount = len(self.sections)
        totalSectionCount = self.numOfSections
        columns = self.cols
        widthPerItem,heightPerItem = self.getNextSize()
        
        currentCol = currentSectionCount % columns #starting at index 0
        currentRow = currentSectionCount // columns #starting at index 0

        xPos = widthPerItem * currentCol
        yPos = heightPerItem * currentRow
        return (xPos,yPos)

        
        

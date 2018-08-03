from button import Button
from settings import Settings as S

import pygame



class ButtonManager:

    def __init__(self,director,startCoords,
                 width=None,height=None,cols=True,full=True,
                 fontType='Times New Roman',fontSize=30):

        
        self.startCoords = startCoords
        self.director = director
        self.screen = director.screen
        self.xStart = startCoords[0]
        self.yStart = startCoords[1]

        self.cols = cols
        self.full = full
        self.fontType = fontType
        self.fontSize = fontSize
        
        if width is None:
            self.width = self.director.dWidth
        else:
            self.width = width
        if height is None:
            self.height = self.director.dHeight
        else:
            self.height = height

        #print('Button manager:',self.width,self.height)

        self.numOfButtons = 0
        self.buttons = []

    def on_event(self,event):
        for button in self.buttons:
            button.on_event(event)

    def draw(self):
        for button in self.buttons:
            button.draw()
        

    def addButton(self,colour,text=False,fontColour=(0,0,0),
                  fontType=False,fontSize=False,bind=False):
        if not fontType:
            fontType = self.fontType
        if not fontSize:
            fontSize = self.fontSize
            
        self.numOfButtons = len(self.buttons)
        oldButtons = self.buttons
        self.buttons = []
        for button in oldButtons:
            size,coords = self.getNextSizeCoords()
            newButton = Button(coords,size,self.screen,button.colour)
            if button.isText:
                newButton.addText(button.text,button.fontType,button.fontSize,
                              button.fontColour)
            if button.isBound():
                newButton.bind(button.method)
            self.buttons.append(newButton)

        size,coords = self.getNextSizeCoords()
        #print('Button:',text,'size:',size,'coords:',coords)
        newButton = Button(coords,size,self.screen,colour)
        if text != False:
            newButton.addText(text,fontType,fontSize,fontColour)
        if bind is not None:
            newButton.bind(bind)
        self.buttons.append(newButton)
        
        self.numOfButtons += 1
        

    def getNextSizeCoords(self):
        """
        Use method to get x and y coordinates of next button
        """
        #get button width and height
        if self.cols:
            width = int(self.width/(self.numOfButtons+1))
            height = self.height
        else:
            width = int(self.width/cols)
            height = int((self.numOfButtons+1) % self.cols)

        #get button initial coordinates
        if self.cols:
            xPos = int(self.width/(self.numOfButtons+1))*len(self.buttons)
            yPos = self.startCoords[1]
        return (width,height),(xPos,yPos)

        
        

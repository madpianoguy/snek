from scenes.gridScene import GridScene
from basic import Scores
from items import Button,Text,Label

from settings import Settings as S

from time import sleep

class ScoreScene(GridScene):

    def __init__(self,director):
        super().__init__(director,cols=1)
        self.scoreManager = Scores()
        self.saveFile = S.media+'snek.scores'
        self.scoreManager.load(self.saveFile)

        self.scoreInput = Text()
        self.addButton = Button()
        self.addButton.setText('Submit Name and Score')
        self.addButton.bind(self.addScore)

        self.addItem(self.scoreInput)
        self.addItem(self.addButton)

        self.latestScore = 0

        self.refreshScores()

    def setLatestScore(self,score):
        self.latestScore = score

    def addScore(self):
        if len(self.scoreInput.text) > 0:
            self.scoreManager.addScore(self.latestScore,self.scoreInput.text)
            self.refreshScores()
            self.scoreManager.save(self.saveFile)

    def formatScore(self,score):
        return "{:10s} {:3d}".format(score[1],score[0])
    
    def refreshScores(self):
        print('Refreshing Scores')
        while self.removeItem(-2):
            print(len(self.sections))
        #self.sections = []
        #self.sections.append(self.scoreInput)
        #self.sections.append(self.addButton)
        for score in self.scoreManager.getScores():
            l = Label()
            l.setText(self.formatScore(score))
            self.insertItem(l,-2)
            print(len(self.sections))
        self.refreshLayout()
            
        

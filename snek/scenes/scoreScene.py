from scenes.gridScene import GridScene
from basic import Scores
from items import Button,Text,Label

from settings import Settings as S

class ScoreScene(GridScene):

    def __init__(self,director):
        super().__init__(director,cols=1)
        self.scoreManager = Scores()
        self.saveFile = S.media+'snek.scores'
        self.scoreManager.load(self.saveFile)

        scoreInput = Text()
        addButton = Button()
        addButton.setText('Submit Name and Score')

        self.addItem(scoreInput)
        self.addItem(addButton)

    def formatScore(self,score):
        return "{:10s} {:3d}".format(score[1],score[0])
    
    def refreshScores(self):
        for score in self.scoreManager.getScores():
            l = Label()
            l.setText(self.formatScore(score))
            self.insertItem(l,-2)
            
        

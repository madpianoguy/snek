from scenes import Scene
from basic import Scores
from settings import Settings as S

class ScoreScene(Scene):

    def __init__(self,director):
        super().__init__(director)
        self.scoreManager = Scores()
        self.scoreManager.load(S.media+'snek.scores')
        self.writeScores()

    def formatScores(self):
        scoreString = ''
        for score in self.scoreManager.getScores():
            print(score)
            text = '{:10s} {:3d}'.format(score[1],score[0])
            #text = '{:10s} {:3d}'
            #format(text,[score[1],score[0]])
            #text = score[1] + str(score[0])
            scoreString += text + ' '
        #scoreString = scoreString[:-1]
        return scoreString

    def on_draw(self):
        self.director.screen.fill(S.black)
        super().on_draw()

    def writeScores(self):
        text = self.formatScores()
        print('Writing:',text)
        self.writeText(text,S.font,S.standardFontSize,S.white)

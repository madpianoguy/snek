from basic import Scores
from scenes.scoreScene import ScoreScene
from scenes.gridScene import GridScene
from items import Item
from director import Director
from settings import Settings as S

if __name__=='__main__':
    #Score = Scores()
    #Score.load(S.media+'snek.scores')
    #print(Score.getScores())

    I1 = Item()
    I2 = Item()
    I3 = Item()
    

    D = Director()
    GS = GridScene(D,cols=2)
    GS.addSection(I1)
    GS.addSection(I2)
    GS.addSection(I3)
    D.add_scene(GS,'gridScene')
    D.change_scene('gridScene')
    pass
    

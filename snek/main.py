from director import Director
from scenes import GameScene,MenuScene,StandardGameScene
from scenes import MultiplayerGameScene,ScoreScene,GridScene
from items import Item,Label
from settings import Settings as S


class SnekGame:

    def __init__(self):
        D = Director()
        GS = GameScene(D)
        MS = MenuScene(D)
        SGS = StandardGameScene(D)
        MGS = MultiplayerGameScene(D)
        SS = ScoreScene(D)
        D.add_scene(MS,'menu')
        D.add_scene(GS,'game')
        D.add_scene(SGS,'standardGame')
        D.add_scene(MGS,'multiplayerGame')
        D.add_scene(SS,'scoreScene')
        
        GrS = GridScene(D,cols=1)
        D.add_scene(GrS,'gridScene')
        I1 = Item()
        I1.setColour(S.red)
        I2 = Item()
        I2.setColour(S.yellow)
        I3 = Item()
        I3.setColour(S.cyan)
        L1 = Label()
        L1.setColour(S.purple)
        L1.setText('Hello')

        GrS.addSection(L1)
        GrS.addSection(I1)
        GrS.addSection(I2)
        GrS.addSection(I3)
        D.change_scene('gridScene')
        
        #D.change_scene('menu')
        #D.change_scene('scoreScene')
        D.run()
        
#TO-DO
        
#Add Snek-Snek collision detection in multiplayer
#Add Snek name value and update end of game score printing
#Add different controls for different Sneks



if __name__=='__main__':
    Game = SnekGame()




    

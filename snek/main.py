from director import Director
from scenes import GameScene,MenuScene,StandardGameScene
from scenes import MultiplayerGameScene,ScoreScene


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
        #D.change_scene('menu')
        D.change_scene('scoreScene')
        D.run()
        
#TO-DO
        
#Add Snek-Snek collision detection in multiplayer
#Add Snek name value and update end of game score printing
#Add different controls for different Sneks



if __name__=='__main__':
    Game = SnekGame()




    

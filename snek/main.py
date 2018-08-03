from director.director import Director
from scenes.gameScene import GameScene
from scenes.menuScene import MenuScene
from scenes.standardGameScene import StandardGameScene
from scenes.multiplayerGameScene import MultiplayerGameScene


class SnekGame:

    def __init__(self):
        D = Director()
        GS = GameScene(D)
        MS = MenuScene(D)
        SGS = StandardGameScene(D)
        MGS = MultiplayerGameScene(D)
        D.add_scene(MS,'menu')
        D.add_scene(GS,'game')
        D.add_scene(SGS,'standardGame')
        D.add_scene(MGS,'multiplayerGame')
        D.change_scene('menu')
        D.run()
        
#TO-DO
        
#Add Snek-Snek collision detection in multiplayer
#Add Snek name value and update end of game score printing
#Add different controls for different Sneks



if __name__=='__main__':
    Game = SnekGame()




    

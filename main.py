from director import Director
from gameScene import GameScene
from menuScene import MenuScene
from standardGameScene import StandardGameScene
from multiplayerGameScene import MultiplayerGameScene


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




    

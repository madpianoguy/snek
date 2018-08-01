from director import Director
from gameScene import GameScene
from menuScene import MenuScene
from standardGameScene import StandardGameScene


if __name__=='__main__':
    D = Director()
    GS = GameScene(D)
    MS = MenuScene(D)
    SGS = StandardGameScene(D)
    #D.change_scene(GS)
    D.add_scene(MS,'menu')
    D.add_scene(GS,'game')
    D.add_scene(SGS,'standardGame')
    D.change_scene('menu')
    D.run()




    

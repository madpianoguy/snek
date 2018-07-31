from director import Director
from gameScene import GameScene
from menuScene import MenuScene


if __name__=='__main__':
    D = Director()
    GS = GameScene(D)
    MS = MenuScene(D)
    #D.change_scene(GS)
    D.add_scene(MS,'menu')
    D.add_scene(GS,'game')
    D.change_scene('menu')
    D.run()




    

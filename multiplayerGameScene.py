from standardGameScene import StandardGameScene
from snek import Snek
from settings import Settings as S

import pygame


class MultiplayerGameScene(StandardGameScene):

    def __init__(self,director):
        super().__init__(director)
        self.setSneks([S.sneks[0],S.sneks[1]])
        #self.setSneks(S.sneks)

    def on_reset(self):
        self.__init__(self.director)
        

    def checkIfCrashed(self):
        super().checkIfCrashed()
        snekBody = []
        for snek in self.sneks:
            snekBody += snek.getBody(head=False)
        for snek in self.sneks:
            #print(snek.getHead(),snekBody)
            if snek.getHead() in snekBody:
                snek.setDead()

    def checkIfGameOver(self):
        oneAlive = False
        for snek in self.sneks:
            if not snek.isDead():
                if oneAlive:
                    return False
                else:
                    oneAlive = True
        return True

    def stop(self):
        self.stopped = True
        for snek in self.sneks:
            if not snek.isDead():
                print(snek.char,'won!')

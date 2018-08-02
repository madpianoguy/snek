from standardGameScene import StandardGameScene
from snek import Snek
from settings import Settings as S

import pygame


class MultiplayerGameScene(StandardGameScene):

    def __init__(self,director):
        super().__init__(director)
        self.setSneks([Snek(S.p1Char,S.p1Colour),
                      Snek(S.p2Char,S.p2Colour)])
        

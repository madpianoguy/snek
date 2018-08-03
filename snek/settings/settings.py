from basic.player import Player
from basic.snek import Snek
import pygame

class Settings:

    dWidth = 1000
    dHeight = 600

    size = 10

    fps = 20

    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    yellow = (255,255,0)
    cyan = (0,255,255)
    purple = (128,0,128)
    maroon = (128,0,0)

    p1Char = 'p1'
    p1Colour = red
    p1Keys = [
        pygame.K_UP,
        pygame.K_LEFT,
        pygame.K_DOWN,
        pygame.K_RIGHT
        ]

    p2Char = 'p2'
    p2Colour = white
    p2Keys = [
        pygame.K_w,
        pygame.K_a,
        pygame.K_s,
        pygame.K_d
        ]

    p3Char = 'p3'
    p3Colour = yellow
    p3Keys = [
        pygame.K_i,
        pygame.K_j,
        pygame.K_k,
        pygame.K_l]

    sneks = [Snek(p1Char,p1Colour,keys=p1Keys),
             Snek(p2Char,p2Colour,keys=p2Keys),
             Snek(p3Char,p3Colour,keys=p3Keys)]
    empty = 'e'
    food = 'f'
    wallChar = 'w'
    
    foodColour = green
    wallColour = blue

    numOfFood = 3

    font = 'Times New Roman'
    #font = 'Comic Sans MS'
    buttonFontSize = 35
    standardFontSize = 30
    scoreFontSize = 100


    

from player import Player

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

    p2Char = 'p2'
    p2Colour = white

    p3Char = 'p3'
    p3Colour = yellow

    players = [Player(p1Char,p1Colour),
               Player(p2Char,p2Colour),
               Player(p3Char,p3Colour)]
    empty = 'e'
    food = 'f'
    wallChar = 'w'
    
    foodColour = green
    wallColour = blue

    numOfFood = 3

    font = 'Comic Sans MS'


    

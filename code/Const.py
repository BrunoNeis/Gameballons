#Color
import pygame

#C
C_BLACK = (0,0,0)
C_RED = (255,0,0)
C_YELLOW = (255,255,0)
C_ORANGE = (255,177,0)
C_BLUE = (8,155,189)

#E
EVENT_GHOST= pygame.USEREVENT + 1

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level4Bg0': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,
    'Level4Bg3': 0,
    'Level4Bg4': 0,
    'Player1': 1,
    "Player1Shot":25,
    'Player2':1,
    "Player2Shot":25,
    'Ghost1':1,
    'Ghost1Shot':25,
    'Ghost2':1,
    'Ghost2Shot':27,
    'Ghost3':1,
    'Ghost3Shot':30,
}
ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level4Bg0': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,
    'Level4Bg3': 0,
    'Level4Bg4': 0,
    'Player1': 0,
    "Player1Shot":0,
    'Player2':0,
    "Player2Shot":0,
    'Ghost1':110,
    'Ghost1Shot':0,
    'Ghost2':125,
    'Ghost2Shot':0,
    'Ghost3':135,
    'Ghost3Shot':0,
}

ENTITY_SPEED= {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 1,
    'Level1Bg3': 0,
    'Level1Bg4': 1,
    'Player1': 4,
    "Player1Shot":5,
    'Player2': 4,
    "Player2Shot":5,
    "Ghost1":2,
    "Ghost1Shot":4,
    "Ghost2":1,
    "Ghost2Shot":3,
    "Ghost3":1,
    "Ghost3Shot":2,

}

ENTITY_HEALTH= {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Level3Bg4': 999,
    'Level4Bg0': 999,
    'Level4Bg1': 999,
    'Level4Bg2': 999,
    'Level4Bg3': 999,
    'Level4Bg4': 999,
    'Player1':400,
    "Player1Shot":3,
    'Player2':400,
    "Player2Shot":3,
    'Ghost1':30,
    'Ghost1Shot':1,
    'Ghost2':80,
    'Ghost2Shot':2,
    'Ghost3':100,
    'Ghost3Shot':3,

}
ENTITY_SHOT_DELAY={
        'Player1':20,
        "Player2":20,
        'Ghost1':80,
        'Ghost2':120,
        'Ghost3':180,

}



#M
MENU_OPTION =("NEW GAME","2 PLAYERS","SCORE","EXIT")

#P
PLAYER_KEY_UP = {'Player1':pygame.K_UP,
                 'Player2':pygame.K_w}
PLAYER_KEY_DOWN= {'Player1':pygame.K_DOWN,
                 'Player2':pygame.K_s}
PLAYER_KEY_LEFT = {'Player1':pygame.K_LEFT,
                 'Player2':pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1':pygame.K_RIGHT,
                 'Player2':pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1':pygame.K_RCTRL,
                 'Player2':pygame.K_LCTRL}
#S
SPAW_TIME= 4000


# W   - Screen
WIN_WIDTH = 1000
WIN_HEIGHT = 563


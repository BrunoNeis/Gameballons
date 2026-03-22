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
EVENT_TIMEOUT= pygame.USEREVENT + 2
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
    "Player1Shot":1,
    'Player2':1,
    "Player2Shot":1,
    'Ghost1':1,
    'Ghost1Shot':1,
    'Ghost2':1,
    'Ghost2Shot':2,
    'Ghost3':1,
    'Ghost3Shot':3,
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
    'Ghost1':10,
    'Ghost1Shot':0,
    'Ghost2':25,
    'Ghost2Shot':0,
    'Ghost3':35,
    'Ghost3Shot':0,
}

ENTITY_SPEED= {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 1,
    'Level1Bg3': 0,
    'Level1Bg4': 1,
    'Level2Bg0': 0,
    'Level2Bg1': 2,
    'Level2Bg2': 1,
    'Level2Bg3': 0,
    'Level2Bg4': 1,
    'Level3Bg0': 0,
    'Level3Bg1': 2,
    'Level3Bg2': 1,
    'Level3Bg3': 0,
    'Level3Bg4': 1,
    'Level4Bg0': 0,
    'Level4Bg1': 2,
    'Level4Bg2': 1,
    'Level4Bg3': 0,
    'Level4Bg4': 1,
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
    'Player1':100,
    "Player1Shot":1,
    'Player2':100,
    "Player2Shot":1,
    'Ghost1':1,
    'Ghost1Shot':1,
    'Ghost2':2,
    'Ghost2Shot':2,
    'Ghost3':4,
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
SPAW_TIME= 1000

#T
TIMEOUT_STEP= 100 #100Ms
TIMEOUT_LEVEL = 50000 #30s

# W   - Screen
WIN_WIDTH = 1000
WIN_HEIGHT = 563
#S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 90),
             'EnterName': (WIN_WIDTH / 2, 150),
             'Label': (WIN_WIDTH / 2, 150),
             'Name': (WIN_WIDTH / 2, 200),
             0: (WIN_WIDTH / 2, 195),
             1: (WIN_WIDTH / 2, 225),
             2: (WIN_WIDTH / 2, 260),
             3: (WIN_WIDTH / 2, 290),
             4: (WIN_WIDTH / 2, 320),
             5: (WIN_WIDTH / 2, 350),
             6: (WIN_WIDTH / 2, 380),
             7: (WIN_WIDTH / 2, 410),
             8: (WIN_WIDTH / 2, 450),
             9: (WIN_WIDTH / 2, 470),
             10: (WIN_WIDTH / 2,500)
             }


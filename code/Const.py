#Color
import pygame

#C
COLOR_BLACK = (0,0,0)
COLOR_RED = (255,0,0)
COLOR_YELLOW = (255,255,0)


#E
EVENT_GHOST= pygame.USEREVENT + 1

ENTITY_SPEED= {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 1,
    'Level1Bg3': 0,
    'Level1Bg4': 1,
    'Player1': 3,
    'Player2': 3,
    "Ghost1":2,
    "Ghost2":2,
    "Ghost3":1,

}

#K




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


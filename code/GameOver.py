import sys

import pygame
from pygame.constants import KEYDOWN, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface


class GameOver:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load("./asset/GameOver.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass


    def show_gameover(self):
        pygame.mixer_music.load("./asset/GameOver.mp3")
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()



    def gameover_text(self,text_size:int, text: str, text_color: tuple , text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name="Blood Victim Zombie", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

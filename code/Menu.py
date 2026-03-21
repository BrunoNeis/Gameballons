#!/usr/bin/python
# -*- coding: utf-8 -*-
from pydoc_data.topics import topics
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, C_BLACK, MENU_OPTION, C_RED, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/Menubg.png").convert_alpha()
        self.rect = self.surf.get_rect(left = 0, top=0 )

    def run(self,):
        menu_option = 0
        pygame.mixer_music.load("./asset/grimghosts.mp3")
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(150, text="GHOST ARROW",  text_color=(C_BLACK), text_center_pos=((WIN_WIDTH/2),200))

            for i in range(len(MENU_OPTION)):
               if i== menu_option:
                   self.menu_text(50, MENU_OPTION[i], text_color=(C_YELLOW), text_center_pos=(200 + 200 * i, 350))
               else:
                self.menu_text(50, MENU_OPTION[i], text_color=(C_RED),text_center_pos=(200 + 200 * i, 350))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close Window
                    quit()  # end pygame.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: #MOVE FOR
                       if menu_option < len(MENU_OPTION) -1:
                          menu_option +=1
                       else:
                          menu_option =0
                    if event.key == pygame.K_LEFT:
                        if menu_option >0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]

#text menu
    def menu_text(self,text_size:int, text: str, text_color: tuple , text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name="Blood Victim Zombie", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        pass
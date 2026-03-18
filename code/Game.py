#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
       # self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH , WIN_HEIGHT))


    def run(self):
        while True:
           menu = Menu(self.window)
           menu.run()
           pass
           #  check for all evesnts
            #   for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # close Window
            #        quit()  # end pygame.
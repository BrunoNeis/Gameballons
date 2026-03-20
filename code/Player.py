#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
import pygame.key

class Player(Entity):

    def __init__(self,name: str, position: tuple):
        super().__init__(name, position)







    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]and self.rect.top > 150:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN]and self.rect.bottom < WIN_HEIGHT-50:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT]and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT]and self.rect.right < WIN_WIDTH / 3:
            self.rect.centerx += ENTITY_SPEED[self.name]



        pass

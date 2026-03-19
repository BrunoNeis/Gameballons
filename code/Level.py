#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity


class Level:
    def __init__(self, window, name, game):
        self.window = window
        self.name = name
        self.game = game
        self.entity_list = list[Entity]= []



    def run(self, ):
        pass

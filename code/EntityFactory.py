#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from unittest import case

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Ghost import Ghost
from code.Player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str,):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level3Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level4Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level4Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level4Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1',(10 ,WIN_HEIGHT/3 +50))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT/2 +50))
            case 'Ghost1':
                return Ghost('Ghost1', (WIN_WIDTH + 10,random.randint(+150,WIN_HEIGHT -100)))
            case 'Ghost2':
                return Ghost('Ghost2', (WIN_WIDTH + 20, random.randint(+150,WIN_HEIGHT -100)))
            case 'Ghost3':
                return Ghost('Ghost3', (WIN_WIDTH + 10, random.randint(+150,WIN_HEIGHT -100)))
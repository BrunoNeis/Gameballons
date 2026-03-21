
from abc import ABC,abstractmethod
import pygame.image

from code.Const import WIN_WIDTH
from code.Entity import Entity
from code.Ghost import Ghost
from code.GhostShot import GhostShot
from code.Player import Player
from code.PlayerShot import PlayerShot

class EntityMediator:


    @staticmethod
    def __verify_collision_window(ent:Entity):
        if isinstance(ent, Ghost):
            if ent.rect.right <0:
                ent.health = 0
            #healf th shoot
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, GhostShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Ghost) and isinstance(ent2, PlayerShot):
           valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Ghost):
           valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, GhostShot):
           valid_interaction = True
        elif isinstance(ent1, GhostShot) and isinstance(ent2, Player):
           valid_interaction = True

       #True
        if valid_interaction :
            if (ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom):

              ent1.health -= ent2.damage
              ent2.health -= ent1.damage
              ent1.last_dmg = ent2.name
              ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(ghost: Ghost, entity_list: list[Entity]):
        if ghost.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += ghost.score
        elif ghost.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += ghost.score




    @staticmethod
    def verify_collision(entity_list: list[Entity]):
       for i  in range(len(entity_list)):
           entity1 = entity_list[i]
           EntityMediator.__verify_collision_window(entity1)
           for j in range(i+1,len(entity_list)):
               entity2 = entity_list[j]
               EntityMediator.__verify_collision_entity(entity1,entity2)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Ghost):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
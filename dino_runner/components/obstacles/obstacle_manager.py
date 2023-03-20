import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus_grande import CactusGrande
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import * #O asterisco serve para importar todas as coisas que tenha dentro da classe/arquivo

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):

        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 3) #Random para decidir qual objeto irá aparecer
            #Possibilidades: 
            if random_obstacle == 0:            
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random_obstacle == 1:
                self.obstacles.append(CactusGrande(LARGE_CACTUS))
            elif random_obstacle == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)    #Mover para esquerda e deletar.
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
import pygame

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__(self) -> None:
        self.obstacle = []

    def update(self, game):
        if len(self.obstacle) == 0:
            self.obstacle.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(750)
                game.playing = False
                break

        
    def draw(self, screen):
        for obstacle in self.obstacle:
            obstacle.draw(screen)
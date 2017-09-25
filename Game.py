import pygame
import sys
from Map import Map
from Player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        self.map = Map(self)
        self.player = Player(self, 100, 300)

        while True:
            delta_time = 1 / float(self.clock.tick(60))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            self.update(delta_time, events)
            self.draw(self.screen)
            pygame.display.flip()

    def update(self, delta_time, events):
        self.player.update(delta_time, events)

    def draw(self, screen):
        self.map.draw(screen)
        self.player.draw(screen)

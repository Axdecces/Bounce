import pygame
import sys
from Map import Map
from Input import Input
from Player import Player


class Game:
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    def __init__(self):
        pygame.init()

        self.map = Map(self)
        self.input = Input()
        self.player = Player(self, 100, 300)

        while True:
            delta_time = float(self.clock.tick(60)) / 1000
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
        self.input.update()
        self.player.update(delta_time, events)

    def draw(self, screen):
        self.map.draw(screen)
        self.player.draw(screen)

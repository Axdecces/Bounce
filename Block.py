import pygame


class Block(pygame.Rect):
    def __init__(self, game, x, y, width, height, color):
        super(Block, self).__init__((x, y), (width, height))
        self.game = game
        self.color = color

    def update(self, delta_time, events):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

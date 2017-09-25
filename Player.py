import pygame
from Block import Block


class Player(Block):
    def __init__(self, game, x, y):
        self.player_width = 16
        self.player_height = 32
        super(Player, self).__init__(game, x, y, self.player_width, self.player_height, (255, 0, 0))
        self.is_left = False
        self.is_right = False

        self.velocity = [float(0), float(0)]
        self.max_velocity = float(20)
        self.gravity = [float(0), float(10)]

    def apply_gravity(self, delta_time):
        if self.velocity[0] < self.max_velocity:
            self.velocity[0] += self.gravity[0] * delta_time
        if self.velocity[1] < self.max_velocity:
            self.velocity[1] += self.gravity[1] * delta_time

    def keep_in_bounds(self):
        if self.left <= 0:
            self.left = 0
        if self.right >= self.game.width:
            self.right = self.game.width
        if self.top <= 0:
            self.top = 0
        if self.bottom >= self.game.height:
            self.bottom = self.game.height

    def update(self, delta_time, events):
        super(Player, self).update(delta_time, events)
        self.apply_gravity(delta_time)
        self.move_ip(self.velocity[0], self.velocity[1])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_RIGHT]:
            pass
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            pass
        self.keep_in_bounds()

    def draw(self, screen):
        super(Player, self).draw(screen)

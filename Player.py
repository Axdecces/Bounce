import pygame
from Block import Block


class Player(Block):
    def __init__(self, game, x, y):
        self.player_width = 16
        self.player_height = 32
        super(Player, self).__init__(game, x, y, self.player_width, self.player_height, (255, 0, 0))

        self.velocity = [float(0), float(0)]
        self.max_velocity = float(8)
        self.gravity = [float(0), float(10)]
        self.acceleration = [8, 8]
        self.is_jumping = True
        self.is_accelerating = False

    def apply_gravity(self, delta_time):
        self.velocity[0] += self.gravity[0] * delta_time
        self.velocity[1] += self.gravity[1] * delta_time

    def get_input(self, delta_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity[0] -= self.acceleration[0] * delta_time
            self.is_accelerating = True
        if keys[pygame.K_RIGHT]:
            self.velocity[0] += self.acceleration[0] * delta_time
            self.is_accelerating = True

    def check_max_velocity(self):
        if abs(self.velocity[0]) > self.max_velocity:
            if self.velocity[0] > 0:
                self.velocity[0] = self.max_velocity
            if self.velocity[0] < 0:
                self.velocity[0] = -self.max_velocity
        if abs(self.velocity[1]) > self.max_velocity * 2:
            if self.velocity[1] > 0:
                self.velocity[1] = self.max_velocity * 2
            if self.velocity[1] < 0:
                self.velocity[1] = -self.max_velocity * 2

    def move(self, delta_x, delta_y):

        # Move each axis separately. Note that this checks for collisions both times.
        if delta_x != 0:
            self.move_single_axis(delta_x, 0)
        if delta_y != 0:
            self.move_single_axis(0, delta_y)

    def move_single_axis(self, delta_x, delta_y):

        # Move the rect
        self.x += delta_x
        self.y += delta_y

        # If you collide with a wall, move out based on velocity
        for block in self.game.map.blocks:
            if self.colliderect(block):
                if delta_x > 0:  # Moving right; Hit the left side of the wall
                    self.right = block.left
                    self.velocity[0] = -self.velocity[0] * .01
                if delta_x < 0:  # Moving left; Hit the right side of the wall
                    self.left = block.right
                    self.velocity[0] = -self.velocity[0] * .01
                if delta_y > 0:  # Moving down; Hit the top side of the wall
                    self.bottom = block.top
                    self.velocity[1] = -self.velocity[1] * .01
                    if not self.is_accelerating:
                        self.velocity[0] = self.velocity[0] * .2
                    self.is_jumping = False
                if delta_y < 0:  # Moving up; Hit the bottom side of the wall
                    self.top = block.bottom
                    self.velocity[1] = -self.velocity[1] * .01

    def keep_in_bounds(self):
        if self.left <= 0:
            self.left = 1
            self.velocity[0] = -self.velocity[0] * .1
        if self.right >= self.game.width:
            self.right = self.game.width - 1
            self.velocity[0] = -self.velocity[0] * .1
        if self.top <= 0:
            self.top = 1
            self.velocity[1] = -self.velocity[1] * .1
        if self.bottom >= self.game.height:
            self.bottom = self.game.height
            self.velocity[1] = -self.velocity[1] * .1

    def update(self, delta_time, events):
        super(Player, self).update(delta_time, events)
        self.apply_gravity(delta_time)
        self.get_input(delta_time)
        self.check_max_velocity()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.is_jumping:
                    self.velocity[1] -= 15
                    self.is_jumping = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.is_accelerating = False
                if event.key == pygame.K_LEFT and not self.is_jumping:
                    self.velocity[0] = 0
                if event.key == pygame.K_RIGHT and not self.is_jumping:
                    self.velocity[0] = 0
        self.move(self.velocity[0], self.velocity[1])
        self.keep_in_bounds()

    def draw(self, screen):
        super(Player, self).draw(screen)

from Debug import Debug
from Block import Block
from Physics import Physics


class Player(Block):
    player_width = 16
    player_height = 32

    velocity_x = float(0)
    velocity_y = float(0)
    gravity_x = float(0)
    gravity_y = float(30)
    acceleration_x = float(20)
    acceleration_y = float(500)
    direction = 1
    max_velocity_x = 8
    max_velocity_y = 30
    is_blocked_left = False
    is_blocked_right = False
    is_blocked_top = False
    is_on_ground = False
    physic = Physics()

    def __init__(self, game, x, y):
        self.player_width = 16
        self.player_height = 32
        super(Player, self).__init__(game, x, y, self.player_width, self.player_height, (255, 0, 0))

        self.x_raw = float(self.x)
        self.y_raw = float(self.y)

        self.debug_1 = Debug(0, 0)
        self.debug_2 = Debug(50, 0)

        self.debug_value_1 = ''
        self.debug_value_2 = ''

    def move(self, x=0, y=0, delta_time=0):
        # TODO: get raw_x for exact calculations
        if abs(self.velocity_y) < self.max_velocity_y:
            self.velocity_y += self.gravity_y * delta_time

        if self.game.input.jump and self.is_on_ground:
            self.velocity_y = 0
            self.velocity_y -= self.acceleration_y * delta_time
            self.is_on_ground = False

        self.y += self.velocity_y

        for block in self.game.map.blocks:
            self.physic.collide_y(self, block)

        if self.game.input.is_exclusive_direction():
            if self.game.input.right:
                if self.velocity_x < 0 and self.is_on_ground:
                    self.velocity_x = 0
                if self.velocity_x <= self.max_velocity_x:
                    self.velocity_x += self.acceleration_x * delta_time
                if self.velocity_x > self.max_velocity_x:
                    self.velocity_x = self.max_velocity_x
            else:
                if self.velocity_x > 0 and self.is_on_ground:
                    self.velocity_x = 0
                if abs(self.velocity_x) <= self.max_velocity_x:
                    self.velocity_x -= self.acceleration_x * delta_time
                if abs(self.velocity_x) > self.max_velocity_x:
                    self.velocity_x = -self.max_velocity_x

        self.x += self.velocity_x

        for block in self.game.map.blocks:
            self.physic.collide_x(self, block)

    def update(self, delta_time, events):
        super(Player, self).update(delta_time, events)
        self.move(delta_time=delta_time)

    def draw(self, screen):
        super(Player, self).draw(screen)
        self.debug_1.draw(self.debug_value_1, screen)
        self.debug_2.draw(self.debug_value_2, screen)

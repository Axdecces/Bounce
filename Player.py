import sys
from Block import Block
from Physics import Physics


class Player(Block):
    player_width = 16
    player_height = 32
    color = (97, 169, 188)

    velocity_x = float(0)
    velocity_y = float(0)
    gravity_x = float(0)
    gravity_y = float(30)
    acceleration_x = float(100)
    acceleration_y = float(500)
    direction = 1
    max_velocity_x = 7
    max_velocity_y = 30
    is_blocked_left = False
    is_blocked_right = False
    is_blocked_top = False
    is_on_ground = False
    physic = Physics()

    def __init__(self, game, x, y):
        self.player_width = 16
        self.player_height = 32
        super(Player, self).__init__(game, x, y, self.player_width, self.player_height, self.color)

        self.x_raw = float(self.x)
        self.y_raw = float(self.y)

        self.debug_value_1 = ''
        self.debug_value_2 = ''


    def update(self, delta_time, events):
        super(Player, self).update(delta_time, events)
        self.move(delta_time=delta_time)

    def draw(self, screen):
        super(Player, self).draw(screen)

    def move(self, x=0, y=0, delta_time=0):
        self.apply_gravity(delta_time)

        self.jump(delta_time)

        self.detect_objective_y()

        self.move_y()

        self.walk(delta_time)

        self.detect_objective_x()

        self.move_x()

    def apply_gravity(self, delta_time):
        if abs(self.velocity_y) < self.max_velocity_y:
            self.velocity_y += self.gravity_y * delta_time

    def jump(self, delta_time):
        if self.game.input.jump and self.is_on_ground:
            self.velocity_y = 0
            self.velocity_y -= self.acceleration_y * delta_time
            self.is_on_ground = False

    def detect_objective_y(self):
        self.is_on_ground = False
        self.is_blocked_top = False

        for objective in self.game.map.objectives:
            self.physic.detect_collision_y(self, objective)
            if self.is_on_ground or self.is_blocked_top:
                sys.exit()

    def move_y(self):
        self.y_raw += self.velocity_y
        self.y = round(self.y_raw, 0)

        for block in self.game.map.blocks:
            self.physic.detect_collision_y(self, block)
            self.physic.resolve_collision_y(self, block)

        self.y = round(self.y_raw, 0)

    def walk(self, delta_time):
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

    def detect_objective_x(self):
        if self.is_on_ground:
            self.velocity_x = self.velocity_x * .8

        self.is_blocked_left = False
        self.is_blocked_right = False

        for objective in self.game.map.objectives:
            self.physic.detect_collision_x(self, objective)
            if self.is_blocked_left or self.is_blocked_right:
                sys.exit()

    def move_x(self):
        self.x_raw += self.velocity_x
        self.x = round(self.x_raw, 0)

        for block in self.game.map.blocks:
            self.physic.detect_collision_y(self, block)
            self.physic.resolve_collision_x(self, block)

        self.x = round(self.x_raw, 0)

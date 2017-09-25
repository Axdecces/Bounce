from Block import Block


class Ground(Block):
    def __init__(self, game, x, y, width, height):
        self.color = (100, 100, 100)
        Block.__init__(self, game,  x, y, width, height, self.color)

    def update(self, delta_time, events):
        super(Ground, self).update(delta_time, events)

    def draw(self, screen):
        super(Ground, self).draw(screen)

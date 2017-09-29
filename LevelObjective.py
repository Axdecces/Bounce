from Block import Block

class LevelObjective(Block):
    color = (255, 255, 255)
    def __init__(self, game, x, y, width, height):
        super(LevelObjective, self).__init__(game, x, y, width, height, self.color)

    def update(self, delta_time, events):
        super(LevelObjective, self).update(delta_time, events)

    def draw(self, screen):
        super(LevelObjective, self).draw(screen)
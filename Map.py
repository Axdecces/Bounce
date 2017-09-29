from Ground import Ground
from LevelObjective import LevelObjective


class Map:
    def __init__(self, game):
        self.game = game
        self.background_color = (200, 200, 200)
        self.blocks = [
            Ground(self.game, 0, self.game.height - 50, self.game.width, 50),
            Ground(self.game, 0, self.game.height - 100, 500, 50),
            Ground(self.game, -20, -20, 20, self.game.height + 20),
            Ground(self.game, self.game.width, -20, 20, self.game.height + 20),
            Ground(self.game, self.game.width - 27, self.game.height - 88, 7, 33)
        ]

        self.objectives = [
        ]

    def draw(self, screen):
        self.map = self.game.screen.fill(self.background_color)
        for block in self.blocks:
            block.draw(screen)
        for objective in self.objectives:
            objective.draw(screen)

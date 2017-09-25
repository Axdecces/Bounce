from Ground import Ground


class Map:
    def __init__(self, game):
        self.game = game
        self.background_color = (200, 200, 200)
        self.blocks = [
            Ground(self.game, 0, self.game.height - 50, self.game.width, 50),
            Ground(self.game, 0, self.game.height - 100, 500, 50)
        ]

    def draw(self, screen):
        self.map = self.game.screen.fill(self.background_color)
        for block in self.blocks:
            block.draw(screen)

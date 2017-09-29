import pygame


class Debug:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.font = pygame.font.Font('joystix monospace.ttf', 16)
        self.show_debug = True

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.show_debug = True
                if event.key == pygame.K_F2:
                    self.show_debug = False

    def draw(self, screen):
        if self.show_debug:
            text_iterations = self.font.render(str(self.value), False, (255, 0, 0))
            screen.blit(
                source=text_iterations,
                dest=(self.x, self.y)
            )

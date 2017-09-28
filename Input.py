import pygame


class Input:
    def __init__(self):
        self.keys = {
            'left' : pygame.K_LEFT,
            'right' : pygame.K_RIGHT,
            'jump' : pygame.K_UP
        }
        self.set_initial_states()

    def set_initial_states(self):
        self.left = False
        self.right = False
        self.jump = False

    def is_exclusive_direction(self):
        return (
            (self.left and not self.right)
            or
            (self.right and not self.left)
        )

    def update(self):
        self.set_initial_states()

        keys = pygame.key.get_pressed()
        if keys[self.keys['left']]:
            self.left = True
        if keys[self.keys['right']]:
            self.right = True
        if keys[self.keys['jump']]:
            self.jump = True
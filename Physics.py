class Physics:

    def __init__(self):
        pass

    def collide_x(self, moving_rect, fixed_rect):
        if moving_rect.colliderect(fixed_rect):
            if moving_rect.velocity_x > 0:
                moving_rect.right = fixed_rect.left
                moving_rect.velocity_x = 0
            else:
                moving_rect.left = fixed_rect.right
                moving_rect.velocity_x = 0

    def collide_y(self, moving_rect, fixed_rect):
        if moving_rect.colliderect(fixed_rect):
            if moving_rect.velocity_y > 0:
                moving_rect.bottom = fixed_rect.top
                moving_rect.is_on_ground = True
            else:
                moving_rect.top = fixed_rect.bottom

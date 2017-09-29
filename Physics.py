class Physics:
    def __init__(self):
        pass

    def detect_collision_x(self, moving_rect, fixed_rect):
        if moving_rect.colliderect(fixed_rect):
            if moving_rect.velocity_x > 0:
                moving_rect.is_blocked_right = True
            else:
                moving_rect.is_blocked_left = True

    def detect_collision_y(self, moving_rect, fixed_rect):
        if moving_rect.colliderect(fixed_rect):
            if moving_rect.velocity_y > 0:
                moving_rect.is_on_ground = True
            else:
                moving_rect.is_blocked_top = True

    def resolve_collision_x(self, moving_rect, fixed_rect):
        if moving_rect.colliderect(fixed_rect):
            if moving_rect.velocity_x > 0:
                moving_rect.x_raw = fixed_rect.left - moving_rect.player_width
                moving_rect.velocity_x = 0
            else:
                moving_rect.x_raw = fixed_rect.right
                moving_rect.velocity_x = 0

    def resolve_collision_y(self, moving_rect, fixed_rect):
        if moving_rect.colliderect(fixed_rect):
            if moving_rect.velocity_y > 0:
                moving_rect.y_raw = fixed_rect.top - moving_rect.player_height
            else:
                moving_rect.y_raw = fixed_rect.bottom
                moving_rect.velocity_y = 0

import pygame
import time


def save_screenshot(game):
    timestamp = int(time.time())
    pygame.image.save(game.screen, str(timestamp) + ".png")

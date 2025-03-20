import pygame
import random

from utils.utils import generate_random_color

class DVD:
    def __init__(self, text, font_size, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.SysFont(None, font_size)
        self.text = text
        self.color = generate_random_color()
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center=(screen_width // 2, screen_height // 2))
        self.speed_x = random.choice([1, -1])
        self.speed_y = random.choice([1, -1])


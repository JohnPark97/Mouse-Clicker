import pygame

class Square():
    def __init__(self, x, y, surface: pygame.Surface, colour):
        self.x = x
        self.y = y
        self.surface = surface
        self.surface.fill(colour)
        self.mask = pygame.mask.from_surface(self.surface)
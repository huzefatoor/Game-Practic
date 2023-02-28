import pygame

class Spritesheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width, height, scale, colour):
        image = pygame.surface((width,height)).convert_alpha()
        
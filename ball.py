import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, settings, screen):
        super(Ball, self).__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('ball.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.speed = self.settings.speed_ball

    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top > self.settings.screen_h-30 or self.rect.bottom < 30:
            self.speed[1] = -self.speed[1]

    def blit_screen(self):
        self.screen.blit(self.image, self.rect)
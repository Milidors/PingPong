import pygame
from pygame.sprite import Sprite


class Player2(Sprite):
    def __init__(self, setting, screen):
        super(Player2, self).__init__()
        self.screen = screen
        self.settings = setting
        self.rect = pygame.Rect(0, 0, self.settings.plat_w,
                                self.settings.plat_h)
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left+20
        self.center = float(self.rect.centery)
        self.color = self.settings.plat_color
        self.speed_plat = self.settings.plat_speed
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.center -= self.speed_plat
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.speed_plat
        self.rect.centery = self.center

    def draw_player(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
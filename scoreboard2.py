import pygame.font
pygame.font.init()


class Scoreboard2():
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font(None, 48)
        self.prep_score()

    def prep_score(self):
        score_str_1 = str(self.stats.score_p2)
        self.score_img = self.font.render(score_str_1, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
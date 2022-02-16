import pygame
from settings import Settings
import game_func as gf
from player2 import Player2
from player import Player
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from scoreboard2 import Scoreboard2


def run_game():

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_w, settings.screen_h))
    pygame.display.set_caption(settings.name)
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    sb2 = Scoreboard2(settings, screen, stats)
    player = Player(settings, screen)
    player2 = Player2(settings, screen)
    ball = Group()


    while True:
        gf.check_event(player, player2)

        player.update()
        player2.update()
        ball.update()
        gf.ball_update(settings, screen,player, player2, ball, stats, sb, sb2)
        gf.update_screen(settings, screen, player, player2, ball, sb, sb2)


run_game()
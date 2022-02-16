import pygame
import sys
from ball import Ball


def check_event(player, player2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event, player, player2)

        elif event.type == pygame.KEYUP:
            check_event_keyup(event, player, player2)


def check_event_keydown(event, player, player2):
    if event.key == pygame.K_UP:
        player.move_up = True

    elif event.key == pygame.K_DOWN:
        player.move_down = True

    if event.key == pygame.K_w:
        player2.move_up = True

    elif event.key == pygame.K_s:
        player2.move_down = True


def check_event_keyup(event, player, player2):
    if event.key == pygame.K_UP:
        player.move_up = False

    elif event.key == pygame.K_DOWN:
        player.move_down = False

    if event.key == pygame.K_w:
        player2.move_up = False

    elif event.key == pygame.K_s:
        player2.move_down = False


def update_screen(settings, screen, player, player2, ball, sb, sb2):
    pygame.init()
    screen.fill(settings.bg_color)
    player.draw_player()
    player2.draw_player()
    create_ball(settings, screen, ball)
    sb.show_score()
    sb2.show_score()
    pygame.display.flip()


def create_ball(settings, screen, ball):
    if len(ball) == 0:
        new_ball = Ball(settings, screen)
        ball.add(new_ball)

    for balls in ball.sprites():
        balls.blit_screen()


def ball_update(settings, screen, player, player2, ball, stats, sb, sb2):
    ball.update()
    screen_rect = screen.get_rect()
    for balls in ball:

        if balls.rect.right >= screen_rect.right:
            ball.remove(balls)
            settings.speed_ball[0] = -settings.speed_ball[0]
            stats.score_p1 += settings.goal
            sb.prep_score()

        elif balls.rect.left <= screen_rect.left:
            ball.remove(balls)
            settings.speed_ball[0] = -settings.speed_ball[0]
            stats.score_p2 += settings.goal
            sb2.prep_score()
    check_collision(settings, player, player2, ball)


def check_collision(settings, player, player2, ball):
    if pygame.sprite.spritecollideany(player, ball):
        settings.speed_ball[0] = -settings.speed_ball[0]

    if pygame.sprite.spritecollideany(player2, ball):
        settings.speed_ball[0] = -settings.speed_ball[0]











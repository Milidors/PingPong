class Settings:
    def __init__(self):
        self.screen_w = 1500
        self.screen_h = 800
        self.bg_color = (255, 255, 255)
        self.name = 'Pin_Pong'
        self.plat_w = self.screen_w / 50
        self.plat_h = self.screen_h / 4
        self.plat_color = (60, 60, 60)
        self.plat_speed = 3
        self.direction = 1
        self.speed_ball = [1, 1]
        self.goal = 1

import random

from game.dvd_colors import DvdColors


class KickText(DvdColors):
    def __init__(self, text, font_size, screen_width, screen_height):
        super().__init__(text, font_size, screen_width, screen_height)
        self.initMoveValues()

    def initMoveValues(self):
        self.LEFT = [0, 1, -1, 1]
        self.RIGHT = [-1, 0, 1, 1]
        self.TOP = [-1, 1, 0, 1]
        self.BOTTOM = [-1, 1, -1, 0]

    def onKick(self, values):
        self.speed_x = random.randint(values[0], values[1])
        self.speed_y = random.randint(values[2], values[3])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.onKick(self.LEFT)
            self.change_color()  

        if self.rect.right >= self.screen_width:
            self.onKick(self.RIGHT)
            self.change_color()  

        if self.rect.top <= 0:
            self.onKick(self.TOP)
            self.change_color()  

        if self.rect.bottom >= self.screen_height:
            self.onKick(self.BOTTOM)
            self.change_color()  

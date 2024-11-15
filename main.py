# main.py
import pyxel
import config

class BallGame:
    def __init__(self):
        pyxel.init(160, 120, title="Bouncing Ball")
    
        self.ball_x = 80
        self.ball_y = 60
        self.ball_dx = 2
        self.ball_dy = 2
        self.paddle_x = 70
        self.paddle_y = 110
        self.paddle_width = config.PADDLE_WIDTH
        self.paddle_height = config.PADDLE_HEIGHT
        pyxel.run(self.update, self.draw)

    def update(self):
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        if self.ball_x < 0 or self.ball_x > 160:
            self.ball_dx *= -1
        if self.ball_y < 0 or self.ball_y > 120:
            self.ball_dy *= -1

        if self.paddle_x < 0:
            self.paddle_x = 0
        if self.paddle_x + self.paddle_width > 160:
            self.paddle_x = 160 - self.paddle_width

        if (self.paddle_y < self.ball_y < self.paddle_y + self.paddle_height and
            self.paddle_x < self.ball_x < self.paddle_x + self.paddle_width):
            self.ball_dy *= -1

        if pyxel.btn(pyxel.KEY_LEFT):
            self.paddle_x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.paddle_x += 2

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.ball_x, self.ball_y, 2, 7)
        pyxel.rect(self.paddle_x, self.paddle_y, self.paddle_width, self.paddle_height, 7)

BallGame()

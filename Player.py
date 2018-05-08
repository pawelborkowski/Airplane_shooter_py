import pygame
from pygame.math import Vector2


class Rocket(object):

    def __init__(self, game):
        pygame.init()
        self.game = game
        self.size = self.game.screen.get_size()
        self.speed = self.size[0] / 200
        self.vel = Vector2(self.speed, 0)
        self.touch_r = False
        self.touch_l = False
        self.margin = self.size[0] / 20
        self.player_size = self.size[0] / 75
        self.points = [Vector2(0, -self.player_size),
                       Vector2(self.player_size, self.player_size),
                       Vector2(-self.player_size, self.player_size)]
        self.pos = Vector2(self.size[0] / 2, self.size[1] * (5/6))

    def update(self):
        self.size = self.game.screen.get_size()
        self.speed = self.size[0] / 200
        self.vel = Vector2(self.speed, 0)
        self.margin = self.size[0] / 20
        self.player_size = self.size[0] / 75
        self.points = [Vector2(0, -self.player_size),
                       Vector2(self.player_size, self.player_size),
                       Vector2(-self.player_size, self.player_size)]
        self.pos.y = self.size[1] * (5/6)

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and not self.touch_r:
            self.pos += self.vel

        elif pressed[pygame.K_LEFT] and not self.touch_l:
            self.pos -= self.vel

    def draw(self):
        self.update()
        pic = pygame.image.load("air_plane.png")
        self.game.screen.blit(pygame.transform.scale(pic, (15, 15)), (0, 0))

        if self.pos.x + self.points[2].x <= self.margin:
            points = [Vector2(self.margin + self.vel.x, self.size[1] * (5 / 6)) + p for p in self.points]
            self.touch_l = True
            self.touch_r = False

        elif self.pos.x + self.points[1].x >= self.size[0] - self.margin:
            points = [Vector2(self.size[0] - self.margin - self.vel.x, self.size[1] * (5 / 6)) + p for p in self.points]
            self.touch_r = True
            self.touch_l = False

        else:
            points = [self.pos + p for p in self.points]
            self.touch_r = False
            self.touch_l = False

        pygame.draw.polygon(self.game.screen, (0, 255, 0), points)

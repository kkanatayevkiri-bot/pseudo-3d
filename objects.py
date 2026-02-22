import pygame as pg
from math import atan2, tau, hypot,cos
from settings import*


class Ren_objects:
    def __init__(self,game,direction="D:/Python/Wolfenstein/table.webp",position=(1.5,1.5)):
        pg.init()
        self.game = game
        self.tex = pg.image.load(direction).convert_alpha()
        self.half_tex = self.tex.get_width() // 2
        self.img_ratio = self.half_tex / self.tex.get_height()
        self.x, self.y = position

    def generate_object(self):
        self.height_object = SCREEN_DIS / self.del_dist
        #debugg
        # print(self.del_angle)
        # print(tan(self.del_angle))

        # self.object_width = self.height_object * tan(self.del_angle) #<-- this made the truble

        # print(self.height_object, self.object_width) #<--- width return a negative num that crashes the program! FIXED!!! the bug (self.px - self.x) = -x? we want the distance from the
        #sprite to the player! (self.px - self.x) = x (6-1) = 5
        #debugg
        self.object_width = self.height_object * self.img_ratio
        image = pg.transform.scale(self.tex,(self.object_width,self.height_object))
        pos = self.screen_x - (self.object_width // 2), HALF_HEGIHT - (self.height_object // 2)
        self.game.raytracing.objects.append((image,pos,self.del_dist))

    def calculate_object(self):
        px, py = self.game.player.pos
        dx, dy = self.x - px , self.y - py
        player_a = self.game.player.angle

        object_a = atan2(dy, dx)
        self.del_angle = object_a - player_a
        if (dx < 0 and player_a > tau) or (dx < 0 and dy < 0):
            self.del_angle += tau

        del_rays = self.del_angle / ANGLE_DELTA
        self.screen_x = (HALF_NUM_RAYS + del_rays) * SCALE
        self.del_dist = hypot(dx, dy)
        self.del_dist = self.del_dist * cos(self.del_angle)
        # print(self.del_angle)

        if -self.half_tex < self.screen_x < (X + self.half_tex) and self.del_dist > 0.5:
            self.generate_object()

    def update(self):
        self.calculate_object()
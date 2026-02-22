import pygame as pg
import math
from settings import*

class Player:
    def __init__(self,game):
        pg.init()
        self.game = game
        self.x,self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    @property
    def pos(self):
        return self.x, self.y
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    
    def movement(self):
        a_cos = math.cos(self.angle)
        a_sin = math.sin(self.angle)
        dx,dy = 0,0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * a_sin
        speed_cos = speed * a_cos

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.try_move(dx,dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
    
    def try_move(self,dx,dy):
        player_scale = 60 / self.game.delta_time

        if not self.is_wall(int(self.x + dx * player_scale), int(self.y)):
            self.x += dx
        if not self.is_wall(int(self.x), int(self.y + dy * player_scale)):
            self.y += dy

    def is_wall(self,dx,dy):
        return (dx,dy) in self.game.m.world

    def mouse_contol(self):
        mouse_pos = pg.mouse.get_pos()
        mx, my = mouse_pos
        if mx < BORDER_LEFT or mx > BORDER_RIGHT:
            pg.mouse.set_pos(HALF_WIDTH,HALF_HEGIHT)
        self.mouse_rel = pg.mouse.get_rel()[0]
        self.mouse_rel = max(-MAX_REL,min(MAX_REL,self.mouse_rel))
        self.angle += self.mouse_rel * MOUSE_SPEED * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_contol()

    def draw(self):
        pass

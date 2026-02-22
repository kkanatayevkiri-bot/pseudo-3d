import pygame as pg
import sys
from settings import*
from player import*
from raytracing import*
from map import*
from object_ren import*
from objects import*



class DinoShooter:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.mouse.set_visible(0)
        self.delta_time = 1
        self.new_game()# Create the map ONCE!

    def new_game(self):
        self.m = Map(self) #Here we place the things that we DO NOT want to loop! one call is just anougth!
        self.renderObject = Objectrenderer(self)
        self.player = Player(self)
        self.raytracing = Raytracing(self)
        self.ob = Ren_objects(self)
        
    def update(self):
        self.player.update()
        self.raytracing.update()
        self.ob.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps():.0f}")

    def draw(self):
        self.window.fill((0,0,0))
        self.m.draw()
        self.player.draw()
        self.renderObject.draw()

    def keyboard(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.run = False
                    sys.exit()

    def run(self):
        while True:
            self.keyboard()
            self.update()
            self.draw()


if __name__ == "__main__":
    g = DinoShooter()
    g.run()
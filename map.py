import pygame as pg

map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,2,0,0,0,3,0,0,0,1],
     [1,0,0,0,0,0,0,2,0,0,0,3,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,0,0,3,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,0,0,3,0,0,0,1],
     [1,0,0,0,0,0,0,2,0,0,0,3,0,0,0,1],
     [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

class Map:
    def __init__(self,game):
        self.game = game
        self.m = map
        self.world = {}
        self.create_world()

    def create_world(self):
        for j, row in enumerate(self.m):
            for i, value in enumerate(row):
                if value:
                    self.world[(i,j)] = value #(0,0) = 1, row0 and col0 hold '1' and so on...(for all '1's)

    def draw(self):
        # [pg.draw.rect(self.game.window,('darkgrey'), (pos[0] * 100, pos[1]*100,100,100),2) for pos in self.world]
        pass
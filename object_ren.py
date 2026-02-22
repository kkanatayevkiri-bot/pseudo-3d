import pygame as pg
from settings import*


class Objectrenderer:
    def __init__(self,game):
        self.game = game
        self.window = self.game.window
        self.textures = self.load_texture()
        self.sky_texutre = pg.image.load("D:/Python/Wolfenstein/sky.jpg").convert_alpha()
        self.sky_texutre = pg.transform.scale(self.sky_texutre,(X,HALF_HEGIHT))
        self.sky_offset = 0

    def backgound(self):
        self.sky_offset += self.game.player.mouse_rel
        self.sky_offset %= X
        #sky
        # pg.draw.rect(self.window,(0,255,0),(0,0,X,HALF_HEGIHT)) #test worked, but we can do better!
        self.window.blit(self.sky_texutre,(-self.sky_offset,0))
        self.window.blit(self.sky_texutre,(-self.sky_offset+X,0))
        #floor
        pg.draw.rect(self.window,(0,30,0),(0,HALF_HEGIHT,X,HALF_HEGIHT))

    def draw(self):
        self.backgound()
        self.render_game_object()

    def render_game_object(self):
        render = self.game.raytracing.objects
        for obj in sorted(render ,key = lambda dist:dist[2],reverse=True):
            wall_slice, pos, depth = obj
            self.window.blit(wall_slice,pos)

    def load_texture(self):
        return{
            i:pg.image.load(f"D:/Python/Wolfenstein/{i}.png") for i in range(1,4)
        }
    


# test = Objectrenderer()
# test.textures[1] works
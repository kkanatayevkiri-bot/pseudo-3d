from math import cos,sin
from settings import*
import pygame as pg

class Raytracing:
    def __init__(self,game):
        pg.init()
        self.game = game
        self.process_data = []
        self.objects = []
        self.textures = self.game.renderObject.textures

    def create_process_data(self):
        self.objects = []
        for data in self.process_data:
            # ray, texture, offset, obj_height
            ray, texture, offset, obj_height, depth = data
            if obj_height < Y:
                texture = self.textures[texture].subsurface(offset*(TEXTURE-SCALE),0,SCALE,TEXTURE)
                wall_slice = pg.transform.scale(texture,(SCALE,obj_height))
                wall_pos = (ray*SCALE, HALF_HEGIHT - (obj_height // 2))
            else:
                # tex_height = TEXTURE *  Y / obj_height
                t = TEXTURE* (800 / obj_height)
                y_point = (TEXTURE- t) / 2
                # texture = self.textures[texture].subsurface(offset*(TEXTURE-SCALE),TEXTURE_HALF - tex_height//2,SCALE,tex_height)
                texture = self.textures[texture].subsurface(offset*(TEXTURE-SCALE),y_point,SCALE,t)
                wall_slice = pg.transform.scale(texture,(SCALE,Y))
                wall_pos = (ray*SCALE, 0)
            
            self.objects.append((wall_slice,wall_pos,depth))

    def cast_ray(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        ray_a = self.game.player.angle - (HALF_FOV + 0.0001)

        self.process_data = []
        texture_vert, texture_horz = 1,1
        for ray in range(NUM_RAYS):
            cos_a = cos(ray_a)
            sin_a = sin(ray_a)

            #Verts!
            x_vert,dx = (x_map+1, 1) if cos_a > 0 else (x_map-1e-6, -1)
            vert_depth = (x_vert - ox) / cos_a
            y_vert = oy+vert_depth * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for _ in range(MAX_DEPTH):
                check_vert = int(x_vert),int(y_vert)
                if check_vert in self.game.m.world:
                    texture_vert = self.game.m.world[check_vert]
                    break
                vert_depth += delta_depth
                x_vert += dx
                y_vert += dy

            #Horz
            y_horz,dy = (y_map+1, 1) if sin_a > 0 else (y_map-1e-6, -1)
            horz_depth = (y_horz - oy) / sin_a
            x_horz = ox+horz_depth * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for _ in range(MAX_DEPTH):
                check_horz = int(x_horz),int(y_horz)
                if check_horz in self.game.m.world:
                    texture_horz = self.game.m.world[check_horz]
                    break
                horz_depth += delta_depth
                x_horz += dx
                y_horz += dy

            # print(vert_depth)
            # print(horz_depth) bug fixed: we didn't change the y_vert,x_vert for the Horz! there for it return 0.0 as depth!
            if vert_depth < horz_depth:
                depth,texture = vert_depth, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1-y_vert)
            else:
                depth,texture = horz_depth, texture_horz
                x_horz %= 1
                offset =  (1-x_horz) if sin_a > 0 else x_horz

            depth *= cos(self.game.player.angle - ray_a)
            obj_height = SCREEN_DIS / depth

            self.process_data.append((ray, texture, offset, obj_height, depth))
            # print(self.process_data) we have data generation

            ray_a += ANGLE_DELTA

    def update(self):
        self.cast_ray()
        self.create_process_data()
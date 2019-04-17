import pygame as pg
from definitions import *


# player sprite
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, X=0, Y=0):
        if not self.wall_collision(X, Y):
            Trail(self.game, self.x, self.y)  # shows trail of current path
            self.x += X
            self.y += Y

    # checks for walls and also map boundaries
    def wall_collision(self, X=0, Y=0):
        for wall in self.game.walls:
            if (wall.x == self.x + X and wall.y == self.y + Y or
                self.x + X < 0 or self.y + Y < 0 or (self.x + X) >
                    (WIDTH/TILESIZE)-1 or (self.y + Y) > (HEIGHT/TILESIZE)-1):
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


# computer player sprite
class Computer(Player):
    def __init__(self, game, x, y, path_lst):
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.path = path_lst
            self.i = 1

    def move(self):
        if not self.wall_collision(self.path[self.i][1], self.path[self.i][0]):
            Trail(self.game, self.x, self.y)  # shows trail of current path
            self.x = self.path[self.i][1]
            self.y = self.path[self.i][0]
            self.i += 1

    # checks for walls and also map boundaries for computer movements
    def wall_collision(self, X=0, Y=0):
        for wall in self.game.walls:
            if (wall.x == X and wall.y == Y or
                X < 0 or Y < 0 or X >
                    (WIDTH/TILESIZE)-1 or Y > (HEIGHT/TILESIZE)-1):
                return True
        return False


# "wall" sprite
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


# trail sprite
class Trail(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.trails
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


# finish line sprite
class End(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.finish
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

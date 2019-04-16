import pygame as pg
import sys
from os import path
from definitions import *
from sprites import *
from BensPF import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))  # set window size
        pg.display.set_caption(TITLE)  # set window menu text
        self.clock = pg.time.Clock()  # create Clock object
        pg.key.set_repeat(100, 50)  # (delay, interval)
        self.load_gamemap()  # load gamemap

    def load_gamemap(self):
        dir = path.dirname(__file__)
        self.map = []  # empty list to store map data
        with open(path.join(dir, 'map3.txt'), 'rt') as f:
            for line in f:
                self.map.append(line)  # read in map line-by-line

    # set up for new game
    def new_game(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.trails = pg.sprite.Group()
        self.finish = pg.sprite.Group()

        for row, tiles in enumerate(self.map):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                    self.computer = Computer(self, col, row, short_list)
                if tile == 'X':
                    self.end = End(self, col, row)

    # player win condition
    def player_win(self):
        return self.player.x == self.end.x and self.player.y == self.end.y

    # computer win condition
    def computer_win(self):
        return self.computer.x == self.end.x and self.computer.y == self.end.y

    # game loop
    def game_loop(self):
        self.playing = True
        while self.playing:
            self.time_change = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            if self.player_win():
                print("You reached the goal!")
                self.playing = False
            if self.computer_win():
                print("The computer beat you to the end!")
                self.playing = False

    def quit(self):
        pg.quit()
        sys.exit()

    # update game
    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.window, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.window, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.window.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.window)
        pg.display.flip()

    # handles all events
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(X=-1)
                    self.computer.move()
                    # print([self.player.y, self.player.x])
                    print([self.computer.y, self.computer.x])
                if event.key == pg.K_RIGHT:
                    self.player.move(X=1)
                    self.computer.move()
                    # print([self.player.y, self.player.x])
                    print([self.computer.y, self.computer.x])
                if event.key == pg.K_UP:
                    self.player.move(Y=-1)
                    self.computer.move()
                    # print([self.player.y, self.player.x])
                    print([self.computer.y, self.computer.x])
                if event.key == pg.K_DOWN:
                    self.player.move(Y=1)
                    self.computer.move()
                    # print([self.player.y, self.player.x])
                    print([self.computer.y, self.computer.x])

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
shortest = path_find()
short_list = shortest[1]
while True:
    g.new_game()
    g.game_loop()
    g.show_go_screen()

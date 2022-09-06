import sys
import pygame as pg
from settings import *


class Game:
    def __init__(self):
        pg.init()
        # uncomment following line for full-screen
        # self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.FULLSCREEN)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # windowed
        pg.display.set_caption(TITLE + ' by ' + AUTHORS)
        self.screen.fill(WHITE)
        self.clock = pg.time.Clock()
        # random git test comment

    def draw_toilet(self):
        # draw bowl
        pg.draw.ellipse(self.screen, BLACK, (TOILET_START_X, TOILET_START_Y, TOILET_WIDTH, TOILET_HEIGHT),
                        TOILET_OUTLINE_WIDTH)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    # use 'q' to exit full-screen
                    if event.key == pg.K_q:
                        pg.quit()
                        sys.exit()

            self.draw_toilet()
            dt = self.clock.tick() / 1000   # sort out delta time
            pg.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.run()

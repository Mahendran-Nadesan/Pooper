import sys
import pygame as pg
from toilet import Toilet
from settings import *


class Game:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.toilet = Toilet()

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

            self.toilet.draw_toilet()
            self.toilet.draw_toilet_water()
            dt = self.clock.tick() / 1000  # sort out delta time
            pg.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.run()

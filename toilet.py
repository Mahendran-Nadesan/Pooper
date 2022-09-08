import sys
import time
import pygame as pg
from settings import *


class Toilet:
    def __init__(self):
        # pygame
        pg.init()
        # uncomment following line for full-screen
        # self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.FULLSCREEN)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # windowed
        pg.display.set_caption(TITLE + ' by ' + AUTHORS)
        self.screen.fill(WHITE)
        # self.clock = pg.time.Clock() # there is a clock in game, do we need it in here?

        # toilet initialisation
        self.water_level = 0
        self.start_time = time.time()

    # Draw methods
    def draw_toilet(self):
        # draw bowl
        pg.draw.ellipse(self.screen, BLACK, (INNER_BOWL_START_X, INNER_BOWL_START_Y, INNER_BOWL_WIDTH,
                                             INNER_BOWL_HEIGHT), TOILET_OUTLINE_WIDTH)
        pg.draw.ellipse(self.screen, BLACK, (OUTER_BOWL_START_X, OUTER_BOWL_START_Y, OUTER_BOWL_WIDTH
                                             , OUTER_BOWL_HEIGHT), TOILET_OUTLINE_WIDTH)

    def draw_toilet_water(self):
        # can't go past max level of water
        if (self.water_level < MAX_LEVELS) and (time.time() - self.start_time > self.water_level * TIME_PER_LEVEL):
            self.water_level += 1
            pg.draw.ellipse(self.screen, TOILET_WATER_BLUE, (self.get_water_start_x(), self.get_water_start_y(),
                                                             self.get_water_width(), self.get_water_height()), 0)

    # Helper methods
    def get_water_start_x(self):
        return (SCREEN_WIDTH - (self.get_water_width())) / 2

    def get_water_start_y(self):
        return (SCREEN_HEIGHT - (self.get_water_height())) / 2

    def get_water_width(self):
        return (INNER_BOWL_WIDTH / MAX_LEVELS) * self.water_level

    def get_water_height(self):
        return (INNER_BOWL_HEIGHT / MAX_LEVELS) * self.water_level

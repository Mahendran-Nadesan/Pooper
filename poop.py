import sys
import time
import pygame as pg
from settings import *


class Poop(pg.sprite.Sprite):
    def __init__(self):
        self.image = ''
        self.in_water = False

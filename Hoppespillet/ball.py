import pygame as pg

class Ball:
    def __init__(self):
        self._pos_x = 20
        self._pos_y = 20

    def tegn(self, vindu):
        pg.draw.circle(vindu, (100,50,140), (self._pos_x,self._pos_y), 25)
        # pg.draw.circle(vindu, (rød,grønn,blå), (x,y), radius)


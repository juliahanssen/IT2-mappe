from figur import Figur
import pygame as pg

class Spiller(Figur):
    def __init__(self, x ,y, fartY):
        super().__init__(x, y)
        self._fartY = fartY

    def tegn(self, vindu):
        pg.draw.circle(vindu, (100,50,140), (self._x,self._y), 25)
    
    def hopp():
        pass
    
    def fall():
        pass

    def er_over_hinder():
        pass
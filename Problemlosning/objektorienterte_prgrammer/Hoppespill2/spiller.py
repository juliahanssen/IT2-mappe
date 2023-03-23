from figur import Figur
import pygame as pg

class Spiller(Figur):
    def __init__(self, x ,y, fartY):
        super().__init__(x, y)
        self._fartY = fartY

    def tegn_spiller(self, vindu):
        pg.draw.circle(vindu, (100,50,140), (self._x,self._y), 25)
    
    def hopp(self):
        self._y -= 5
    
    def fall(self):
        self._y +=1

    def er_over_hinder():
        pass
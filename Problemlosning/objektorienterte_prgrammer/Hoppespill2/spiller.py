from figur import Figur
from hinder import Hinder
import pygame as pg

class Spiller(Figur):
    def __init__(self, x ,y, fartY):
        super().__init__(x, y)
        self._fartY = fartY
        self._radius = 25
        self._poeng = 0

    def tegn_spiller(self, vindu):
        pg.draw.circle(vindu, (100,50,140), (self._x,self._y), self._radius)
    
    def hopp(self):
        self._y -= 5
    
    def fall(self):
        if self._y < 720 - self._radius:
             self._y +=1

    #def poeng(self):
        #if self._y > hinder._hoyde_topp and self._y < hinder._hoyde_bunn:
            #self._poeng +=1

    #def er_over_hinder(self):
        #if self._y < hinder._hoyde_topp or self._y > hinder._hoyde_bunn:
            #return True
from figur import Figur
import pygame as pg
from random import randint

class Hinder(Figur):
    def __init__(self, x, y, fartX):
        super().__init__(x, y)
        self._fartX = fartX
        self._hoyde = randint(20,100)
        self._bredde = 10
    
    def tegn_hinder(self, vindu):
        pg.draw.rect(vindu, (180,40,70),(self._x, self._y,self._bredde, self._hoyde))

    def flytt_venstre():
        pass
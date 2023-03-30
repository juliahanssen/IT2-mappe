from figur import Figur
import pygame as pg
from random import randint

class Hinder(Figur):
    def __init__(self, x, y, fartX):
        super().__init__(x, y)
        self._fartX = fartX
        self._hoyde_bunn = randint(20,400)
        self._hoyde_topp = randint(20,300)
        self._bredde = 90
        self._y = 720 - self._hoyde_bunn
    
    def tegn_hinder(self, vindu):
        pg.draw.rect(vindu, (180,40,70),(self._x, 0,self._bredde, self._hoyde_topp))
        pg.draw.rect(vindu, (180,40,70),(self._x, self._y,self._bredde, self._hoyde_bunn))


    def flytt_venstre(self):
        self._x -= 1

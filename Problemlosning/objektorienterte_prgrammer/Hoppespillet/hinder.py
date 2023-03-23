import pygame as pg
from random import randint

class Hinder:
    def __init__(self):
        self._pos_x = 300
        self._hoyde = randint(20,100)
        self._pos_y = 500 - self._hoyde
        self._bredde = 10
    
    def tegn_hinder(self, vindu):
        pg.draw.rect(vindu, (180,40,70),(self._pos_x, self._pos_y,self._bredde, self._hoyde))
        # pg.draw.rect(vindu, (rød,grønn,blå),(x,y,bredde,høyde))
    
    def flytt_venstre(self):
        self._pos_x -= 1

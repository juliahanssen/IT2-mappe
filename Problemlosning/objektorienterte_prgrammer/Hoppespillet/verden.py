import pygame as pg
from ball import Ball
from hinder import Hinder
import time

ball1 = Ball()
hindere = []

for i in range(3):
    nytt_hinder = Hinder()
    hindere.append(nytt_hinder)

pg.init
VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((255,255,255)) # farger bakgrunnen hvit # vindu.fill((rød,grønn,blå)) # andel rød, grønn, blå mellom 0-255

    for hinder in hindere:
        hinder.flytt_venstre()
        hinder.tegn_hinder(vindu)
    ball1.tegn(vindu)
    pg.display.flip() # Oppdaterer pygame-vinduet Denne MÅ være med
    time.sleep(1/60)

pg.quit() # avslutter pygame
print("Ferdig!")
# Example file showing a basic pygame "game loop"
import pygame as pg
from spiller import Spiller
from hinder import Hinder
from random import randint

# pygame setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

spiller = Spiller(70,600,50)
hindere = []

for i in range(3):
    nytt_hinder = Hinder(1260, 600, 10)
    hindere.append(nytt_hinder)

frame = 0

poeng = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")

    # LAG SPILLET DIT HER:

    spiller.tegn_spiller(screen)
    if frame == 300:
        frame = 0 
        nytt_hinder = Hinder(1260, 600, 10)
        hindere.append(nytt_hinder)

    for hinder in hindere:
        hinder.tegn_hinder(screen)
        hinder.flytt_venstre()
        if spiller._x > hinder._x and spiller._x < hinder._x + 90:
            if spiller._y > hinder._hoyde_topp and spiller._y < hinder._hoyde_bunn:
                poeng += 0.01
    

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        spiller.hopp()

    spiller.fall()

    font = pg.font.Font(None, 36) 
    poeng_text = font.render(f'Poeng: {poeng}', True, (255, 255, 255)) 
    screen.blit(poeng_text, (10, 10))

    if spiller._y < hinder._hoyde_topp or spiller._y > hinder._hoyde_bunn:
        print("tapt")
    

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

    frame += 1

pg.quit()
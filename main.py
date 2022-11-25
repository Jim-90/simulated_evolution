# TODO:
#   Remove microbe when energy reach zero
#   Continously add food
#   Comment code

import pygame, sys
import game_functions as gf

from settings import Settings
from rules import Rules
from microbe import Microbe
from prey import Prey

def main():
    pygame.init()

    clock = pygame.time.Clock()
    settings = Settings()
    rules = Rules()

    screen = pygame.display.set_mode(size=(settings.screen_width, settings.screen_height), flags=pygame.RESIZABLE)
    screen.fill(settings.bg_color)
    #game = pygame.display.set_mode(size=(settings.game_width, settings.game_height))

    pygame.display.set_caption("Simulated evolution!")

    init_microbes = 30
    microbes = []
    food = []

    xy_pos = gf.generate_microbe_positions(settings, init_microbes)
    food_pos = gf.generate_random_food(settings, 0.4)

    for xy in xy_pos:
        microbes.append(Microbe(settings, screen, rules, xy))
    for xy in food_pos:
        food.append(Prey(settings, screen, xy))

    while True:

        gf.check_event()
        gf.update_microbes(settings, screen, rules, microbes, food_pos, food)
        gf.update_screen(screen, settings, microbes, food)
        print(len(microbes))
        clock.tick(30)

if '__main__' == __name__:
    main()
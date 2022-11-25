import random
import pygame

class Prey():

    def __init__(self, settings, screen, init_pos) -> None:
        
        self.settings = settings
        self.screen = screen
        self.pos_x = init_pos[0]
        self.pos_y = init_pos[1]

        self.rect = pygame.Rect(self.pos_x*self.settings.xscale, self.pos_y*self.settings.yscale, self.settings.foodsize, self.settings.foodsize)


    def draw_food(self):

        pygame.draw.rect(self.screen, self.settings.food_color, self.rect)
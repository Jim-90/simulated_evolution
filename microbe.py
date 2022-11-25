import random
import pygame

class Microbe():

    def __init__(self, settings, screen, rules, init_pos):
        self.screen = screen
        self.settings = settings
        self.rules = rules   
        self.age = 0
        self.ticks = 0
        self.energy = 1000
        self.direction = random.randint(0, 7)                          #           [0   1   2]
        self.generation = 0                                            # DIRECTON  [7       3]
        self.offspring = 0                                             #           [6   5   4]
        self.is_dead = False
        
        self.genome = self.generate_genome()
        self.pos_x = init_pos[0] #random.randint(0, self.settings.game_width)
        self.pos_y = init_pos[1] #random.randint(0, self.settings.game_height)
        self.rect = pygame.Rect(self.pos_x*self.settings.xscale, self.pos_y*self.settings.yscale, self.settings.microbesize, self.settings.microbesize)
        

    def generate_genome(self):
        """Generate a genome, each part represeniting the probability of chooisng that direction"""
        genome_raw = [random.randint(0, 100) for _ in range(8)]
        
        return [x/sum(genome_raw) for x in genome_raw]


    def update_direction(self):
        """
        idx: 
        0 : No change
        1 : turn 1 pixel right
        2 : turn 2 pixel right
        3 : turn 3 pixel right
        4 : reverse
        5 : turn 3 pixel left
        6 : turn 2 pixel left
        7 : turn 1 pixel left
        """
        idx = 0
        cumr = self.genome[0]
        r = random.random()
        while r > cumr:
            cumr += self.genome[idx+1]
            idx += 1

        self.direction = (self.direction + idx)%8
        self.energy -= self.direction_penalty(idx)


    def direction_penalty(self, dir_index):
        """Energy cost for changing direction"""
        return self.rules.energy_cost_dir[dir_index]


    def move(self):
        """Update position of microbe"""
        #           [(-1,-1)  (-1, 0)  (-1, 1)]
        # MOVEMENT  [(0, -1)           (0, 1)]
        #           [(1, -1)  (1, 0)   (1, 1) ]
        if self.energy > 0:
            self.pos_x += self.rules.movement[self.direction][1]
            self.pos_y += self.rules.movement[self.direction][0]
            
            # Check boundaries
            if self.pos_x < 0:
                self.pos_x = self.settings.game_width-1
            elif self.pos_x >= self.settings.game_width:
                self.pos_x = 0
            if self.pos_y < 0:
                self.pos_y = self.settings.game_height-1
            elif self.pos_y >= self.settings.game_height:
                self.pos_y = 0

            # Update rect
            self.rect.x = self.pos_x*self.settings.xscale
            self.rect.y = self.pos_y*self.settings.yscale
            
            # Update energy
            self.energy -= 1
    
    
    def draw_microbe(self):
            """Draw microbe"""
            pygame.draw.rect(self.screen, self.settings.microbe_color, self.rect)


import pygame, sys, random
from settings import Settings
from rules import Rules
from microbe import Microbe

def update_screen(screen,settings, microbes, foods):
    """Update screen and flip"""
    screen.fill(settings.bg_color)

    for microbe in microbes:
        microbe.draw_microbe()

    for food in foods:
        food.draw_food()

    #screen.blit(pygame.transform.scale(game, screen.get_rect().size), (0, 0))
    pygame.display.flip()


def check_event():
    """Respond to keypress event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_microbes(settings, screen, rules, microbes, foodset, foods):
    """Check energy levels, recreate, move"""
    new_microbes = []
    for microbe in microbes:
        microbe.update_direction()
        microbe.move()
        check_food(rules, microbe, foodset, foods)

        microbe.age += 1
        microbe.ticks += 1
        if (microbe.age > rules.offspring_age) and (microbe.energy >= 1000):
            microbe.age == 0
            microbe.energy = microbe.energy/2
            new_microbes.append(create_offspring(settings, screen, rules, microbe))
    microbes += new_microbes    

def generate_microbe_positions(settings, n_microbes):
    """Generate random microbe positions and map them to the gameboard"""
    xypos = []
    npos = settings.game_width*settings.game_height
    idx = random.sample(range(npos), n_microbes)
    for id in idx:
        temp = []
        temp.append(id%(settings.game_width-1))
        temp.append(id//(settings.game_height-1))
        xypos.append(temp)
    
    return xypos


def create_offspring(settings, screen, rules, parent):
    microbe = Microbe(settings, screen, rules, [parent.pos_x, parent.pos_y])
    microbe.energy = parent.energy
    return microbe


def generate_random_food(settings, food_prob):
    npos = settings.game_width*settings.game_height
    cords_set = set()
    while len(cords_set) < npos*food_prob:
        x, y = random.randint(0, settings.game_width-1), random.randint(0, settings.game_height-1)
        cords_set.add((x,y))
    
    return cords_set

def check_food(rules, microbe, foodset, foods):
    pred_pos = (microbe.pos_x, microbe.pos_y)

    if pred_pos in foodset:
        food_id = 0
        for food in foods:
            if (food.pos_x == microbe.pos_x) and (food.pos_y == microbe.pos_y):
                foodset.remove(pred_pos)
                del foods[food_id]
                microbe.energy += rules.foodenergy
                break
            food_id += 1

    
def update_state(microbe):
    microbe.ticks += 1
    microbe.age += 1
    
def check_alive(microbes):
    for idx, microbe in enumerate(microbes.copy()):
        if microbe.is_dead:
            del microbes[idx]
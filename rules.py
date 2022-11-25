
class Rules():

    def __init__(self):

        self.energy_cost_dir = {0:0, 1:1, 2:2, 3:4, 4:8, 5:4, 6:2, 7:1}
        self.energy_cost_tick = 1
        self.movement = {0: (-1, -1),
                         1: (-1, 0),
                         2: (-1, 1),
                         3: (0, 1),
                         4: (1, 1),
                         5: (1, 0),
                         6: (1, -1),
                         7: (0, -1)
                         }  # (dy, dx)
        self.foodenergy = 50
        self.max_energy = 1500
        self.offspring_age = 20

if '__main__' == __name__:

    rules = Rules()

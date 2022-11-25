from random import choices

class Settings():

    def __init__(self):
        # Display settings.
        self.screen_width =  1000
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)
        self.microbe_color = (0, 0, 255)
        self.food_color = (0, 153, 0)

        # Game settings.
        self.game_width = 200
        self.game_height = 200
        self.xscale = self.screen_width/self.game_width
        self.yscale = self.screen_height/self.game_height
        self.microbesize = int(1.2*self.screen_width/self.game_width)
        self.foodsize = int(0.6*self.screen_width/self.game_width)
        self.game_mode = 'random'
        
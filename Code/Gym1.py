from Import import *
from Pokemon1 import PokemonCharacter
import random

class GYM1(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self.map = None
        self.background = None
        self.round = 1
        self.monster1 = None
        self.monster2 = None
        self.monster2list = None
    
    def setup(self):
        self.map = arcade.load_tilemap("Assets/Tiled/Beach.json", 1.78)
        self.background = self.map.sprite_lists["Background"]
        self.monster2list = arcade.SpriteList()
        self.monster2 = PokemonCharacter()
        self.monster2list.append(self.monster2)

    def on_update(self, delta_time: float):
        #if round < 4:
            #pickmons = random.randint(0, len(self.monsternum))
            #if pickmons == 0:
        pass
    
    def on_draw(self):
        self.background.draw()
        self.monster2list.draw()


game = arcade.Window(Width, Height, Title)
mainView = GYM1()
mainView.setup()
game.show_view(mainView)
arcade.run()
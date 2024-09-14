from Import import *
from Player import PlayerCharacter

X = 144
Y = 368


class Map1(arcade.View):
    def __init__(self):
        super().__init__()
        self.Player = None
        self.Player_list = None
        self.WorldSeparator = None
        self.Gym = None
        self.GymDoor = None
        self.SDoor = None
        self.Shop = None
        self.Hospital = None
        self.HDoor = None
        self.House = None
        self.Door = None
        self.Tree = None
        self.Road = None
        self.Ground = None
        self.Border = None
        self.Background = None
        self.Rock = None
        self.tile_map = None
        self.key_left = None
        self.key_right = None
        self.Door_engine = None
        self.GymDoor_engine = None
        self.HDoor_engine = None
        self.Border_engine = None
        self.left_pressed = None
        self.right_pressed = None
        self.top_pressed = None
        self.down_pressed = None
        self.House_engine = None
        self.Hospital_engine = None
        self.Gym_engine = None
        self.Ground_engine = None
        self.Rock_engine = None
        self.Epress = None
        self.SDoor_engine = None
        self.Bor1_engine = None
        self.Shop_engine = None

    def setup(self):
        self.tile_map = arcade.load_tilemap("Assets/Tiled/World Map 1.json", 2)
        self.Background = self.tile_map.sprite_lists["Background"]
        self.Border = self.tile_map.sprite_lists["Border"]
        self.Ground = self.tile_map.sprite_lists["Ground"]
        self.Tree = self.tile_map.sprite_lists["Tree"]
        self.Road = self.tile_map.sprite_lists["Road"]
        self.House = self.tile_map.sprite_lists["House"]
        self.Door = self.tile_map.sprite_lists["Door"]
        self.Hospital = self.tile_map.sprite_lists["Hospital"]
        self.HDoor = self.tile_map.sprite_lists["HDoor"]
        self.Shop = self.tile_map.sprite_lists["Shop"]
        self.SDoor = self.tile_map.sprite_lists["SDoor"]
        self.Gym = self.tile_map.sprite_lists["Gym"]
        self.GymDoor = self.tile_map.sprite_lists["GymDoor"]
        self.WorldSeparator = self.tile_map.sprite_lists["WorldSeparator"]
        self.Rock = self.tile_map.sprite_lists["Rock"]
        self.Player_list = arcade.SpriteList()
        self.Player = PlayerCharacter()
        self.Player.center_x = X
        self.Player.center_y = Y
        self.Player_list.append(self.Player)
        self.Door_engine = arcade.PhysicsEngineSimple(self.Player, self.Door)
        self.GymDoor_engine = arcade.PhysicsEngineSimple(self.Player, self.GymDoor)
        self.HDoor_engine = arcade.PhysicsEngineSimple(self.Player, self.HDoor)
        self.Border_engine = arcade.PhysicsEngineSimple(self.Player, self.Border)
        self.House_engine = arcade.PhysicsEngineSimple(self.Player, self.House)
        self.Hospital_engine = arcade.PhysicsEngineSimple(self.Player, self.Hospital)
        self.Gym_engine = arcade.PhysicsEngineSimple(self.Player, self.Gym)
        self.Ground_engine = arcade.PhysicsEngineSimple(self.Player, self.Ground)
        self.Bor1_engine = arcade.PhysicsEngineSimple(self.Player, self.WorldSeparator)
        self.SDoor_engine = arcade.PhysicsEngineSimple(self.Player, self.SDoor)
        self.Shop_engine = arcade.PhysicsEngineSimple(self.Player, self.Shop)
        self.Rock_engine = arcade.PhysicsEngineSimple(self.Player, self.Rock)

    def on_update(self, delta_time: float):
        self.Player_list.update()
        self.Player_list.update_animation()
        self.GymDoor_engine.update()
        self.HDoor_engine.update()
        self.Border_engine.update()
        self.House_engine.update()
        self.Hospital_engine.update()
        self.Gym_engine.update()
        self.Ground_engine.update()
        self.SDoor_engine.update()
        self.Shop_engine.update()
        self.Rock_engine.update()
        self.Player.change_x = 0
        self.Player.change_y = 0
        if self.right_pressed:
            self.Player.change_x = -0.3
        if self.left_pressed:
            self.Player.change_x = 0.3
        if self.top_pressed:
            self.Player.change_y = 0.3
        if self.down_pressed:
            self.Player.change_y = -0.3
        # MBorder_engine = arcade.check_for_collision_with_list(self.Player, self.WorldSeparator)
        # if MBorder_engine and self.Epress == True:
        #     map2 = Map2()
        #     map2.setup()
        #     game.show_view(map2)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.Background.draw()
        self.Rock.draw()
        self.Border.draw()
        self.Ground.draw()
        self.Road.draw()
        self.House.draw()
        self.Door.draw()
        self.Hospital.draw()
        self.HDoor.draw()
        self.Shop.draw()
        self.SDoor.draw()
        self.Gym.draw()
        self.GymDoor.draw()
        self.WorldSeparator.draw()
        self.Player_list.draw()
        self.Tree.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.top_pressed = True
        elif symbol == arcade.key.S:
            self.down_pressed = True
        elif symbol == arcade.key.D:
            self.left_pressed = True
        elif symbol == arcade.key.A:
            self.right_pressed = True
        elif symbol == arcade.key.E:
            self.Epress = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.top_pressed = False
        elif symbol == arcade.key.S:
            self.down_pressed = False
        elif symbol == arcade.key.D:
            self.left_pressed = False
        elif symbol == arcade.key.A:
            self.right_pressed = False
        elif symbol == arcade.key.E:
            self.Epress = False


game = arcade.Window(Width, Height, Title)
mainView = Map1()
mainView.setup()
game.show_view(mainView)
arcade.run()
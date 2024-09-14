from arcade import Window
from Import import *
from Player import PlayerCharacter
import random

X = 144
Y = 368

class GameState():
    def __init__(self) -> None:
        self.monster = 0
        self.money = 0
        self.pokemon = None
        self.change_x1 = 144
        self.change_y1 = 368
        self.change_x2 = 576
        self.change_y2 = 491

    @staticmethod
    def get_instance():
        if not hasattr(GameState, '_instance'):
            GameState._instance = GameState()
        return GameState._instance
    
class Mainmenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.sound = None
        self.player = None

    def setup(self):
        self.sound = arcade.load_sound("Assets/Audio/05. Welcome to the World of Pokémon!.mp3")
        self.sound_play = arcade.play_sound(self.sound, loop=True)

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_YELLOW)
    
    def on_draw(self):
        self.clear()
        arcade.draw_text("SAKUMON", 360, 320, arcade.color.BLACK, font_size=35, font_name="Pixeloid Sans")
        arcade.draw_text("Press anywhere to start", 260, 280, arcade.color.BLACK, font_size=25, font_name="Pixeloid Sans")
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.sound_play is not None:
            arcade.stop_sound(self.sound_play)
        gameView = Map1()
        gameView.setup()
        self.window.show_view(gameView)

class Map1(arcade.View):
    def __init__(self):
        super().__init__()
        self.game_state = GameState.get_instance()
        self.pokemon = None
        self.Player = None
        self.Player_list = None
        self.WorldSeparator =  None
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
        self.Text = None
        self.Money = 0
        self.sound = None

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
        self.game_state.pokemon = self.tile_map.sprite_lists["Pokemon"]
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
        self.sound = arcade.load_sound("Assets/Audio/21 - Hurry Along.mp3")
        self.sound.play(loop=True)

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
        MBorder_engine = arcade.check_for_collision_with_list(self.Player, self.WorldSeparator)
        Pokemon_engine = arcade.check_for_collision_with_list(self.Player, self.game_state.pokemon)
        if MBorder_engine and self.Epress == True:
             map2 = Map2()
             map2.setup()
             game.show_view(map2)
        for i in Pokemon_engine:
            chance = random.randint(1, 10)
            if chance > 5:
                self.game_state.monster += 1
            else:
                print("You fail to catch a pokemon")
            print(self.game_state.monster)
            i.remove_from_sprite_lists()

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
        self.game_state.pokemon.draw()
        self.Player_list.draw()
        self.Tree.draw()
        self.Text = arcade.Text(text=f"Money: ${self.Money}  Sakumon: {self.game_state.monster}monster", x=10, y=5, color=arcade.color.WHITE, font_size=15, font_name="Pixeloid Sans")
        self.Text.draw()

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

class Map2(arcade.View):
    def __init__(self):
        super().__init__()
        self.gamestate = GameState.get_instance()
        self.pokemon = None
        self.Player = None
        self.Player_list = None
        self.GymDoor = None
        self.Gym = None
        self.HDoor = None
        self.Hospital = None
        self.Door = None
        self.House = None
        self.Road = None
        self.Tree = None
        self.Tree2 = None
        self.Tree3 = None
        self.Ground = None
        self.Border = None
        self.Background = None
        self.tile_map = None
        self.key_left = None
        self.key_right = None
        self.WorldSeparator = None
        self.WorldSeparator1 = None
        self.Door_engine = None
        self.House_engine2 = None
        self.Gym_engine = None
        self.GymDoor_engine = None
        self.Tree_engine = None
        self.Tree2_engine = None
        self.Tree3_engine = None
        self.Border_engine = None
        self.Bor1_engine = None
        self.Bor2_engine = None
        self.Hospital_engine = None
        self.HDoor_engine = None
        self.Epress = None
        self.left_pressed = None
        self.right_pressed = None
        self.top_pressed = None
        self.down_pressed = None
        self.Text = None
        self.Money = 0

    def setup(self):
        self.tile_map = arcade.load_tilemap("Assets/Tiled/World Map 2.json", 2)
        self.Background = self.tile_map.sprite_lists["Background"]
        self.Border = self.tile_map.sprite_lists["Border"]
        self.Ground = self.tile_map.sprite_lists["Ground"]
        self.Tree = self.tile_map.sprite_lists["Tree"]
        self.Road = self.tile_map.sprite_lists["Road"]
        self.House = self.tile_map.sprite_lists["House"]
        self.Door = self.tile_map.sprite_lists["Door"]
        self.Hospital = self.tile_map.sprite_lists["Hospital"]
        self.HDoor = self.tile_map.sprite_lists["HDoor"]
        self.Gym = self.tile_map.sprite_lists["Gym"]
        self.GymDoor = self.tile_map.sprite_lists["GymDoor"]
        self.WorldSeparator = self.tile_map.sprite_lists["WorldSeperator"]
        self.Tree2 = self.tile_map.sprite_lists["Tree 2"]
        self.Tree3 = self.tile_map.sprite_lists["Tree 3"]
        self.pokemon = self.tile_map.sprite_lists["Pokemon"]
        self.Player_list = arcade.SpriteList()
        self.Player = PlayerCharacter()
        self.Player.center_x = 576
        self.Player.center_y = 491
        self.Player_list.append(self.Player)
        self.Door_engine = arcade.PhysicsEngineSimple(self.Player, self.Door)
        self.GymDoor_engine = arcade.PhysicsEngineSimple(self.Player, self.GymDoor)
        self.HDoor_engine = arcade.PhysicsEngineSimple(self.Player, self.HDoor)
        self.Border_engine = arcade.PhysicsEngineSimple(self.Player, self.Border)
        self.House_engine2 = arcade.PhysicsEngineSimple(self.Player, self.House)
        self.Hospital_engine = arcade.PhysicsEngineSimple(self.Player, self.Hospital)
        self.Gym_engine = arcade.PhysicsEngineSimple(self.Player, self.Gym)
        self.Bor1_engine = arcade.PhysicsEngineSimple(self.Player, self.WorldSeparator)
        self.Tree_engine = arcade.PhysicsEngineSimple(self.Player, self.Tree)
        self.Tree2_engine = arcade.PhysicsEngineSimple(self.Player, self.Tree2)
        self.Tree3_engine = arcade.PhysicsEngineSimple(self.Player, self.Tree3)

    def on_update(self, delta_time: float):
        self.Player_list.update()
        self.Player_list.update_animation()
        self.GymDoor_engine.update()
        self.HDoor_engine.update()
        self.Border_engine.update()
        self.House_engine2.update()
        self.Hospital_engine.update()
        self.Gym_engine.update()
        self.Bor1_engine.update()
        self.Tree_engine.update()
        self.Tree2_engine.update()
        self.Tree3_engine.update()
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
        MBorder_engine = arcade.check_for_collision_with_list(self.Player, self.WorldSeparator)
        Pokemon_engine = arcade.check_for_collision_with_list(self.Player, self.pokemon)
        if MBorder_engine and self.Epress == True:
            map1 = Map1()
            map1.setup()
            game.show_view(map1)
        for i in Pokemon_engine:
            chance = random.randint(1, 10)
            if chance > 5:
                self.gamestate.monster += 1
            else:
                print("You fail to catch a pokemon")
            print(self.gamestate.monster)
            i.remove_from_sprite_lists()
        
        if self.gamestate.monster > 5:
            endgame = ENDGAME()
            self.window.show_view(endgame)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.Background.draw()
        self.Border.draw()
        self.Ground.draw()
        self.Road.draw()
        self.Tree3.draw()
        self.Tree2.draw()
        self.Gym.draw()
        self.Tree.draw()
        self.House.draw()
        self.Hospital.draw()
        self.WorldSeparator.draw()
        self.pokemon.draw()
        self.Player_list.draw()
        self.Text = arcade.Text(text=f"Money: ${self.Money}  Sakumon: {self.gamestate.monster}monster", x=10, y=5, color=arcade.color.WHITE, font_size=15, font_name="Pixeloid Sans")
        self.Text.draw()

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

class ENDGAME(arcade.View):
    def __init__(self):
        super().__init__()
        self.gamestate = GameState.get_instance()
        self.monster = None
        self.sound = None
        self.player = None

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_YELLOW)
    
    def on_draw(self):
        self.clear()
        arcade.draw_text("The END", 360, 320, arcade.color.BLACK, font_size=35, font_name="Pixeloid Sans")
        arcade.draw_text(f"You a great pokemon hunter with {self.gamestate.monster} Monster", 100, 280, arcade.color.BLACK, font_size=25, font_name="Pixeloid Sans")
            
game = arcade.Window(Width, Height, Title)
mainView = Mainmenu()
mainView.setup()
game.show_view(mainView)
arcade.run()
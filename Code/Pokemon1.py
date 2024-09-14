import arcade

def load_texture(filename):
    return[
        arcade.load_texture(filename),
        arcade.load_texture(filename)
    ]

class PokemonCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()
        main_path = "Assets/Image/MPWSP01/menu sprites/menusprite7.png"
        self.idleTexture = load_texture(f'{main_path}')

    def attack():
        pass
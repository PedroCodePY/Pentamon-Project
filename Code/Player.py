import arcade

speed = 5
Update_Per_Frame = 5
right_facing = 0
left_facing = 1

def load_texture(filename):
    return[
        arcade.load_texture(filename),
        arcade.load_texture(filename)
    ]

class PlayerCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.character_facing_direction = right_facing
        self.cur_texture = 0
        self.scale = 0.5
        main_path = ":resources:images/animated_characters/male_adventurer/maleAdventurer"
        self.idleTexture = load_texture(f'{main_path}_idle.png')
        self.walkTextures = []
        for i in range(8):
            texture = load_texture(f'{main_path}_walk{i}.png')
            self.walkTextures.append(texture)

    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x < 0 and self.character_facing_direction == right_facing:
            self.character_facing_direction = left_facing
        elif self.change_x > 0 and self.character_facing_direction == left_facing:
            self.character_facing_direction = right_facing

        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idleTexture[
                self.character_facing_direction
            ]
            return

        self.cur_texture += 1
        if self.cur_texture > 7 * Update_Per_Frame:
            self.cur_texture = 0

        frame = self.cur_texture // Update_Per_Frame
        direction = self.character_facing_direction
        self.texture = self.walkTextures[frame][direction]
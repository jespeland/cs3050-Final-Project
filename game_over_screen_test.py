import arcade 

SCREEN_WIDTH  = 650
SCREEN_HEIGHT = 650
class GameOverView(arcade.View):

    #Load game over image onto window
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("GameOver.jpg")

    #clear current window textures and draw game over texture
    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)


    #exit arcade when player clicks screen
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        arcade.exit()

    def on_update(self, delta_time: float):
        view = GameOverView()
        self.window.show_view(view)
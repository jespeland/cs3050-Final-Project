import arcade
from Board import *
import threading
import random
import time
# Constants
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650

compPlayer = False
compColor = ""
numPlayers = input("How many players? Enter 1-4: ")
while numPlayers != "1" and numPlayers != "2" and numPlayers != "3" and numPlayers != "4":
    numPlayers = input("Invalid input. Enter 1-4")

numPlayers = int(numPlayers)
colors = []
print("Enter the colors of each player one by one.")
print("The order that you enter them in will be the order of the turns.")
for i in range(numPlayers):
    color = input("Enter one of the colors")

    while (color != "Red" and color != "Blue" and color != "Green" and color != "Yellow") or color in colors:
        if color in colors:
            color = input("Color already chosen. Pick a different one: ")
        else:
            color = input("Color not valid. Pick a different color: ")

    colors.append(color)

if len(colors) < 4:
    compChoice = input("Would you like a computer player? (Enter y or n): ")

    while compChoice != "y" and compChoice != "n":
        compChoice = input("Enter y or n: ")

    if compChoice == "y":
        if not "Red" in colors:
            compColor = "Red"
            print("Computer will be Red")

        elif not "Blue" in colors:
            compColor = "Blue"
            print("Computer will be Blue")

        elif not "Green" in colors:
            compColor = "Green"
            print("Computer will be Green")

        else:
            compColor = "Yellow"
            print("Computer will be Yellow")

        compPlayer = True
class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Sorry! Board")

        # Initialize variables for handling dragging
        self.dragging_sprite = None
        self.offset_x = 0
        self.offset_y = 0

        # create a sprite for the background image
        self.image_sprite = arcade.Sprite(r'..\cs3050_finalproject\sorryBoardSmaller.png', center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2)
        self.coordinates = [[47, 603], [84, 603], [121, 603], [158, 603], [195, 603], [232, 603], [269, 603], [306, 603], [343, 603], [380, 603], [417, 603], [454, 603], [491, 603], [528, 603], [565, 603], [602, 603], [607, 603], [607, 566], [607, 529], [607, 492], [607, 455], [607, 418], [607, 381], [607, 344], [607, 307], [607, 270], [607, 233], [607, 196], [607, 159], [607, 122], [607, 85], [607, 48], [607, 43], [570, 43], [533, 43], [496, 43], [459, 43], [422, 43], [385, 43], [348, 43], [311, 43], [274, 43], [237, 43], [200, 43], [163, 43], [126, 43], [89, 43], [52, 43], [47, 43], [47, 80], [47, 117], [47, 154], [47, 191], [47, 228], [47, 265], [47, 302], [47, 339], [47, 376], [47, 413], [47, 450], [47, 487], [47, 524], [47, 561], [47, 598]]
        self.red_home = [[117,568],[117,533],[117,498],[117,463],[117,428]]
        self.blue_home = [[572,533],[537,533],[502,533],[467,533],[432,533]]
        self.green_home = [[82,113],[117,113],[152,113],[187,113],[222,113]]
        self.yellow_home = [[537,78],[537,113],[537,148],[537,183],[537,218]]
        self.red_start = [[170,559],[220,553],[175,515],[222,520]]
        self.blue_start = [[555,475],[568,440],[528,472],[523,440]]
        self.green_start = [[95,160],[135,167],[93,220],[138,222]]
        self.yellow_start = [[486,85],[440,87],[483,115],[435,117]]
        self.red_home = [[170, 559], [220, 553], [175, 515], [222, 520]]
        self.blue_home = [[555, 475], [568, 440], [528, 472], [523, 440]]
        self.green_home = [[95, 160], [135, 167], [93, 220], [138, 222]]
        self.yellow_home = [[486, 85], [440, 87], [483, 115], [435, 117]]
        self.piece_sprites = []
        self.delay = 1.0
        # create a sprite for the draggable square
        self.blue_square = arcade.SpriteSolidColor(20, 20, arcade.color.BLUE)
        self.blue_square.center_x = 397
        self.blue_square.center_y = 603

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.draw_board()
        self.image_sprite.draw()
        for piece_sprite in self.piece_sprites:
            piece_sprite.draw()

    def draw_piece(self, x, y, pieceColor):
        if(pieceColor == "Red"):
            piece = arcade.SpriteSolidColor(20, 20, arcade.color.RED)
        elif (pieceColor == "Blue"):
            piece = arcade.SpriteSolidColor(20, 20, arcade.color.BLUE)
        elif (pieceColor == "Yellow"):
            piece = arcade.SpriteSolidColor(20, 20, arcade.color.YELLOW)
        else:
            piece = arcade.SpriteSolidColor(20, 20, arcade.color.GREEN)
        piece.center_x = x
        piece.center_y = y
        return piece

    def draw_board(self):
        # Draw the background
        self.image_sprite.draw()
        self.blue_square.draw()
        self.piece_sprites = []  # Reset the piece sprites list
        self.numRedStart = 0
        self.numBlueStart = 0
        self.numGreenStart = 0
        self.numYellowStart = 0
        for coord in self.coordinates:
            self.blue_square.center_x, self.blue_square.center_y = coord[0], coord[1]
            self.blue_square.draw()
            arcade.finish_render()
            self.delay# Finish the render to update the screen

        for piece in Board.redTeam.pieces:
            coords = piece.coords
            if coords == pos.START:
                piece_sprite = self.draw_piece(self.red_start[self.numRedStart][0], self.red_start[self.numRedStart][1], piece.color)
                self.numRedStart += 1
            elif coords == pos.HOME:
                piece_sprite = self.draw_piece(250, 250, piece.color)
            elif (coords < 0):
                position = -coords
                position -= 1
                piece_sprite = self.draw_piece(self.red_home[position][0], self.red_home[position][1], piece.color)
            else:
                piece_sprite = self.draw_piece(self.coordinates[coords][0], self.coordinates[coords][1], piece.color)
            self.piece_sprites.append(piece_sprite)

        for piece in Board.blueTeam.pieces:
            coords = piece.coords
            if coords == pos.START:
                piece_sprite = self.draw_piece(self.blue_start[self.numBlueStart][0], self.blue_start[self.numBlueStart][1],piece.color)
                self.numBlueStart += 1
            elif coords == pos.HOME:
                piece_sprite = self.draw_piece(250, 250, piece.color)
            elif (coords < 0):
                position = -coords
                position -= 1
                piece_sprite = self.draw_piece(self.blue_home[position][0], self.blue_home[position][1], piece.color)
            else:
                piece_sprite = self.draw_piece(self.coordinates[coords][0], self.coordinates[coords][1], piece.color)
            self.piece_sprites.append(piece_sprite)

        for piece in Board.yellowTeam.pieces:
            coords = piece.coords
            if coords == pos.START:
                piece_sprite = self.draw_piece(self.yellow_start[self.numYellowStart][0], self.yellow_start[self.numYellowStart][1], piece.color)
                self.numYellowStart += 1
            elif coords == pos.HOME:
                piece_sprite = self.draw_piece(250, 250, piece.color)
            elif (coords < 0):
                position = -coords
                position -= 1
                piece_sprite = self.draw_piece(self.yellow_home[position][0], self.yellow_home[position][1], piece.color)
            else:
                piece_sprite = self.draw_piece(self.coordinates[coords][0], self.coordinates[coords][1], piece.color)
            self.piece_sprites.append(piece_sprite)

        for piece in Board.greenTeam.pieces:
            coords = piece.coords
            if coords == pos.START:
                piece_sprite = self.draw_piece(self.green_start[self.numGreenStart][0], self.green_start[self.numGreenStart][1], piece.color)
                self.numGreenStart += 1
            elif coords == pos.HOME:
                piece_sprite = self.draw_piece(250, 250, piece.color)
            elif (coords < 0):
                position = -coords
                position -= 1
                piece_sprite = self.draw_piece(self.green_home[position][0], self.green_home[position][1], piece.color)
            else:
                piece_sprite = self.draw_piece(self.coordinates[coords][0], self.coordinates[coords][1], piece.color)
            self.piece_sprites.append(piece_sprite)

    def on_mouse_press(self, x, y, button, modifiers):
        # Check if the mouse click is on the square sprite
        if self.blue_square.collides_with_point((x, y)):
            self.dragging_sprite = self.blue_square
            self.offset_x = x - self.dragging_sprite.center_x
            self.offset_y = y - self.dragging_sprite.center_y

    def on_mouse_release(self, x, y, button, modifiers):
        self.dragging_sprite = None

    def on_mouse_motion(self, x, y, dx, dy):
        if self.dragging_sprite:
            self.dragging_sprite.center_x = x - self.offset_x
            self.dragging_sprite.center_y = y - self.offset_y

def run_graphics():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
def run_board():
    board = Board()
    choice = input("Move or quit")
    while choice != "quit":
        for col in colors:
            print("It is ", col, " turn!")
            card = board.theDeck.draw_card()
            choice = int(input("Which piece would you like to move?"))
            board.turn(col, card, choice)
            board.__str__()
            while card == 2:
                print("Draw again!")
                print("It is ", col, " turn!")
                card = board.theDeck.draw_card()
                choice = int(input("Which piece would you like to move?"))
                board.turn(col, card, choice)
                board.__str__()

        if compPlayer:
            card = board.theDeck.draw_card()
            choice = random.randint(1, 4)
            print("It is computer's turn")
            board.turn(compColor, card, choice)
            board.__str__()
            while card == 2:
                print("Draw again!")
                card = board.theDeck.draw_card()
                choice = random.randint(1, 4)
                print("It is computer's turn")
                board.turn(compColor, card, choice)
                board.__str__()
        choice = input("Move or quit")
if __name__ == "__main__":
    # Start the graphics thread
    graphics_thread = threading.Thread(target=run_graphics)
    graphics_thread.start()

    # Start the board thread
    board_thread = threading.Thread(target=run_board)
    board_thread.start()
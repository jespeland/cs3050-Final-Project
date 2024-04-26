import arcade

WIDTH, HEIGHT = 800, 600
INPUT_HEIGHT = 50

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.input_text = []
        self.input_prompt = "Enter the first number: "
        self.first_number = None
        self.second_number = None
        self.error_message = None

    def on_draw(self):
        arcade.start_render()
        self.draw_input()
        if self.error_message:
            arcade.draw_text(self.error_message, 10, 10, arcade.color.RED, 20)

    def draw_input(self):
        input_text = ''.join(self.input_text)
        arcade.draw_text(self.input_prompt + input_text, 10, HEIGHT - INPUT_HEIGHT + 10, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE:
            if self.input_text:
                self.input_text.pop()
        elif (65 <= key <= 90) or (48 <= key <= 57):
            self.input_text.append(chr(key))
        elif key == arcade.key.ENTER:
            self.handle_input(''.join(self.input_text))
            self.input_text = []

    def handle_input(self, input_str):
        if self.input_prompt.startswith("Enter the first number: "):
            if self.validate_number_input(input_str):
                self.first_number = float(input_str)
                self.input_text = []
                self.input_prompt = "Enter the second number: "
                self.error_message = None
            else:
                self.error_message = "Invalid input. Please enter a valid number."
        elif self.input_prompt.startswith("Enter the second number: "):
            if self.validate_number_input(input_str):
                self.second_number = float(input_str)
                self.input_text = []
                result = self.first_number + self.second_number
                self.input_prompt = f"Result: {self.first_number} + {self.second_number} = {result}"
                self.error_message = None
            else:
                self.error_message = "Invalid input. Please enter a valid number."

    def validate_number_input(self, input_str):
        try:
            float(input_str)
            return True
        except ValueError:
            return False

def main():
    game = MyGame(WIDTH, HEIGHT, "Console Calculator")
    arcade.run()

if __name__ == "__main__":
    main()

from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Clears the screen and updates the scoreboard with the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def increase_level(self):
        """Increases the level by 1 and updates the scoreboard."""
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        """Displays 'Game Over' message at the center of the screen."""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

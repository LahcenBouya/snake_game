from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_high_score()
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.update_score_board()

    def get_high_score(self):
        with open("snake_game/highscore.txt", "r") as my_file:
            return int(my_file.read())
    
    def save_high_score(self):
        with open("snake_game/highscore.txt", "w") as my_file:
            my_file.write(str(self.score))

        
    def update_score_board(self):
        self.hideturtle()
        self.write(f"Score : {self.score}   high score : {self.highscore}", align="center", font=("arial", 30, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_high_score()
            
        self.write(f"Game over \n\nyour final Score : {self.score} \n\nHigh score: {self.highscore}", align="center", font=("arial", 30, "bold"))

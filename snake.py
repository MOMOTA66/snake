import os
import time
import keyboard
import random

class SnakeGame:
    def __init__(self):
        self.max_length = 10
        self.time_delay = 0.1
        self.snake = Snake(self.max_length)
        self.star = Star(self.max_length)

    def run(self):
        while True:
            self.record_snake_path()
            self.update_snake_state()

            if self.is_eating_star():
                self.snake.increase_length()
                self.star.randomize_position()

            print(f"Snake Length: {self.snake.length}")
            self.print_game_board()
            time.sleep(self.time_delay)
            os.system("cls" if os.name == "nt" else "clear")

    def print_game_board(self):
        for i in range(self.max_length):
            for j in range(self.max_length):
                if i in (0, self.max_length - 1) or j in (0, self.max_length - 1):
                    print(" 墙", end="")
                elif (i, j) == (self.snake.y, self.snake.x):
                    print(" 蛇", end="")
                elif (i, j) == (self.star.y, self.star.x):
                    print(" 星", end="")
                else:
                    print(" -", end=" ")
            print()

    def update_snake_state(self):
        self.snake.move()
        if keyboard.is_pressed("right") and self.snake.direction != "left":
            self.snake.direction = "right"
        elif keyboard.is_pressed("left") and self.snake.direction != "right":
            self.snake.direction = "left"
        elif keyboard.is_pressed("up") and self.snake.direction != "down":
            self.snake.direction = "up"
        elif keyboard.is_pressed("down") and self.snake.direction != "up":
            self.snake.direction = "down"

    def is_eating_star(self):
        return (self.snake.x, self.snake.y) == (self.star.x, self.star.y)

    def record_snake_path(self):
        self.snake.record_path()

class Snake:
    def __init__(self, max_length):
        self.max_length = max_length
        self.x = 2
        self.y = 2
        self.direction = "right"
        self.length = 1
        self.path = []

    def move(self):
        new_x, new_y = self.x, self.y
        if self.direction == "right":
            new_x += 1
        elif self.direction == "left":
            new_x -= 1
        elif self.direction == "up":
            new_y -= 1
        elif self.direction == "down":
            new_y += 1

        if not self.is_touching_wall(new_x, new_y):
            self.x, self.y = new_x, new_y

    def is_touching_wall(self, x, y):
        return x == 0 or x == self.max_length - 1 or y == 0 or y == self.max_length - 1

    def increase_length(self):
        self.length += 1

    def record_path(self):
        self.path.insert(0, (self.x, self.y))

class Star:
    def __init__(self, max_length):
        self.max_length = max_length
        self.x = 3
        self.y = 3

    def randomize_position(self):
        while True:
            random_x = random.randint(1, self.max_length - 2)
            random_y = random.randint(1, self.max_length - 2)
            if (random_x, random_y) != (self.x, self.y):
                self.x, self.y = random_x, random_y
                break

if __name__ == "__main__":
    game = SnakeGame()
    game.run()



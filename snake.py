import os
import time
import keyboard
import random

# 蛇初始位置
snake_X = 2
snake_Y = 2

star_X = 3
star_Y = 3

wall = " 牆"
empty = " -"
snake_symbol = " 蛇"
snake_length = 1
star_symbol = " 星"
maxLength = 10
timeLength = 0.1
currentDirection = "right"
snake_recordPath = []
last_recorded_path = None
snake_body = [(snake_X, snake_Y)]

# 畫面渲染
def main():
    while True:
        for i in range(maxLength):
            for j in range(maxLength):
                if i in (0, maxLength - 1) or j in (0, maxLength - 1):
                    print(wall, end="")
                elif i == snake_Y and j == snake_X:
                    print(snake_symbol, end="")
                elif i == star_Y and j == star_X:
                    print(star_symbol, end="")
                elif (j, i) in snake_body:
                    print(snake_symbol, end="")
                else:
                    print(empty, end=" ")
            print()

        recordSnakePath()
        updateSnakeState()
        if isEatStar():
            add_snake_Length_()
            randomStarPosition()

        print(snake_length)
        time.sleep(timeLength)
        os.system("cls" if os.name == "nt" else "clear")

def updateSnakeState():
    global snake_X, snake_Y, currentDirection, snake_body

    new_X = snake_X
    new_Y = snake_Y

    if keyboard.is_pressed("right") and currentDirection != "left":
        currentDirection = "right"
    elif keyboard.is_pressed("left") and currentDirection != "right":
        currentDirection = "left"
    elif keyboard.is_pressed("up") and currentDirection != "down":
        currentDirection = "up"
    elif keyboard.is_pressed("down") and currentDirection != "up":
        currentDirection = "down"

    if currentDirection == "right":
        new_X = new_X + 1
    elif currentDirection == "left":
        new_X = new_X - 1
    elif currentDirection == "up":
        new_Y = new_Y - 1
    elif currentDirection == "down":
        new_Y = new_Y + 1

    isTouchWall = new_X == 0 or new_X == maxLength - 1 or new_Y == 0 or new_Y == maxLength - 1
    if not isTouchWall:
        snake_X = new_X
        snake_Y = new_Y

    # 更新蛇的身體位置 (這裡)
    snake_body.insert(0, (snake_X, snake_Y))
    if len(snake_body) > snake_length:
        snake_body.pop()

def isEatStar():
    return snake_X == star_X and snake_Y == star_Y

def randomStarPosition():
    max_attempts = 100
    attempts = 0

    while attempts < max_attempts:
        global star_X, star_Y

        random_X = random.randint(1, maxLength - 1 - 1)
        random_Y = random.randint(1, maxLength - 1 - 1)

        isNotCover = (random_X, random_Y) not in snake_recordPath and (random_X, random_Y) not in snake_body
        if isNotCover:
            star_X = random_X
            star_Y = random_Y
            break

        attempts += 1

def recordSnakePath():
    global last_recorded_path
    snake_Path = (snake_X, snake_Y)

    if snake_Path != last_recorded_path:
        snake_recordPath.insert(0, snake_Path)
        last_recorded_path = snake_Path

def add_snake_Length_():
    global snake_length
    snake_length = snake_length + 1

main()





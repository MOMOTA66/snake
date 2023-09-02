import os
import time
import keyboard
import random

# 蛇初始位置
snake_X = 5
snake_Y = 5

star_X = 8
star_Y = 8

wall = " 牆"
empty = " -"
snake_symbol = " 蛇"
star_symbol =" 星"
maxLength = 15
timeLength = 0.1
currentDirection = "right"  # 當前方向 右移



# 畫面渲染
def main():
    while True:
        for i in range(maxLength):
            for j in range(maxLength):
                if i in (0, maxLength - 1) or j in (0, maxLength - 1):
                    print(wall, end="")
                # 打印 蛇的畫面
                elif i == snake_Y and j == snake_X:
                    print(snake_symbol, end="")
                #打印 星星的畫面
                elif i == star_Y and j == star_X:
                    print(star_symbol, end="")
                else:
                    print(empty, end=" ")
            # 打印畫面
            print()

        snakeState()  # 更新 蛇 的狀態
        # starState     # 更新 星 的狀態
        # 設定畫面更新時間
        time.sleep(timeLength)
        # 清除畫面
        os.system("cls" if os.name == "nt" else "clear")



# 蛇的狀態
def snakeState():
    
    global snake_X, snake_Y, currentDirection
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

    # 判斷站存的x和y是不是在牆壁上，如果是的話就不要用佔存的值
    isTouchWall = new_X == 0 or new_X == maxLength - 1 or new_Y == 0 or new_Y == maxLength - 1
    if not isTouchWall:
         snake_X = new_X
         snake_Y = new_Y
    





# def starState():
#     global star_X, star_Y,currentSnakeCoordinate
#     new_X, new_Y = star_X, star_Y



main()
# if __name__ == "__main__":



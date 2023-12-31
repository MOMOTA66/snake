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
snake_Lenght = 1
star_symbol = " 星"
maxLength = 10
timeLength = 0.1
currentDirection = "right"  # 當前方向 右移
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
                # 打印 蛇的畫面
                elif i == snake_Y and j == snake_X:
                    print(snake_symbol, end="")
                # 打印 星星的畫面
                elif i == star_Y and j == star_X:
                    print(star_symbol, end="")
                # 打印 蛇身體的畫面
                elif (j, i) in snake_body:
                    
                    print(snake_symbol, end="")
                else:
                    print(empty, end=" ")
            # 打印畫面
            print()
        
        # 記錄 蛇 的路徑
        recordSnakePath()
        # print(snake_recordPath)
        # 更新 蛇 的狀態
        updateSnakeState()  
        if isEatStar():
            # 增加 蛇 的長度
            add_snake_Length_()
            # 更新 星 的位置
            randomStarPosition()

        print("當前分數", snake_Lenght)
        # 設定畫面更新時間
        time.sleep(timeLength)
        # 清除畫面
        os.system("cls" if os.name == "nt" else "clear")

# 蛇的狀態
def updateSnakeState():
    bodyLength()
    global snake_X, snake_Y, currentDirection
    new_X = snake_X
    new_Y = snake_Y

    if keyboard.is_pressed("right"):
        currentDirection = "right"
    elif keyboard.is_pressed("left"):
        currentDirection = "left"
    elif keyboard.is_pressed("up"):
        currentDirection = "up"
    elif keyboard.is_pressed("down"):
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

# 是否吃掉星星
def isEatStar():
    return snake_X == star_X and snake_Y == star_Y    


# 重新隨機產生星星位子
def randomStarPosition():
    # 防止無止盡的運算而卡住
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




# 更新蛇的身體位置
def bodyLength():
    global snake_body
    snake_body.insert(0, (snake_X, snake_Y))
    
    # 檢查蛇的身體長度是否大於等於 snake_length
    if len(snake_body) > snake_Lenght:
        snake_body.pop()


# 紀錄蛇的路徑
def recordSnakePath():
    global last_recorded_path
    snake_Path = (snake_X, snake_Y)
    # 當撞牆會累積同樣座標 須避免同座標一直被輸入
    if snake_Path != last_recorded_path:
        snake_recordPath.insert(0, snake_Path)
        last_recorded_path = snake_Path

# 增加蛇的長度
def add_snake_Length_():
    global snake_Lenght
    snake_Lenght = snake_Lenght + 1


main()

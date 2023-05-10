import random

# 生成随机数
number = random.randint(1, 100)

# 游戏开始
print("猜数字游戏开始了！请猜一个1到100之间的整数：")

while True:
    # 玩家猜测数字
    guess = int(input())

    # 判断猜测的数字与随机数的大小关系
    if guess == number:
        print("恭喜你，猜对了！")
        break
    elif guess > number:
        print("太大了，再猜一次吧：")
    else:
        print("太小了，再猜一次吧：")

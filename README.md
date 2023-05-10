# 导入游戏引擎模块和其他需要的模块
import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏界面的大小和标题
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("植物大战僵尸")

# 加载游戏所需的图片和音效资源
bg_image = pygame.image.load("background.png")
sunflower_image = pygame.image.load("sunflower.png")
zombie_image = pygame.image.load("zombie.png")
sun_sound = pygame.mixer.Sound("sun.wav")
shoot_sound = pygame.mixer.Sound("shoot.wav")

# 创建玩家、植物、僵尸等对象
player = Player()
plants = []
zombies = []
# 游戏循环
while True:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 处理玩家点击事件
            pos = pygame.mouse.get_pos()
            x, y = pos[0], pos[1]
            if player.get_sun(x, y):
                # 玩家收集阳光
                sun_sound.play()
                player.sun += 25
            elif player.buy_sunflower(x, y):
                # 玩家购买向日葵
                if player.sun >= 50:
                    player.sun -= 50
                    plants.append(Sunflower())
            elif player.buy_peashooter(x, y):
                # 玩家购买豌豆射手
                if player.sun >= 100:
                    player.sun -= 100
                    plants.append(Peashooter())
        elif event.type == pygame.KEYDOWN:
            # 处理键盘按键事件
            if event.key == pygame.K_SPACE:
                # 玩家种植植物
                player.plant_mode = not player.plant_mode

    # 更新游戏元素的状态和位置
    player.update()
    for plant in plants:
        plant.update()
    for zombie in zombies:
        zombie.update()

    # 检

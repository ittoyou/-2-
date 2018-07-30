import pygame
pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480, 700))
#把图片加载进来
bg =pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
#把图片加载进来
bg =pygame.image.load("./images/hero1.png")
screen.blit(bg,(200,500))
#更新的意思
pygame.display.update()

#游戏时钟
clock = pygame.time.Clock()
i = 0
while True:
    clock.tick(60)#一秒刷新60次
    i+=1
    print(i)

pygame.quit()


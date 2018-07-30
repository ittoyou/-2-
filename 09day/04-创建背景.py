import pygame
pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480, 700))
#把图片加载进来
bg =pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
#更新的意思
pygame.display.update()
while True:
    pass

pygame.quit()

